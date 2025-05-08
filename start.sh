#!/usr/bin/bash

set -e

if ! docker image inspect "scc-web-chall-bun-base:latest" >/dev/null 2>&1; then
    echo "Image scc-web-chall-bun-base:latest not found. Running build.sh..."
    cd ./chall/web/base.3-4-5
    ./build.sh
    cd ../../../
else
    echo "Image scc-web-chall-bun-base:latest already exists."
fi

cd ctfd
docker compose build
docker compose up
