import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from fescripts.libs.feio import IPv4
from colorama import init
init()
from colorama import Fore,Back
import signal
from ipaddress import ip_network, ip_address
import socket, struct
from time import gmtime, strftime

class IPRS:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("IPRS","FeScript to scan range of ip address.","""this FeScript will scan givven range of IP Addresses and shows up addresses.""",{'start': {'Body': '', 'Description': 'start of IP range (165.26.53.0)', 'Require': True}, 'end': {'Body': '', 'Description': 'end of IP range (165.26.53.255)', 'Require': True}},"0xDeviI")
    _log_name = "fescripts/Network/IPScan/"
    InputManager = IPv4()

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

    def ips(self, start, end):
      start = struct.unpack('>I', socket.inet_aton(start))[0]
      end = struct.unpack('>I', socket.inet_aton(end))[0]
      return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]

    def isOpen(self, ip, port):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(2)
      try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        file=open(self._log_name, "a+")
        file.write(ip + "\n")
        print(Fore.GREEN + "[+] " + ip + Fore.RESET)
      except:
        print(Fore.RED + "[-] " + ip + Fore.RESET)
      finally:
        s.close()

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      startIP = self._fs._Opt["start"]["Body"]
      endIP = self._fs._Opt["end"]["Body"]
      ip_range = (startIP, endIP)
      allIPS = self.ips(*ip_range)
      self._log_name += "log-" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".txt"
      for i in allIPS:
        self.isOpen(i, "80")
      print("\nScan Finished. log saved in:\n    " + self._log_name)
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
      if (self.InputManager.isValidIPV4Addr(value)):
        self._fs._Opt[prop]["Body"] = value
        return None
      else:
        return [False, value + " is not a valid IPv4 Address!"]
