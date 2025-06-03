import socket

HOST = '127.0.0.1'  # Replace with server IP
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"[+] Connected to {HOST}:{PORT}")

try:
    while True:
        command = input("RemoteShell> ")
        if command.lower() in ('exit', 'quit'):
            client.send(command.encode())
            break

        client.send(command.encode())
        output = client.recv(4096).decode()
        print(output)

finally:
    client.close()
