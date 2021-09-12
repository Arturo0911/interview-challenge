#!/bin/bash


echo "first checking the docker version installed"
docker version

docker-compose build && docker-compose up
