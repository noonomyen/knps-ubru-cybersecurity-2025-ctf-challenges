FROM oven/bun:1.2.10

COPY . /app

WORKDIR /app

RUN bun install

RUN bun run build

CMD ["bun", "start"]
