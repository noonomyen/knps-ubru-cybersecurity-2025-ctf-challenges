def decode(ciphertext: str, key: str):
    plaintext: list[str] = []
    key = bytes.fromhex(key).decode().lower()
    key_length = len(key)
    i = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if char.islower():
                plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            i += 1
        else:
            plaintext.append(char)
    return "".join(plaintext)

def encode(plaintext: str, key: str):
    ciphertext: list[str] = []
    key = bytes.fromhex(key).decode().lower()
    key_length = len(key)
    i = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if char.islower():
                ciphertext.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                ciphertext.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            i += 1
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

key = "4b4559"

print(encode("????", key))
# zvmq{NkU5d0f2K9N2mItQwA91ZCza}
