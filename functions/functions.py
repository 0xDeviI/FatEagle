import binascii
from fescripts.libs.blake2s import Blake2
from fescripts.libs.blake import Blake
from fescripts.libs.md2 import MD2
import shutil
from colorama import init
init()
from colorama import Fore,Back
import random
from faker import Faker
import os
from shutil import copyfile
import hashlib
import fescripts.libs.ripemd128 as ripe128
from fescripts.libs.alphaHash import *
import json
from fescripts.libs.PFable import fable_mode,fable

class FUNCTIONS:
    def __init__(self):
        pass

    def randomPass(self,chars,_length):
        return ''.join(random.choice(chars) for _ in range(int(_length)))

    def randomMacAddr(self):
        return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    def randomIPv4(self):
        return Faker().ipv4()

    def randomIPv6(self):
        return Faker().ipv6()

    def generateRHL(self,ip="0.0.0.0",port=6666,buffer_size=2e5,_os="windows",path=""):
        if (os.path.exists(path)):
            _FILE = open("functions/_ReverseHell/rhcp.py","r")
            _RHCPC = _FILE.read()
            _FILE.close()
            _FILE = open("functions/_ReverseHell/rh.py","w")
            _FILE.write(_RHCPC)
            _FILE.close()
            _RHCPC = _RHCPC.replace("{IP}",'"' + ip + '"')
            _RHCPC = _RHCPC.replace("{PORT}",str(port))
            _RHCPC = _RHCPC.replace("{BUFFER_SZIE}",str(buffer_size))
            _FILE = open("functions/_ReverseHell/rh.py","w")
            _FILE.write(_RHCPC)
            _FILE.close()
            if (_os == "windows"):
                os.system("pyinstaller --onefile -c -F functions/_ReverseHell/rh.py")
                copyfile("dist/rh.exe",path + "/rh.exe")
                shutil.rmtree("build/")
                shutil.rmtree("dist/")
                os.remove("rh.spec")
            elif (_os == "linux"):
                copyfile("functions/_ReverseHell/rh.py",path + "/rh.py")
                os.system("chmod +x " + path + "/rh.py")
            else:
                print(Fore.RED + "bad os type selected!" + Fore.RESET)
        else:
            print(Fore.RED + "path not exist!" + Fore.RESET)
        return ""

    def md5(self,message):
        return hashlib.new('md5', message.encode('utf-8')).hexdigest()

    def md4(self,message):
        return hashlib.new('md4', message.encode('utf-8')).hexdigest()

    def md2(self,message):
        return MD2().hash_digest(message.encode("utf-8"))
    
    def sha1(self,message):
        return hashlib.new('sha1', message.encode('utf-8')).hexdigest()

    def sha256(self,message):
        return hashlib.sha256(message.encode('utf-8')).hexdigest()

    def sha384(self,message):
        return hashlib.sha384(message.encode('utf-8')).hexdigest()

    def sha512(self,message):
        return hashlib.sha512(message.encode('utf-8')).hexdigest()

    def ripemd128(self,message):
        return ripe128.hexstr(ripe128.ripemd128(message.encode("utf8")))

    def ripemd160(self,message):
        return hashlib.new('ripemd160', message.encode('utf-8')).hexdigest()

    def blake224(self,message):
        return Blake(224).hash_digest(message.encode("utf-8"))

    def blake256(self,message):
        return Blake(256).hash_digest(message.encode("utf-8"))

    def blake384(self,message):
        return Blake(384).hash_digest(message.encode("utf-8"))

    def blake512(self,message):
        return Blake(512).hash_digest(message.encode("utf-8"))

    def blake2s224(self,message):
        return Blake2(224).hash_digest(message.encode("utf-8"))

    def blake2s256(self,message):
        return Blake2(256).hash_digest(message.encode("utf-8"))

    def blake2s384(self,message):
        return Blake2(384).hash_digest(message.encode("utf-8"))

    def blake2s512(self,message):
        return Blake2(512).hash_digest(message.encode("utf-8"))

    def ntlm(self,message):
        return binascii.hexlify(hashlib.new('md4', message.encode('utf-16le')).digest()).decode("utf-8")
    
    def alpha(self,message):
        ah = AlphaHashV1()
        return ah.Hash(message)

    def funHelp(self):
        funcs = {"randomPass":{"desc":"generates a random password with specific length","usage":"call randomPass [CHARS] [LENGTH]"},
        "randomPass":{"desc":"generates a random password with specific length","usage":"call randomPass [CHARS] [LENGTH]"},
        "randomMacAddr":{"desc":"generates a random mac address","usage":"call randomMacAddr"},
        "randomIPv4":{"desc":"generates a random randomIPv4","usage":"call randomIPv4"},
        "randomIPv6":{"desc":"generates a random randomIPv6","usage":"call randomIPv6"},
        "generateRHL":{"desc":"generates a ReverseHell FeScript Listener","usage":"call generateRHL [IP] [PORT] [BUFFER_SIZE] [OS_TYPE] [PATH]"},
        "md2":{"desc":"generates a md2 hash","usage":"call md2 [MESSAGE]"},
        "md4":{"desc":"generates a md4 hash","usage":"call md4 [MESSAGE]"},
        "md5":{"desc":"generates a md5 hash","usage":"call md5 [MESSAGE]"},
        "sha1":{"desc":"generates a sha1 hash","usage":"call sha1 [MESSAGE]"},
        "sha256":{"desc":"generates a sha256 hash","usage":"call sha256 [MESSAGE]"},
        "sha384":{"desc":"generates a sha384 hash","usage":"call sha384 [MESSAGE]"},
        "sha512":{"desc":"generates a sha512 hash","usage":"call sha512 [MESSAGE]"},
        "ripemd128":{"desc":"generates a ripemd128 hash","usage":"call ripemd128 [MESSAGE]"},
        "ripemd160":{"desc":"generates a ripemd160 hash","usage":"call ripemd160 [MESSAGE]"},
        "blake224":{"desc":"generates a blake224 hash","usage":"call blake224 [MESSAGE]"},
        "blake256":{"desc":"generates a blake256 hash","usage":"call blake256 [MESSAGE]"},
        "blake384":{"desc":"generates a blake384 hash","usage":"call blake384 [MESSAGE]"},
        "blake512":{"desc":"generates a blake512 hash","usage":"call blake512 [MESSAGE]"},
        "blake2s224":{"desc":"generates a blake2s224 hash","usage":"call blake2s224 [MESSAGE]"},
        "blake2s256":{"desc":"generates a blake2s256 hash","usage":"call blake2s256 [MESSAGE]"},
        "blake2s384":{"desc":"generates a blake2s384 hash","usage":"call blake2s384 [MESSAGE]"},
        "blake2s512":{"desc":"generates a blake2s512 hash","usage":"call blake2s512 [MESSAGE]"},
        "ntml":{"desc":"generates a ntml hash","usage":"call ntml [MESSAGE]"},
        "alpha":{"desc":"generates a alpha hash","usage":"call alpha [MESSAGE]"}
        }
        return funcs

    def searchFunc(self,_search):
        if (_search == "*"):  _search = "*"
        _file = open("FunctionsDB.json","r",encoding="utf8")
        _funcs = json.load(_file)
        cols = ["name","description","usage"]
        data = []
        for _ in _funcs:
            if (_search == "*"):
                data.append([_["FUNC_NAME"],_["FUNC_DESC"],_["FUNC_USAGE"]])
            else:
                if (_search.casefold() in _["FUNC_DESC"].casefold() 
                or _search.casefold() in _["FUNC_NAME"].casefold() 
                or _search.casefold() in _["FUNC_USAGE"].casefold()):
                    data.append([_["FUNC_NAME"],_["FUNC_DESC"],_["FUNC_USAGE"]])
        if (len(data) == 0):
            print(Fore.LIGHTRED_EX + "can't find any function named '" + Fore.CYAN + _search + Fore.LIGHTRED_EX + "'.\nif you added new function, you may need to update function database using:" + Fore.YELLOW + "\n        update fundb" + Fore.RESET)
        else:
            _fable = fable(cols,data,fable_mode.BOLD_COLUMNS)
            print(_fable.popData())

    def updateFunctionDB(self,userRequest=False):
        funs = self.funHelp()
        data = []
        for i in funs.keys():
            data.append({"FUNC_NAME":i,"FUNC_DESC":funs[i]["desc"],"FUNC_USAGE":funs[i]["usage"]})
        _file = open("FunctionsDB.json","w",encoding="utf8")
        json.dump(data,_file,indent=4, sort_keys=True)
        _file.close()
        if (userRequest):   print(Fore.GREEN + "Function Database Updated!" + Fore.RESET)

    def execute(self,script,opt):
        optStr = ""
        for i in opt:
            i = i.replace('"', "")
            if (isinstance(i,str)):
                optStr += '"' + str(i) + '"' + ","
            else:
                optStr += str(i) + ","
        optStr = optStr[0:len(optStr) - 1]
        try:
            print(eval(f"self.{script}({optStr})"))
        except:
            print(Fore.RED + f"Script {script} can't run.\nError: function not found or args not entered correctly." + Fore.RESET)