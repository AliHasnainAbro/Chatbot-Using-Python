import threading
import socket
import os

host = '0.0.0.0'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Server running on {host}:{port}")

clients = {}
lock = threading.Lock()

def save_history(name, message):
    with open(f"{name}_history.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def handle_client(client):
    try:
        client.send("Enter your name: ".encode())
        name = client.recv(1024).decode().strip()

        with lock:
            clients[name] = client

        client.send(f"👋 Hello {name}, you're now connected!\nCommands: /list, @user msg, /exit.".encode())

        while True:
            message = client.recv(1024)
            if not message:
                break
            decoded = message.decode().strip()

            if decoded == "/exit":
                client.send("Goodbye 👋".encode())
                break
            elif decoded == "/list":
                with lock:
                    users = ", ".join([u for u in clients if u != name])
                client.send(f"Users online: {users}".encode())
            elif decoded.startswith('@'):
                try:
                    parts = decoded.split(' ', 1)
                    target = parts[0][1:]
                    msg = parts[1]
                    if target in clients:
                        full = f"[PM] {name} -> {target}: {msg}"
                        clients[target].send(full.encode())
                        client.send(full.encode())
                        save_history(name, full)
                        save_history(target, full)
                    else:
                        client.send("❌ User not found.".encode())
                except:
                    client.send("⚠️ Use: @username message".encode())
            else:
                reply = f"[Server 🤖] {name}, you said: {decoded}"
                client.send(reply.encode())
                save_history(name, f"You: {decoded}")
                save_history(name, reply)
    finally:
        with lock:
            if name in clients:
                del clients[name]
        client.close()

def receive():
    while True:
        client, addr = server.accept()
        print(f"Connected from {addr}")
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

if __name__ == "__main__":
    receive()
