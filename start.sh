#!/usr/bin/bash

set -e

if ! docker image inspect "scc-bun-web-base:latest" >/dev/null 2>&1; then
    (cd ./chall/_assets/bun-web-base && ./build.sh)
else
    echo "Image scc-bun-web-base:latest already exists."
fi

cd ./server
docker compose build
docker compose up
