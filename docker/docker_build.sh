#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

docker system prune -f

source ${DIR}/docker_env.sh

docker build ${DIR}/.. -f ${DIR}/Dockerfile -t ${DOCKER_IMAGE_NAME}

docker image prune