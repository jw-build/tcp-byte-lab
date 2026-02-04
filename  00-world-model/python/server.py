import socket

HOST = "127.0.0.1"
PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"[server] listening on {HOST}:{PORT}")

conn, addr = sock.accept()
print(f"[server] accepted connection from {addr}")

while True:
    data = conn.recv(4)  # 故意用小 buffer，暴露 TCP 行为
    if not data:
        print("[server] connection closed")
        break

    print(f"[server] recv {len(data)} bytes")
    print(f"[server] raw: {data}")
    print(f"[server] hex: {data.hex()}")

conn.close()
sock.close()
