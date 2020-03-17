#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source ${DIR}/docker_env.sh

while [ "$1" != "" ]; do
    case $1 in
        -b|-i|-r|--bird|--insect|--reptile)
            SKIMMER_ARGS="$SKIMMER_ARGS $1"
            ;;
        -c|-o|-f|-g|-s|--class|--order|--family|--genus|--species)
            SKIMMER_ARGS="$SKIMMER_ARGS $1"
            ;;
        -e|--enet)
            SKIMMER_ARGS="$SKIMMER_ARGS $1"
            shift
            SKIMMER_ARGS="$SKIMMER_ARGS $1"
            ;;
         -n|--name)
            SKIMMER_ARGS="$SKIMMER_ARGS $1"
            shift
            IMG=$1
            SKIMMER_ARGS="$SKIMMER_ARGS $IMG"
            ;;
    esac
    shift
done

DIR="$(dirname "$DIR")"

docker run --name $DOCKER_CONTAINER_NAME --entrypoint ./run_image.sh -v $DIR/$IMG:/skimmer/$IMG $DOCKER_IMAGE_NAME $SKIMMER_ARGS
docker rm -f $DOCKER_CONTAINER_NAME