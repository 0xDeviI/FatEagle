import os
import sys
import signal
#from shutil import copyfile
from colorama import init
init()
from colorama import Fore,Back

def signal_handler(sig, frame):
    print(Fore.LIGHTBLUE_EX + "\nGoodbye!" + Fore.RESET)
    sys.exit(0)

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    ans = input("enter FeScript group Path: ")
    gpath = ans
    if (gpath[0:4] == "libs" or gpath[0:4] == "temp"):
        print(Fore.RED + "can't use reserved directories like libs,temp or e.t.c..")
        exit()
    if (os.path.exists("fescripts/" + ans) == False):   os.makedirs("fescripts/" + ans)
    _FeScript = {}
    ans = input("enter FeScript name: ")
    _FeScript["name"] = ans
    ans = input("enter FeScript mini info: ")
    _FeScript["mini_info"] = ans
    ans = input("enter FeScript long info: ")
    _FeScript["long_info"] = ans
    opt = {}
    _name = ""
    _def_val = ""
    _desc = ""
    _req = False
    while (ans != "done"):
        _name = input("enter FeScript switch name: ")
        _def_val = input("enter FeScript switch default value: ")
        _desc = input("enter FeScript switch info: ")
        _req = input("is FeScript switch required ? (Yes/No): ")
        _req = True if _req == "Yes" else   False
        opt[_name] = {"Body":_def_val,"Description":_desc,"Require":_req}
        ans = input("add other switch or done ? (add/done)")
    _FeScript["options"] = str(opt)
    ans = input("enter FeScript author: ")
    _FeScript["author"] = ans
#    #copyfile("templates/script_struct.py","fescripts/" + _FeScript["name"] + ".py")
    _FILE = open("templates/script_struct.py", "r")
    _arr = _FILE.readlines()
    x = ""
    for i in _arr:
        i = i.replace("\n", "")
        x += i + "\n"
    _FILE.close()
    x = x.replace("FESC_NAME", _FeScript["name"])
    x = x.replace("{{FESCRIPT_NAME}}", _FeScript["name"])
    x = x.replace("{{MINI_INFO}}", _FeScript["mini_info"])
    x = x.replace("{{LONG_INFO}}", _FeScript["long_info"])
    x = x.replace("OPTIONS", _FeScript["options"])
    x = x.replace("{{AUTHOR}}", _FeScript["author"])
    _FILE = open("fescripts/" + gpath + _FeScript["name"] + ".py","w")
    _FILE.write(x)
    _FILE.close()
    print(Fore.LIGHTGREEN_EX + "Fescritp '" + Fore.LIGHTYELLOW_EX + _FeScript["name"] + Fore.LIGHTGREEN_EX + "' Successfully Created!" + Fore.RESET)

if (__name__ == "__main__"):
    signal.signal(signal.SIGINT, signal_handler)
    clearConsole()
    main()