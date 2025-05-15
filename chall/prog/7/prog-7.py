from time import time
from random import seed, randint

secret_num = int(time())

flag = input("Enter flag: ")
if len(flag) < 6 or flag[:4] != "prog":
    print("Flag format is incorrect!")
    exit(1)

print("Encrypting...")

seed(secret_num)

encrypted = ""

for c in flag.strip():
    encrypted += chr((ord(c) + randint(1, 255)) % 255)

encrypted_hex = encrypted.encode("utf-8").hex()

print(f"Encrypted: {encrypted_hex}")
# 1530c2bc2ec2a22ec38cc2b9c38378c29fc385c286491f04c2b6c299c38fc3a7552dc2be662dc2a3c3b5c39a0859
