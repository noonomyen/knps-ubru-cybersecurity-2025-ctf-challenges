print("Locker")

password: None | str = None
try:
    password = open("./password.txt", "r", encoding="utf-8").read().strip()
except Exception:
    pass
finally:
    if password is None:
        print("Locker is not available. password.txt not found.")
        exit(1)

pass_ = password == input("Enter password: ")

if pass_:
    print("Correct !")
    print(bytes.fromhex("".join(map(chr, [i^0x63+int(pass_)*1 for i in [i^0xc4+int(pass_)*4 for i in [i^0x30+int(pass_)*2 for i in [i^0x93+int(pass_)*3 for i in bytes.fromhex("3f383f3a3e6e3e3f3f6a3b383b383f383b3d3d6e3e3c3b393e3c3d6e3f313b383f3d3d6e3e3b3e303b3c3e6d3b313b3b3d6e3b3f3e303b3b3d6e3f383b3c3b3d3b3d3f3f3b383b3a3e3c3d6e3b383b3a3d6e3b303b3a3b3b3b3c3e6a3a383b3f3e303b3b3d6e3f383b3a3b383b313b3a3b3c3e6c3f6c")]]]]))).decode())
else:
    print("Incorrect !")
    exit(1)
