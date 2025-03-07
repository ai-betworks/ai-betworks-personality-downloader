from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel

from deployment_graph import deployment_agent
from eliza_generator_graph import eliza_generator_agent
from models import MasterState
from research_graph import research_agent
from tools.common import default_llm

load_dotenv()


class SetPublicFigure(BaseModel):
    public_figure: str


def set_public_figure(state: MasterState):
    """Set the public figure name from user input"""

    # TODO Later search for Instagram, LinkedIn, TikTok
    extract_public_figure_sys_msg = SystemMessage(
        content="""
    The user will give you a message containing the name of a public figure.
    
    Your goal is to extract the name from their query and return the following JSON:
    {{
        "public_figure": string, // The name of the public figure. If you are unable to extract the name, leave it blank.
    }}
    
    Do not respond with anything other than the above JSON.
    """
    )
    structured_llm = default_llm().with_structured_output(SetPublicFigure)
    res = structured_llm.invoke([extract_public_figure_sys_msg] + state["messages"])
    if not res.public_figure:
        raise ValueError(
            "Unable to extract public figure name from user input, aborting"
        )
    return {"public_figure": res.public_figure}


# Add nodes and edges
personality_downloader_agent_builder = StateGraph(MasterState)
personality_downloader_agent_builder.add_node("set_public_figure", set_public_figure)
personality_downloader_agent_builder.add_node("research_agent", research_agent)
personality_downloader_agent_builder.add_node(
    "eliza_generator_agent", eliza_generator_agent
)
personality_downloader_agent_builder.add_node("deployment_agent", deployment_agent)

personality_downloader_agent_builder.add_edge(START, "set_public_figure")
personality_downloader_agent_builder.add_edge("set_public_figure", "research_agent")
personality_downloader_agent_builder.add_edge("research_agent", "eliza_generator_agent")
personality_downloader_agent_builder.add_edge(
    "eliza_generator_agent", "deployment_agent"
)
personality_downloader_agent_builder.add_edge("deployment_agent", END)

# Compile
# memory = MemorySaver()
personality_downloader_agent = personality_downloader_agent_builder.compile()
