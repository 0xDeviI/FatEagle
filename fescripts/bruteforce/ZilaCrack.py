import os
import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import signal
import zipfile

class ZilaCrack:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("ZilaCrack","breakdown zip files using bruteforce (crack zip files pass)","""ZilaCrack is a FeScript to find zip files password using bruteforce attack. you just need a password list to start attack using ZilaCrack.""",{'file': {'Body': '', 'Description': 'path of where zip file exist', 'Require': True}, 'wordlist': {'Body': '', 'Description': 'path of where wordlist exist', 'Require': True}},"0xDeviI")
    
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
      if (os.path.exists(self._fs._Opt["file"]["Body"]) and os.path.exists(self._fs._Opt["wordlist"]["Body"])):
        if (zipfile.is_zipfile(self._fs._Opt["file"]["Body"]) == False):
          print(Fore.LIGHTRED_EX + "error: Bad zipfile!" + Fore.RESET)
        else:
          _zfile = zipfile.ZipFile(self._fs._Opt["file"]["Body"])
          _wl = open(self._fs._Opt["wordlist"]["Body"],"r",encoding="utf-8")
          for i in _wl.readlines():
            i = i.replace("\n","")
            try:
              _zfile.extractall(path="fescripts/temp/extracted/",pwd=bytes(i,"utf-8"))
              print(Fore.LIGHTGREEN_EX + "[+] Password Found: " + i + Fore.RESET)
              break
            except:
              print(Fore.LIGHTRED_EX + "[-]" + Fore.RESET + " Password: " + i)
          _wl.close()
      else:
        print(Fore.LIGHTRED_EX + "error: zipfile or wordlist not exist!" + Fore.RESET)
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
