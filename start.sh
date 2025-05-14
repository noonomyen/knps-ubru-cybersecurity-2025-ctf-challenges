#!/usr/bin/bash

set -e

if ! docker image inspect "scc-bun-web-base:latest" >/dev/null 2>&1; then
    (cd ./chall/_assets/bun-web-base && ./build.sh)
fi

if ! docker image inspect "scc-status-service:latest" >/dev/null 2>&1; then
    (cd ./server/status && ./build.sh)
fi

cd ./server
docker compose build
docker compose up
