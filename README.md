# DevOps-Core-Practical-Project

## Contents

* [Introduction](#introduction)
    * [Brief](#brief)
    * [Proposal](#proposal)
* [Architcture](#architecture)
    * [Risk Assessment](#risk-assessment)
    * [Trello Board](#trello-board)
    * [CI-Pipeline](#ci-pipeline)
* [Infrastructure](#infrastructure)
    * [Jenkins](#jenkins)
    * [Entity Diagram](#entity-diagram)
    * [Docker Swarm](#docker-swarm)
* [Development](#development)
    * [Unit Testing](#unit-testing)
    * [Front End Design](#front-end-design)

## Introduction

### Brief

The brief for this project was "to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together."

### Proposal

In order to meet the requirements set out within the brief I began planning my sprint in order to ensure that I could produce an application that utilised the CI/CD pipeline.

The idea that I came up with was to create 4 services based on cricket that gives the user a random player shot and score:
* The front end - which provides the results of the services working together, as well as the past 5 results found from within the database.
* Service 2 - Creates a random name for the player.
* Service 3 - Creates a random shot.
* Service 4 - Returns a score based on the random inputs that it gets from Service 2 and 3.

[![Image from Gyazo](https://i.gyazo.com/403c135785fd73d7e9089bd8f82851ba.png)](https://gyazo.com/403c135785fd73d7e9089bd8f82851ba)

## Architecture

### Risk Assessment

A detailed risk assessment was carried out in order to monitor any potential risks that might have been encountered throughout the project. Below are 2 risk assessments, one from the beginning of the project and the second is one done towards the end of the project in order to assess how the risk assessment impacted the sprint.

[![Image from Gyazo](https://i.gyazo.com/5f349f0fa6f71fb3b5abdfb9e61fff5c.png)](https://gyazo.com/5f349f0fa6f71fb3b5abdfb9e61fff5c)
[![Image from Gyazo](https://i.gyazo.com/cc9b05d9183509d50c77ae77c2bce027.png)](https://gyazo.com/cc9b05d9183509d50c77ae77c2bce027)


### Trello Board

A Trello board was used throughout the sprint as a means of project tracking, below are images taken at different stages throughout the sprint, the green colour on the majority of the boards represents the importance (MosCow Prioritisation) of the individual task.

[![Image from Gyazo](https://i.gyazo.com/e4d7ffa93a9bb3f67441bd2a2fcec4dc.png)](https://gyazo.com/e4d7ffa93a9bb3f67441bd2a2fcec4dc)

[![Image from Gyazo](https://i.gyazo.com/7240dc9b3f98ca008624501058b7d4fa.jpg)](https://gyazo.com/7240dc9b3f98ca008624501058b7d4fa)

[![Image from Gyazo](https://i.gyazo.com/84c2a185801edaedfd0677c86ef6e999.jpg)](https://gyazo.com/84c2a185801edaedfd0677c86ef6e999)

### CI-Pipeline

[![Image from Gyazo](https://i.gyazo.com/6beaa368c77f955b4b7a9d4509174494.png)](https://gyazo.com/6beaa368c77f955b4b7a9d4509174494)

## Infrastructure

### Jenkins

Job 1: Testing
<br>
Jenkins runs unit tests which test each service in order to make sure they are running properly.

```
for service in service-2 service-3 service-4 server
do
    python3 -m pytest $service --cov=$service --cov-report=xml --junitxml=junit/test-results.xml
done
```
The code above individually tests each service within the application.

Job 2: Build & Push
<br>
Jenkins uses the following code to build and push the docker images.

```
#!/bin/bash

docker-compose build --parallel
docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
docker-compose push
```
The credentials are stored within the Jenkins UI.

Job 3: Ansible
<br>
Ansible is then installed on the Jenkins server in order to help configure the docker-manager and the docker-worker. The inventory.yaml and playbook.yaml are also setup aswell as the roles, allowing for the swarm manager and worker to be setup.

Job 4: Deployment
<br>
Jenkins uses the docker-compose.yaml file in order to then deploy the app within the swarm.

### Entity Diagram

[![Image from Gyazo](https://i.gyazo.com/848eaaf830d01dfa402d1ab02004630e.png)](https://gyazo.com/848eaaf830d01dfa402d1ab02004630e)

### Docker Swarm

Docker swarm is used as an orchstration tool in which a network is created in order to host the app.

## Development

### Unit Testing

Unit testing was implemented throughout the sprint in order to test the functionality of the app. Testing is used with Jenkins to make it part of the CI Pipeline.

[![Image from Gyazo](https://i.gyazo.com/ba362fa030495851dc96fe803bff39fa.png)](https://gyazo.com/ba362fa030495851dc96fe803bff39fa)

[![Image from Gyazo](https://i.gyazo.com/d0e8bf2265ebae9a190bb0496a3cad51.png)](https://gyazo.com/d0e8bf2265ebae9a190bb0496a3cad51)

[![Image from Gyazo](https://i.gyazo.com/abb7d5980676b50c7d038df7dab41003.png)](https://gyazo.com/abb7d5980676b50c7d038df7dab41003)

### Front End Design

The Frontend design shows the service created by the microservices in the backend of the application. When refreshed the app shows a different combination of player shot and score.

[![Image from Gyazo](https://i.gyazo.com/4900ef0188eb597fc2868a9a9ddbb78d.png)](https://gyazo.com/4900ef0188eb597fc2868a9a9ddbb78d)

[![Image from Gyazo](https://i.gyazo.com/b97139485808f658c43c9fbb2aac36a5.png)](https://gyazo.com/b97139485808f658c43c9fbb2aac36a5)

## Imporvements

Implement NGINX as a reverse proxy.
<br>
Create a more advanced version 2.

## Acknowledgements

Ollie Nichols
<br>
Harry Volker









