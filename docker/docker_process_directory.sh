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
         --dir)
            shift
            SKIMMER_DIR=$1
            ;;
         --output)
            shift
            OUTPUT=$1
            ;;
    esac
    shift
done

DIR="$(dirname "$DIR")"

docker run --name $DOCKER_CONTAINER_NAME -v $DIR/$SKIMMER_DIR:/skimmer/images $DOCKER_IMAGE_NAME $SKIMMER_ARGS
docker cp $DOCKER_CONTAINER_NAME:$WORKDIR/$OUTPUT $SKIMMER_DIR.csv
docker rm -f $DOCKER_CONTAINER_NAME