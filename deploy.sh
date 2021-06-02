#!/bin/bash

#Build server image 
docker build -t service-1_api service-1

#Build api images
docker build -t service-2_api service-2
docker build -t service-3_api service-3
docker build -t service-4_api service-4


#Create network 
docker network create cricket_shot_network


#Run containers 

docker run -d -p 5000:5000 --name service-1_api --network create cricket_shot_network service-1_api
docker run -d --name service-2_api --network create cricket_shot_network service-2_api
docker run -d --name service-3_api --network create cricket_shot_network service-3_api
docker run -d --name service-4_api --network create cricket_shot_network service-4_api