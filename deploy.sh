#!/bin/bash

echo "=== DEPLOY START ==="
cd /home/jiehoes/geonode-project || exit

git pull origin master


echo "=== DEPLOY DONE ==="
echo "WHOAMI: $(whoami)"
