#!/bin/bash
DOCKER_IMAGE_NAME=demulab/ros2:latest

./stop-docker-container.sh
docker build ./docker -t $DOCKER_IMAGE_NAME #--no-cache=true
