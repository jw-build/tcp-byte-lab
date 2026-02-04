import socket
import time

HOST = "127.0.0.1"
PORT = 9000

payload = b"\x01\x02hello\xff"

print(f"[client] payload raw: {payload}")
print(f"[client] payload hex: {payload.hex()}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# 故意拆成两次 send
sock.send(payload[:3])      # \x01 \x02 h
time.sleep(0.5)
sock.send(payload[3:])      # ello \xff

print("[client] done sending")
sock.close()
