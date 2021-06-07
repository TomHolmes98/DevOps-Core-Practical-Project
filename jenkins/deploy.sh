#!/bin/bash
scp docker-compose.yaml docker manager:
ssh docker-manager << EOF

export DATABASE_URI=${DATABASE_URI}

docker stack deploy --compose-file docker-compose.yaml project
EOF
