from random import randint

flag = [80, 82, 79, 71, 91, 24, 18, 85, 23, 19, 63, 70, 16, 18, 67, 19, 93]

secret = randint(1, 1024)

decoded = "flag"
try:
    decoded = "".join([chr((c - secret) % 256) for c in flag])
except Exception:
    pass
finally:
    if decoded[:4] != "prog":
        print("Incorrect secret number!")
    else:
        print("Decoded:", decoded)
        print("Secret number:", secret)
