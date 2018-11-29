#!/bin/sh

# Assumes username and password variables from docker build are correct
#docker run -it --rm -p 5001:80 fbg

# This is how to override the username and password needed
#docker run -it --rm -p 5001:80 -e username="test_user" -e password="test_password" fbg

# This is how to override the pages.json file so that the docker container
# doesn't need to be rebuilt, only re-deployed
docker run -it --rm -p 5001:80 -e username="test_user" -e password="test_password" -v $(pwd)/app/pages.json:/app/pages.json fbg

# This is how to run it for permanent deployment
#docker run -d --name fbg --restart on-failure  -p 5001:80 -e username="test_user" -e password="test_password" -v $(pwd)/app/pages.json:/app/pages.json fbg
