from random import randint

flag = [235, 237, 234, 226, 246, 180, 238, 207, 211, 235, 202, 224, 190, 223, 202, 225, 193, 205, 207, 228, 194, 233, 206, 229, 235, 197, 224, 230, 245, 248]

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
