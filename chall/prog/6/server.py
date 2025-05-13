import asyncio
import random

HOST = '0.0.0.0'
PORT = 8012
FLAG = "prog{7h15_m47h_700_f457!!@}"
NUM_QUESTIONS_TO_WIN = 10
TIME_LIMIT_PER_QUESTION = 3

def generate_problem():
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        answer = num1 + num2
    elif operator == '-':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, num1)
        answer = num1 - num2
    elif operator == '*':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 50)
        answer = num1 * num2
    elif operator == '/':
        answer = random.randint(1, 50)
        num2 = random.randint(1, 50)
        num1 = answer * num2

    problem = f"{num1} {operator} {num2} = ?"
    return problem, answer

async def send_message(writer: asyncio.StreamWriter, message: str):
    writer.write(message.encode('utf-8'))
    await writer.drain()

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    print(f"[+] New connection from {addr}")

    await send_message(writer, "Welcome to the Math Challenge!\n")
    await send_message(writer, f"Solve {NUM_QUESTIONS_TO_WIN} problems correctly within {TIME_LIMIT_PER_QUESTION} seconds each to get the flag.\n")
    await send_message(writer, "Send only the answer, followed by a newline.\n\n")

    score = 0

    try:
        for i in range(NUM_QUESTIONS_TO_WIN):
            problem, correct_answer = generate_problem()
            await send_message(writer, f"Question {i+1}/{NUM_QUESTIONS_TO_WIN}: {problem}\nYour answer: ")

            try:
                # รอรับคำตอบพร้อม timeout
                answer_task = reader.readline()
                client_answer_raw = await asyncio.wait_for(answer_task, timeout=TIME_LIMIT_PER_QUESTION)
                client_answer_raw = client_answer_raw.decode('utf-8').strip()

                if not client_answer_raw:
                    await send_message(writer, "No answer received. Game Over.\n")
                    print(f"[-] Client {addr} sent empty answer or disconnected.")
                    break

                try:
                    client_answer = int(client_answer_raw)
                except ValueError:
                    await send_message(writer, "Invalid input. Please send numbers only. Game Over.\n")
                    print(f"[-] Client {addr} sent invalid input.")
                    break

                if client_answer == correct_answer:
                    score += 1
                    await send_message(writer, f"Correct! Score: {score}/{NUM_QUESTIONS_TO_WIN}\n\n")
                else:
                    await send_message(writer, f"Incorrect. The correct answer was {correct_answer}. Game Over.\n")
                    print(f"[-] Client {addr} answered incorrectly.")
                    break

                if score == NUM_QUESTIONS_TO_WIN:
                    await send_message(writer, f"Congratulations! You solved all {NUM_QUESTIONS_TO_WIN} problems!\n")
                    await send_message(writer, f"Here is your flag: {FLAG}\n")
                    print(f"[+] Client {addr} got the flag!")
                    break

            except asyncio.TimeoutError:
                await send_message(writer, f"Timeout! You took too long ({TIME_LIMIT_PER_QUESTION}s limit). Game Over.\n")
                print(f"[-] Client {addr} timed out.")
                break

    except Exception as e:
        print(f"[!] Error with client {addr}: {e}")
    finally:
        print(f"[-] Connection closed with {addr}")
        writer.close()
        await writer.wait_closed()

async def start_server():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"[*] Listening on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("\n[*] Server shutting down.")
