#!/bin/bash
# Check if docker image exists, and if it does, run docker-compose down, and remove the image
if docker images | grep -q $IMAGE_NAME; then
    echo "Docker image $IMAGE_NAME already exists"
    docker-compose down
    # docker rmi $IMAGE_NAME
else
    echo "Docker image $IMAGE_NAME does not exist"
fi
# docker volume rm agentic-hackathon_langgraph-data
langgraph build -t $IMAGE_NAME

docker-compose up -d