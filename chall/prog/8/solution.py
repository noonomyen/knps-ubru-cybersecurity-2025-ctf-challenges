from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("127.0.0.1", 8011))

# Skip hello message
_ = sock.recv(1024)

while True:
    sock.send(b"find")
    data = sock.recv(1024).decode().strip()

    if data == "100":
        sock.send(b"catch")
        flag = sock.recv(1024).decode().strip()
        print(flag)
        break
