import socket
import re

HOST = 'localhost'
PORT = 8012

def calculate_answer(num1: int, operator: str, num2: int) -> int:
    """
    Implement the logic to solve the math problem.

    Args:
        num1 (int): The first number.
        operator (str): The operator (+, -, *, /).
        num2 (int): The second number.

    Returns:
        int: The result of the calculation.
    """

def handle_line(line: str, sock: socket.socket):
    print(f"S: {line}")

    if any(term in line for term in ["Incorrect.", "Timeout!", "Invalid input.", "Game Over."]):
        print("[*] Game Over.")
        return False

    if "programming{" in line:
        print(f"[*] FLAG FOUND: {line}")
        return False

    match = re.search(r"Question \d+/\d+: (\d+) ([+\-*/]) (\d+) = \?", line)
    if match:
        num1, operator, num2 = map(str, match.groups())
        print(f"[*] Parsed problem: {num1} {operator} {num2}")

        try:
            result = calculate_answer(int(num1), operator, int(num2))
            print(f"C: {result}")
            sock.sendall(f"{result}\n".encode('utf-8'))
        except Exception as e:
            print(f"[!] Error solving problem: {e}")
            sock.sendall(b"error\n")
            return False

    return True

def run_bot():
    try:
        with socket.create_connection((HOST, PORT)) as sock:
            print(f"[*] Connected to {HOST}:{PORT}")
            buffer = ""

            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    print("[*] Server closed the connection.")
                    break

                buffer += chunk.decode('utf-8')
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    line = line.strip()

                    if line:
                        keep_running = handle_line(line, sock)
                        if not keep_running:
                            return
    except ConnectionRefusedError:
        print(f"[!] Connection refused. Is the server running on {HOST}:{PORT}?")
    except socket.timeout:
        print("[!] Socket timed out.")
    except ConnectionResetError:
        print("[!] Connection reset by server.")
    except BrokenPipeError:
        print("[!] Broken pipe. Server likely closed the connection.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
    finally:
        print("[*] Disconnected.")

if __name__ == "__main__":
    run_bot()
