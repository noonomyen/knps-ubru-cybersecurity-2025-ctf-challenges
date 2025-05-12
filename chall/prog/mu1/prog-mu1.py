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
# 1530c2bc2ec2a230c2acc393c29838c29cc29e6e2101c392727ec2a5c3aa5e27c2981d4e7fc39cc3a6c3864a69c394c288c3906f484ec282c2a30ec290c3adc3aa2e06c38a
