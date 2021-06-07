#!/bin/bash

docker build
docker-compose build --parallel
docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
docker-compose push
