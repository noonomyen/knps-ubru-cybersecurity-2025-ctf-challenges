import socket
import socketserver
import random
import time
import string
from ascii_art import ASCII_ART, AVAILABLE_CHARS # Import จากไฟล์ ascii_art.py

HOST, PORT = "0.0.0.0", 8013
FLAG = "prog{rPJSLZooaqaTzugrOag9uqax!}"
CAPTCHA_LENGTH = 7
ROUNDS_TO_WIN = 15
TIMEOUT_SECONDS = 30.0

class CaptchaHandler(socketserver.BaseRequestHandler):
    def send_line(self, message):
        self.request.sendall(message.encode('utf-8') + b'\n')

    def recv_line(self, timeout=None):
        self.request.settimeout(timeout)
        try:
            data = self.request.recv(1024).strip()
            return data.decode('utf-8')
        except socket.timeout:
            return None
        except ConnectionResetError:
            print(f"Client {self.client_address} disconnected abruptly.")
            return "RESET"
        finally:
            self.request.settimeout(None)

    def handle(self):
        print(f"Connected by {self.client_address}")
        self.send_line("Welcome to ASCII Art Captcha Challenge!")
        self.send_line(f"You need to solve {ROUNDS_TO_WIN} rounds.\n")
        self.send_line(f"Each CAPTCHA is {CAPTCHA_LENGTH} characters long.")
        self.send_line(f"You have {TIMEOUT_SECONDS} seconds to answer AFTER all characters are shown.")
        # --- FIX HERE ---
        self.send_line("Let's begin!") # ลบ \n ที่เกินออก
        time.sleep(0.1)
        # --- END FIX ---

        if not AVAILABLE_CHARS:
            self.send_line("Server error: No ASCII art available. Please contact admin.")
            print("Error: AVAILABLE_CHARS is empty in ascii_art.py")
            return

        for round_num in range(1, ROUNDS_TO_WIN + 1):
            self.send_line(f"--- Round {round_num}/{ROUNDS_TO_WIN} ---")
            time.sleep(0.1)
            captcha_string = "".join(random.choice(AVAILABLE_CHARS) for _ in range(CAPTCHA_LENGTH))

            for char_to_display in captcha_string:
                art_lines = ASCII_ART.get(char_to_display)
                if not art_lines:
                    self.send_line(f"Error: Art for '{char_to_display}' not found. Sending placeholder.")
                    for _ in range(5):
                        self.send_line("?????")
                else:
                    for line in art_lines:
                        self.send_line(line)
                self.send_line("<------------>")
                time.sleep(0.1)

            self.send_line(f"Enter the {CAPTCHA_LENGTH}-character string: ")

            start_time = time.time() # ไม่ได้ใช้ end_time ใน logic timeout ตรงนี้, recv_line จัดการ timeout
            user_answer = self.recv_line(timeout=TIMEOUT_SECONDS)
            # end_time = time.time() # ถ้าจะใช้ เช็ค delta time เอง

            if user_answer is None:
                self.send_line("Timeout! Too slow.")
                print(f"Client {self.client_address} timed out on round {round_num}.")
                return
            if user_answer == "RESET":
                return

            if len(user_answer) != CAPTCHA_LENGTH:
                self.send_line(f"Invalid input length. Expected {CAPTCHA_LENGTH} characters.")
                print(f"Client {self.client_address} sent wrong length on round {round_num}.")
                return

            if user_answer == captcha_string:
                self.send_line("Correct!")
                if round_num == ROUNDS_TO_WIN:
                    self.send_line(f"Congratulations! Here is your flag: {FLAG}")
                    print(f"Client {self.client_address} got the flag!")
                else:
                    self.send_line("") # เว้นบรรทัดก่อน round ใหม่
            else:
                self.send_line(f"Incorrect. The answer was: {captcha_string}")
                print(f"Client {self.client_address} failed round {round_num}. Expected: {captcha_string}, Got: {user_answer}")
                return

        print(f"Client {self.client_address} finished.")

if __name__ == "__main__":
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer((HOST, PORT), CaptchaHandler)
    print(f"Server listening on {HOST}:{PORT}")
    print(f"Ensure you have populated ascii_art.py with enough characters (at least {len(AVAILABLE_CHARS)} available).")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server shutting down.")
        server.shutdown()
        server.server_close()