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
    print(bytes.fromhex("".join(map(chr, [i^0x63+int(pass_)*1 for i in [i^0xc4+int(pass_)*4 for i in [i^0x30+int(pass_)*2 for i in [i^0x93+int(pass_)*3 for i in bytes.fromhex("3f383f3a3e6e3e3f3f6a3f383f3e3b3f3c6b3d3e3c693e313c3e3b313d693e6c3c3f3e6b3f3f3d3d3f393c3c3c6b3e3c3b3e3b3a3c3a3d3a3e6b3f6c")]]]]))).decode())
else:
    print("Incorrect !")
    exit(1)
