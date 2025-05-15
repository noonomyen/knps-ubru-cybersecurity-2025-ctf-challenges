from random import seed, randint
from datetime import datetime

flag = "1530c2bc2ec2a22ec38cc2b9c38378c29fc385c286491f04c2b6c299c38fc3a7552dc2be662dc2a3c3b5c39a0859"
flag = bytes.fromhex(flag).decode("utf-8")
secret_num = int(datetime(2025, 5, 12, 0, 0, 0).timestamp())

while True:
    seed(secret_num)
    de = ""
    for c in flag:
        de += chr((ord(c) - randint(1, 255)) % 255)

    if de.startswith("prog"):
        print(f"{datetime.fromtimestamp(secret_num)} ({secret_num})")
        print(f"Decrypted: {de}")
        break

    secret_num += 1
