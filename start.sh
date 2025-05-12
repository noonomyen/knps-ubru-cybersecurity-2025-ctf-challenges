#!/usr/bin/bash

set -e

if ! docker image inspect "scc-bun-web-base:latest" >/dev/null 2>&1; then
    echo "Image scc-bun-web-base:latest not found. Running build.sh..."
    cd ./chall/_assets/bun-web-base
    ./build.sh
    cd ../../../
else
    echo "Image scc-bun-web-base:latest already exists."
fi

cd ctfd
docker compose build
docker compose up
