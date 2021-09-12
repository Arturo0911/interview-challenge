#!/bin/bash


echo "first checking the docker version installed"
docker version

doker-compose build && docker-compose up
