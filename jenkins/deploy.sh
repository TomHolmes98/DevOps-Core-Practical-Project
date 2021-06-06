#!/bin/bash

ssh docker-manager << EOF
export DATABASE_URI=${DATABASE_URI}
ls
whoami
pwd
docker stack deploy --compose-file docker-compose.yaml app
EOF
