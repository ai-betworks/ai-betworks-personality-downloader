import json
from typing import TypedDict
from typing_extensions import Annotated
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel
from models import ElizaDict, MasterState
from langgraph.graph import MessagesState
import os
import requests
import logging
from models import DeploymentDict
from tools.common import reduce_dict_merge


class DeploymentGraphOutput(MessagesState):
    public_figure: str
    eliza: Annotated[ElizaDict, reduce_dict_merge]
    deployment: Annotated[DeploymentDict, reduce_dict_merge]


def create_eliza_output_file(state: MasterState):
    public_figure = state.get("public_figure")
    eliza = state.get("eliza")

    eliza["clients"] = ["twitter", "discord"]
    eliza["modelProvider"] = "anthropic"
    eliza["plugins"] = ["twitter", "solana"]
    # Convert public figure name to lowercase alphanumeric with underscores
    filename = "".join(c.lower() if c.isalnum() else "_" for c in public_figure)
    filename = f"personalities/{filename}.json"

    with open(filename, "w") as f:
        json.dump(eliza, f, indent=2)
    return {"deployment": {}}


def deploy_to_autonome(state: MasterState):
    # Get settings from environment variable    s
    autonome_jwt = os.getenv("AUTONOME_JWT_TOKEN")  # TODO move this to state
    autonome_rpc = os.getenv("AUTONOME_RPC")
    eliza = state.get("eliza")
    if not eliza:
        print("No eliza found in state, cannot deploy")
        return {
            "deployment": {
                "target_platform": "autonome",
                "endpoint": "",
                "success": False,
                "raw_output": "eliza configuration not found in state",
            }
        }

    request_body = {
        "name": eliza["name"],
        "config": eliza,
        "creationMethod": 2,
        "envList": {},
        "templateId": "Eliza",
    }

    headers = {
        "Authorization": f"Bearer {autonome_jwt}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(autonome_rpc, json=request_body, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        resp_data = response.json()
        if resp_data.get("app", {}).get("id"):
            app_id = resp_data["app"]["id"]
            app_url = f"https://dev.autonome.fun/autonome/{app_id}/details"
            print(f"Launching successful, please find your agent on: {app_url}")
            return {
                "deployment": {
                    "target_platform": "autonome",
                    "endpoint": app_url,
                    "success": True,
                    "raw_output": resp_data,
                }
            }
    except:
        return {
            "deployment": {
                "target_platform": "autonome",
                "endpoint": app_url,
                "success": False,
                "raw_output": resp_data,
            }
        }

    # except requests.exceptions.RequestException as error:
    #     if callback:
    #         eliza_logger.error("Error during launching agent")
    #         eliza_logger.error(str(error))
    #         callback({
    #             'text': f"Error launching agent: {str(error)}",
    #             'content': {'error': str(error)}
    #         })
    #     return False


deployment_agent_builder = StateGraph(DeploymentGraphOutput)
deployment_agent_builder.add_node("create_eliza_output_file", create_eliza_output_file)

deployment_agent_builder.add_edge(START, "create_eliza_output_file")
deployment_agent_builder.add_edge("create_eliza_output_file", END)

deployment_agent = deployment_agent_builder.compile()
