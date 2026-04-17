#!/bin/bash

echo "=== DEPLOY START ==="
cd /home/jiehoes/geonode-project || exit

git pull origin main

docker compose down
docker compose up -d 

echo "=== DEPLOY DONE ==="
