import asyncio
import socket

from random import shuffle
from multiprocessing import Process

pport: None | int = None

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    addr = writer.get_extra_info("peername")
    print(f"[{pport}] Connection: {addr}")

    writer.write(b"Hello! You sent 'find', so we will randomly generate a number between 1 and 100 for you. If you get 100, respond with 'catch' within 1 seconds to claim your prize.\n")
    await writer.drain()

    numbers = [i for i in range(1, 101)]
    shuffle(numbers)

    for number in numbers:
        try:
            data = await asyncio.wait_for(reader.read(100), timeout=1.0)
        except asyncio.TimeoutError:
            writer.write(b"Timeout!\n")
            await writer.drain()
            writer.close()
            return

        if data.strip() == b"find":
            writer.write(f"{number}\n".encode())
            await writer.drain()

            if number == 100:
                try:
                    data = await asyncio.wait_for(reader.read(100), timeout=1.0)
                    if data.strip() == b"catch":
                        print(f"[{pport}] Solved: {addr}")
                        writer.write(b"Congratulations!\nFlag: prog{7h475_3xc171n9}\n")
                        await writer.drain()
                        writer.close()
                        return
                    else:
                        writer.write(b"Wrong response. Bye!\n")
                        await writer.drain()
                        writer.close()
                        return
                except asyncio.TimeoutError:
                    writer.write(b"Timeout!\n")
                    await writer.drain()
                    writer.close()
                    return
        else:
            writer.write(b"Wrong response. Bye!\n")
            await writer.drain()
            writer.close()
            return

    writer.write(b"Error\n")
    await writer.drain()
    writer.close()

async def main(port: int):
    global pport
    pport = port

    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)

    sock.bind(("::", port))
    sock.listen(100)
    sock.setblocking(False)

    print(f"[{pport}] Started")

    server = await asyncio.start_server(handle_client, sock=sock)
    async with server:
        await server.serve_forever()

def start_server(port: int):
    asyncio.run(main(port))

if __name__ == "__main__":
    procs = []
    for port in [8000, 8001, 8002, 8003]:
        p = Process(target=start_server, args=(port, ))
        p.daemon = True
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
