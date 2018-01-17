#!/bin/sh

cd $(dirname $0)

if [ $(cat $HOME/.docker/config.json | grep auths | wc -l) -eq 0 ]; then
    if docker login registry.laboratorium.ee; then
        echo "Login successful"
    else
        read
        exit 1
    fi
fi

docker-compose build
docker-compose up

read
