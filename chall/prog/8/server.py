import asyncio
import socket

from random import shuffle
from multiprocessing import Process
from os import cpu_count, getpid
from time import sleep

CPUS = cpu_count()
if CPUS is None:
    CPUS = 1
    print("Warning: CPU count is None, defaulting to 1.")

async def async_server(id: int) -> None:
    sock: socket.socket

    if socket.has_dualstack_ipv6():
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    sock.bind(("", 8012))
    sock.setblocking(False)
    sock.listen(16)

    print(f"[{id}:{getpid()}] Listening on {sock.getsockname()}")

    PID = getpid()

    async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        addr = writer.get_extra_info("peername")
        print(f"[{id}:{PID}] Connection from {addr}")

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
                            print(f"[{id}:{PID}] Solved: {addr}")
                            writer.write(b"Congratulations!\nFlag: prog{aPqyYvklvtsuU9NbFav2bHCB}\n")
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

    server = await asyncio.start_server(handler, sock=sock)

    try:
        await server.serve_forever()
    except asyncio.exceptions.CancelledError:
        print(f"[{id}:{PID}] Server cancelled")
        server.close()
        await server.wait_closed()

def process(id: int) -> None:
    asyncio.run(async_server(id))

if __name__ == "__main__":
    PID = getpid()
    print(f"[main:{PID}] Starting server with {CPUS} processes")
    procs: list[Process] = []

    for id in range(CPUS):
        proc = Process(target=process, args=(id,))
        proc.daemon = True
        proc.start()
        print(f"[main:{PID}] Started process {proc.pid}")
        procs.append(proc)

    try:
        while True:
            for id, proc in enumerate(procs):
                if not proc.is_alive():
                    print(f"[main:{PID}] Process {proc.pid} is not alive, restarting")
                    new_proc = Process(target=process, args=(id,))
                    new_proc.daemon = True
                    new_proc.start()
                    procs[id] = new_proc
                    print(f"[main:{PID}] Restarted process {new_proc.pid}")
            sleep(1)
    except KeyboardInterrupt:
        print(f"[main:{PID}] Keyboard interrupt, terminating processes")
        for proc in procs:
            proc.terminate()
            proc.join()

    print(f"[main:{PID}] All processes terminated")
    print(f"[main:{PID}] Server stopped")
