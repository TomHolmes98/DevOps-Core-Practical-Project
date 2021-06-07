#!/bin/bash

#Build server image 
docker build -t server server

#Build api images
docker build -t service-2_api service-2
docker build -t service-3_api service-3
docker build -t service-4_api service-4


#Create network 
docker network create cricket_shot_network


#Run containers 

docker run -d -p 5000:5000 --name server --network cricket_shot_network -e DATABASE_URI=$DATABASE_URI server
docker run -d --name service-2_api --network cricket_shot_network service-2_api
docker run -d --name service-3_api --network cricket_shot_network service-3_api
docker run -d --name service-4_api --network cricket_shot_network service-4_api