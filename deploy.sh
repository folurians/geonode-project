#!/bin/bash

echo "=== DEPLOY START ==="

cd /home/jiehoes/geonode-project || exit

git fetch origin
git reset --hard origin/master

echo "=== DEPLOY DONE ==="