# How to use

## Local development

Notebook has commands you can run to test individual parts of the graph.

To run against a real REST API that you can hook up to a frontend:
```bash
pip install -U langgraph-cli   
pip install -U "langgraph-cli[inmem]"
langgraph dev
```

To run against self-hosted infra:
```bash
langgraph build -t $IMAGE_NAME
docker-compose up -d
```


# ad0ll's research and pre-work for the Agentic hackathon

Private repo created to demo AI concepts and test POCs for ideas being brainstormed.

The contents of this repo cannot be used as is for the hackathon, please only use as a reference.

I have uploaded this early since some content can be used as a reference for our trading bot

