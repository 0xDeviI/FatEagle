import sys
import threading
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import requests
import signal


class RetroDirScanner:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("RetroDirScanner","a FeScript to scan web direcotry.","""a FeScript to scan web direcotry coded by 0xDeviI.\n to use this FeScript load it , set requirements and START""",{'SITE_ADDR': {'Body': '', 'Description': 'address of website to scan directory (without protocol)', 'Require': True}, 'DIR_PATH': {'Body': 'fescripts/Web/Indexing/_directories.list', 'Description': 'path of list of directories', 'Require': True}},"0xDeviI")
    
    def __init__(self):
      pass
    
    def help(self):
        print(self._fs._totalDesc)
    
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

    def parsePage(self,url):
        req = requests.get(url)
        if (int(req.status_code / 100) == 2):
          print(Fore.LIGHTGREEN_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)
        elif (int(req.status_code / 100) == 3):
          print(Fore.LIGHTYELLOW_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)
        elif (int(req.status_code / 100) == 4 or int(req.status_code / 100) == 5):
          print(Fore.LIGHTRED_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)
        else:
          print(Fore.LIGHTCYAN_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      _site_addr = self._fs._Opt["SITE_ADDR"]["Body"]
      _dir_list = self._fs._Opt["DIR_PATH"]["Body"]
      directories = []
      for i in open(_dir_list,'r').readlines():
        directories.append(i.replace("\n",""))
      for directory in directories:
        url = "http://" + _site_addr + "/" + directory
        self.parsePage(url)
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
