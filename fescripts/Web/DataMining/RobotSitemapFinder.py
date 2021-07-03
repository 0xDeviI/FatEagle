import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import requests
import signal

class RobotSitemapFinder:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("RobotSitemapFinder","a FeScript to find websites robots.txt or sitemap.xml","""a FeScript to find websites robots.txt or sitemap.xml Coded By 0xDeviI.\nto use this FeScript load it , set requirements , and START !""",{'SITE_ADDR': {'Body': '', 'Description': 'address of target website (without protocol).', 'Require': True}},"0xDeviI")
    
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
      _site_addr = self._fs._Opt["SITE_ADDR"]["Body"]
      _urls = ["https://" + _site_addr.replace("/","") + "/robots.txt",
      "https://" + _site_addr.replace("/","") + "/robots.txt.gz",
      "https://" + _site_addr.replace("/","") + "/sitemap.xml",
      "https://" + _site_addr.replace("/","") + "/sitemap.xml.gz",
      "https://" + _site_addr.replace("/","") + "/sitemap.ashx",
      "https://" + _site_addr.replace("/","") + "/sitemap.ashx.gz"
      ]
      for i in _urls:
        try:
          r = requests.get(i)
          if (r.status_code < 400):
            print(Fore.GREEN + "[+] " + str(r.status_code) + " " + i + Fore.RESET)
          else:
            print(Fore.RED + "[-] " + str(r.status_code) + " " + i + Fore.RESET)
        except requests.exceptions.RequestException:
          print(Fore.LIGHTRED_EX + "[!] " + i + "  ---> HTTP_REQUEST_ERROR" + Fore.RESET)
      
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
