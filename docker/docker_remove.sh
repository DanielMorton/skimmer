#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source $DIR/docker_env.sh

if [ $1 == "-c" ]
then
    docker rm -f $DOCKER_CONTAINER_NAME
elif [ $1 == "-i" ]
then
    docker image prune -f
    docker rmi -f $DOCKER_IMAGE_NAME
fi