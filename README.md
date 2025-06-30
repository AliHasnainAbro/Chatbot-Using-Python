Simple Chat Application
This is a basic command-line chat application built with Python's socket and threading modules. It features a server and a GUI client, allowing users to connect, send messages, and communicate with each other.

Features
GUI Client: User-friendly graphical interface for chatting.

Private Messaging: Send direct messages to specific online users using @username <message>.

List Online Users: View a list of currently connected users with the /list command.

Chat History: Each user's chat history is saved to a separate text file (<username>_history.txt) on the server side.

Server-Side Confirmation: The server echoes back the message sent by the client.

Exit Command: Gracefully disconnect from the server using the /exit command.

How to Run
Prerequisites
Python 3.x installed on your system.

Server Setup
Save the server code as server.py (or server12.py as per your provided file name).

Open a terminal or command prompt.

Navigate to the directory where you saved server.py.

Run the server using the command:

python server.py

You should see the message "Server running on 0.0.0.0:5555".

Client Setup
Save the client code as client.py.

Open a new terminal or command prompt.

Navigate to the directory where you saved client.py.

Run the client using the command:

python client.py

A GUI window will appear, prompting you to enter your name.

Usage
Connecting: When you run client.py, you will be prompted to enter a username. Enter your desired name to connect to the chat.

Sending Messages: Type your message in the input field at the bottom of the client window and press Enter or click the "Send" button.

Private Messages: To send a private message to another user, type @username Your message here (e.g., @Alice Hello Alice!).

List Users: To see who is currently online, type /list in the input field and press Enter.

Exiting: To disconnect from the chat, type /exit in the input field and press Enter, or simply close the client window.

Code Structure
server.py: Handles client connections, message routing, private messaging, and chat history saving.

client.py: Provides the graphical user interface for users to interact with the chat server.

Technologies Used
Python 3

socket module for network communication

threading module for handling multiple clients concurrently

tkinter for the graphical user interface

Future Enhancements (Ideas for further development)
Add support for broadcasting messages to all connected users.

Implement a command for changing usernames.

Encrypt messages for enhanced security.

Add timestamps to chat messages.

Implement a persistent chat history that loads when a user reconnects.

Allow file sharing between clients.

Improve error handling and user feedback.
