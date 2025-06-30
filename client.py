import threading
import socket
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import sys

# Server connection settings
host = 'localhost'
port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# === GUI SETUP ===
root = tk.Tk()
root.title("Chat Client")
root.geometry("600x450")
root.configure(bg="#1f1f2e")

# === CHAT DISPLAY AREA ===
chat_frame = tk.Frame(root, bg="#1f1f2e")
chat_frame.pack(fill='both', expand=True)

chat_area = scrolledtext.ScrolledText(
    chat_frame,
    state='disabled',
    bg="#2d2d44",
    fg="#f5f5f5",
    font=("Consolas", 11),
    wrap='word'
)
chat_area.pack(padx=10, pady=10, fill='both', expand=True)

# === INPUT FIELD FRAME ===
input_frame = tk.Frame(root, bg="#1f1f2e")
input_frame.pack(fill='x', padx=10, pady=(0, 10))

message_var = tk.StringVar()

message_entry = tk.Entry(
    input_frame,
    textvariable=message_var,
    font=("Helvetica", 11),
    bg="#f0f0f0",
    fg="#000000",
    relief=tk.FLAT,
    bd=3
)
message_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))

send_button = tk.Button(
    input_frame,
    text="Send",
    command=lambda: send_message(),
    bg="#34a853",
    fg="white",
    font=("Helvetica", 10, "bold"),
    padx=10,
    pady=5
)
send_button.pack(side='right')

# === MESSAGE FUNCTIONS ===
def send_message():
    msg = message_var.get().strip()
    if msg:
        client.send(msg.encode('utf-8'))
        if msg == '/exit':
            root.quit()
            client.close()
            sys.exit(0)
        message_var.set('')

message_entry.bind("<Return>", lambda event: send_message())

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break
            chat_area.config(state='normal')
            chat_area.insert('end', msg + '\n')
            chat_area.yview('end')
            chat_area.config(state='disabled')
        except:
            break

def on_closing():
    try:
        client.send('/exit'.encode('utf-8'))
    except:
        pass
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)

# === LOGIN PROMPT ===
name_prompt = client.recv(1024).decode('utf-8')
name = simpledialog.askstring("Name", name_prompt)
client.send(name.encode('utf-8'))

# === START RECEIVING THREAD ===
threading.Thread(target=receive_messages, daemon=True).start()

# === RUN GUI ===
root.mainloop()
