from random import seed, randint
from datetime import datetime

flag = "1530c2bc2ec2a230c2acc393c29838c29cc29e6e2101c392727ec2a5c3aa5e27c2981d4e7fc39cc3a6c3864a69c394c288c3906f484ec282c2a30ec290c3adc3aa2e06c38a"
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
