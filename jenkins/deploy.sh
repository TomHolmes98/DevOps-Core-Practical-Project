#!/bin/bash

ssh docker-manager << EOF
export DATABASE_URI=${DATABASE_URI}

docker stack deploy --compose-file docker-compose.yaml service
EOF
