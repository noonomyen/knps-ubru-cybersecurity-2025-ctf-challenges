FROM scc-bun-web-base:latest

WORKDIR /app

COPY . .

RUN bun run build

CMD ["bun", "start"]
