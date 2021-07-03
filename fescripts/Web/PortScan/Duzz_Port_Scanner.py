import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import socket,threading
import signal

class Duzz_Port_Scanner:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("Duzz_Port_Scanner","a port scanner FeScript",
    """
    a port scanner FeScript coded by 0xDeviI.
    to use fescript load it and then set
    requirement and BOBM , fesStart !!!""",
    {'IP': {'Body': '', 'Description': 'ip address to check port status', 'Require': True},
    'SC_ALL':{'Body': '', 'Description': 'True for scan top 1000 ports and false for not scan all', 'Require': False},
    'PORT':{'Body': '8080', 'Description': 'specific port to scan (SC_ALL should be False)', 'Require': True}},"0xDeviI")
    
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


    def TCP_connect(self,ip, port_number, delay, output):
      TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      TCPsock.settimeout(delay)
      try:
          TCPsock.connect((ip, port_number))
          output[port_number] = 'Listening'
      except:
          output[port_number] = ''

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      _SC_ALL = self._fs._Opt["SC_ALL"]["Body"]
      _ip = self._fs._Opt["IP"]["Body"]
      _port = self._fs._Opt["PORT"]["Body"]
      
      if (_SC_ALL == "True"):
        _FILE = open("fescripts/Web/PortScan/_top_1000_port.list","r")
        _LINES = _FILE.readlines()
        threads = []
        output = {}
        for i in _LINES:
            i = i.replace("\n","")
            t = threading.Thread(target=self.TCP_connect, args=(_ip, int(i), 5, output))
            threads.append(t)
        for i in threads:
            i.start()
        for i in threads:
            i.join()
        keys = output.keys()
        for i in keys:
            if (output[i] == 'Listening'):
              print(Fore.LIGHTGREEN_EX + "[+] " + _ip + ":" + str(i) + " is open!" + Fore.RESET)
        _FILE.close()
      else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((_ip,int(_port)))
        if (result == 0):
          print(Fore.LIGHTGREEN_EX + "[+] " + _ip + ":" + str(_port) + " is open!" + Fore.RESET)
        else:
          print(Fore.LIGHTRED_EX + "[!] " + _ip + ":" + str(_port) + " is closed!" + Fore.RESET)
        sock.close()
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