FROM oven/bun:1.2.10 AS scc-bun-web-base

WORKDIR /app

COPY . .

RUN bun install --frozen-lockfile
