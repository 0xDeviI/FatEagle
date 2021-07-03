from fescripts.libs.blake2s import Blake2
from fescripts.libs.blake import Blake
from fescripts.libs.md2 import MD2
import hashlib,binascii
import os
import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import signal
import fescripts.libs.ripemd128 as ripe128
from fescripts.libs.alphaHash import *

class Hash6:
    #config
    SHOW_NOT_FOUND_RES = True
    #config
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("Hash6","a FeScript to bruteforce Hashes","""a FeScript to bruteforce diffrent kind of hashes like md,sha,blake,ripemd and e.t.c...""",{'Hash': {'Body': '', 'Description': 'hash you want to brute force.', 'Require': True}, 'Wordlist': {'Body': '', 'Description': 'wordlist you have to brute force hash', 'Require': True}, 'Salt': {'Body': '', 'Description': 'hash salt if hash uses.', 'Require': False}},"0xDeviI")
    
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
      print("""
1) MD2
2) MD4
3) MD5
4) SHA1
5) SHA256
6) SHA384
7) SHA512
8) RIPEMD-128
9) RIPEMD-160
10) BLAKE-224
11) BLAKE-256
12) BLAKE-384
13) BLAKE-512
14) BLAKE2s-224
15) BLAKE2s-256
16) BLAKE2s-384
17) BLAKE2s-512
18) NTLM
19) ALPHA-1
      """)
      hashType = input("enter hash ID: ")
      if (os.path.exists(self._fs._Opt["Wordlist"]["Body"])):
        _file = open(self._fs._Opt["Wordlist"]["Body"],encoding="utf8")
        ah = AlphaHashV1()
        for i in list(_file.readlines()):
          i = i.replace("\n","")
          if (hashType == "1"):
            digest = MD2().hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "2"):
            digest = hashlib.new('md4', i.encode('utf-8')).hexdigest()
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "3"):
            digest = hashlib.new('md5', i.encode('utf-8')).hexdigest()
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "4"):
            digest = hashlib.new('sha1', i.encode('utf-8')).hexdigest()
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "5"):
            digest = hashlib.sha256(i.encode('utf-8')).hexdigest()
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "6"):
            digest = hashlib.sha384(i.encode('utf-8')).hexdigest()
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "7"):
            digest = hashlib.sha512(i.encode('utf-8')).hexdigest()
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "8"):
            digest = ripe128.hexstr(ripe128.ripemd128(i.encode("utf8")))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "9"):
            digest = hashlib.new('ripemd160', i.encode('utf-8')).hexdigest()
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "10"):
            digest = Blake(224).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "11"):
            digest = Blake(256).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "12"):
            digest = Blake(384).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "13"):
            digest = Blake(512).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "14"):
            digest = Blake2(224).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "15"):
            digest = Blake2(256).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "16"):
            digest = Blake2(384).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "17"):
            digest = Blake2(512).hash_digest(i.encode("utf-8"))
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "18"):
            digest = binascii.hexlify(hashlib.new('md4', i.encode('utf-16le')).digest()).decode("utf-8")
            if (digest.lower() == self._fs._Opt["Hash"]["Body"].lower()):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
          elif (hashType == "19"):
            digest = ah.Hash(i)
            if (digest == self._fs._Opt["Hash"]["Body"]):
              print(Fore.LIGHTGREEN_EX + "[+] " +  digest + " : " + i + Fore.RESET)
              break
            elif (self.SHOW_NOT_FOUND_RES):
              print(Fore.LIGHTRED_EX  + "[!] " + Fore.RESET + digest + " : " + i)
      else:
        print(Fore.LIGHTRED_EX + "wordlist not found!" + Fore.RESET)
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
