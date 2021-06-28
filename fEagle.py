import os
import sys
import signal
import header
import commandParser as _command_parser
import fescriptManager
import socket as s
import json
import shutil
import time
from colorama import init
init()
from colorama import Fore,Back
from processManager import _process_mode,FE_PROCESS_MANAGER
from fescripts.libs.PFable import fable_mode,fable
from colorManager import *
from feConfig import *

_HEADER = header.FE_HEADER()
_COLOR_M = FE_COLOR()
_cp = _command_parser.FE_COMMAND_PARSE()
_fsc = fescriptManager.FE_SCRIPT_MANAGER()
_proc = FE_PROCESS_MANAGER()
_in_app = True
__FE_MULTI_FESCRIPT__ = []

def goodBye():
    print(Fore.LIGHTBLUE_EX + "\nGoodbye!" + Fore.RESET)
    sys.exit(0)

def signal_handler(sig, frame):
    goodBye()
signal.signal(signal.SIGINT, signal_handler)

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    _HEADER.printHeader()
    while (_in_app):
        try:
            command = input(Fore.RESET + "FatEagle ~> " if _fsc.loaded_script == "" else "FatEagle " + Fore.MAGENTA + "fescript" + Fore.RESET + "(" + Fore.YELLOW + _fsc.loaded_script + Fore.RESET + ") ~> ")
        except:
            goodBye()
        if (command.casefold() == "myIP".casefold()):
            print("Your IP adrress is :",Fore.LIGHTGREEN_EX + s.gethostbyname(s.gethostname()) + Fore.RESET)
        elif (command.casefold() == "myHost".casefold()):
            print("Your host name is :",Fore.LIGHTGREEN_EX + s.gethostname() + Fore.RESET)
        elif (os.name == "nt" and command == "cls"):
            clearConsole()
        elif (os.name != "nt" and command == "clear"):
            clearConsole()
        elif (command.casefold() == "banner".casefold()):
            _HEADER.printHeader()
        elif (_cp.isLoading(command) != False):
            f = _cp.isLoading(command)
            if (f["Type"] == "FESCRIPT"):
                _fsc.loadScript(f["Name"])
        elif (command.casefold() == "unload module"):
            if (_fsc.loaded_script != ""):  _fsc.unloadScript()
        elif (command.casefold() == "fesInfo".casefold()):
            if (_fsc.loaded_script != ""):
                try:
                    _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
                    eval("_main_module." + pathilize(_fsc.loaded_script) + "().info()")
                except:
                    print(Fore.LIGHTRED_EX + "fescript " + Fore.LIGHTBLUE_EX + pathilize(_fsc.loaded_script) + Fore.LIGHTRED_EX + " does not exist or may it has some errors" + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + "no module loaded." + Fore.RESET)
        elif (command.casefold() == "fesHelp".casefold()):
            if (_fsc.loaded_script != ""):
                try:
                    _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
                    eval("_main_module." + pathilize(_fsc.loaded_script) + "().help()")
                except:
                    print(Fore.LIGHTRED_EX + "fescript " + Fore.LIGHTBLUE_EX + pathilize(_fsc.loaded_script) + Fore.LIGHTRED_EX + " does not exist or may it has some errors" + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + "no module loaded." + Fore.RESET)
        elif (command.casefold() == "fesOptions".casefold()):
            if (_fsc.loaded_script != ""):
                try:
                    _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
                    eval("_main_module." + pathilize(_fsc.loaded_script) + "().switchInfo()")
                except:
                    print(Fore.LIGHTRED_EX + "fescript " + Fore.LIGHTBLUE_EX + pathilize(_fsc.loaded_script) + Fore.LIGHTRED_EX + " does not exist or may it has some errors" + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + "no module loaded." + Fore.RESET)
        elif (command.casefold() == "fesRequire".casefold()):
            if (_fsc.loaded_script != ""):
                try:
                    _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
                    eval("_main_module." + pathilize(_fsc.loaded_script) + "().missedSwitch()")
                except:
                    print(Fore.LIGHTRED_EX + "fescript " + Fore.LIGHTBLUE_EX + pathilize(_fsc.loaded_script) + Fore.LIGHTRED_EX + " does not exist or may it has some errors" + Fore.RESET)
            else:
                    print(Fore.LIGHTRED_EX + "no module loaded." + Fore.RESET)
        elif (_cp.IsSet(command) != False):
            setValue(command)
        elif (_cp.IsShow(command) != False):
            showValue(_cp.IsShow(command))
        elif (command.casefold() == "fesStart".casefold()):
            try:
                _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
                _proc.setPM(_process_mode.IN_SCRIPT)
                eval("_main_module." + pathilize(_fsc.loaded_script) + "()._pre_start()")
                _proc.setPM(_process_mode.FREE)
            except:
                print(Fore.LIGHTRED_EX + "fescript " + Fore.LIGHTBLUE_EX + pathilize(_fsc.loaded_script) + Fore.LIGHTRED_EX + " does not exist or may it has some errors" + Fore.RESET)
        elif (_cp.IsSearch(command) != False):
            _search = _cp.IsSearch(command)
            if (_search == "*"):  _search = "s"
            _file = open("ModulesDB.json","r",encoding="utf8")
            _modules = json.load(_file)
            cols = ["name","description"]
            data = []
            for _ in _modules:
                if (_search.casefold() in _["MODULE_FNAME"].casefold() or _search.casefold() in _["MODULE_INFO"].casefold()):
                    data.append([_["MODULE_FNAME"],_["MODULE_INFO"]])
            if (len(data) == 0):
                print(Fore.LIGHTRED_EX + "can't find any fescript named '" + Fore.CYAN + _search + Fore.LIGHTRED_EX + "'.\nif you added new fescript, you may need to update modules database using:" + Fore.YELLOW + "\n        update db" + Fore.RESET)
            else:
                _fable = fable(cols,data,fable_mode.BOLD_COLUMNS)
                print(_fable.popData())
        elif (command.casefold() == "update db".casefold()):
            updateModulesDB(True)
        elif (command.casefold() == "exit".casefold()):
            print(Fore.LIGHTBLUE_EX + "\nGoodbye!" + Fore.RESET)
            sys.exit(0)
        elif (_cp.IsAdd(command) != False):
            arged = _cp.IsAdd(command)
            __fes_dir = getListOfFiles("fescripts/")
            for i in range(0,len(__fes_dir)):
                __fes_dir[i] = __fes_dir[i].replace("fescripts/","")
            _fescript = arged[1]
            _list_name = arged[2]
            __all_vars = globals().keys()
            found = False
            for i in __all_vars:
                if (_list_name == i):
                    found = True
                    break
            if (found):
                found = False
                for i in __fes_dir:
                    if (_fescript == i):
                        found = True
                        break
                if (found):
                    if (_fescript not in eval(_list_name)):
                        eval(_list_name + ".append(\"" + _fescript + "\")")
                else:
                    print(Fore.LIGHTRED_EX + "fescript '" + Fore.LIGHTBLUE_EX + _fescript + Fore.LIGHTRED_EX + "' is Undefined!" + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + "list '" + Fore.LIGHTBLUE_EX + _list_name + Fore.LIGHTRED_EX + "' is Undefined!" + Fore.RESET)
            del __all_vars
            del __fes_dir
        elif (_cp.IsShowList(command) != False):
            _list_name = _cp.IsShowList(command)
            __all_vars = globals().keys()
            found = False
            for i in __all_vars:
                if (_list_name == i):
                    found = True
                    break
            if (found):
                eval("print(" + str(_list_name) + ")")
            else:
                print(Fore.LIGHTRED_EX + "list '" + Fore.LIGHTBLUE_EX + _list_name + Fore.LIGHTRED_EX + "' is Undefined!" + Fore.RESET)
            del __all_vars
        elif (command.casefold() == "deltemp".casefold()):
            clearModuleTemp(True)
        elif (command.casefold() == "info __FE_MULTI_FESCRIPT__".casefold()):
            for i in __FE_MULTI_FESCRIPT__:
                print(i + " : ")
                _main_module = locals()[pathilize(i)] = __import__("fescripts." + i.replace("/","."),fromlist=['object'])
                _ = eval("_main_module." + pathilize(i) + "().switchInfo()")
                del _main_module
        elif (command.casefold() == "start __FE_MULTI_FESCRIPT__".casefold()):
            for i in __FE_MULTI_FESCRIPT__:
                print(i + " : ")
                _main_module = locals()[pathilize(i)] = __import__("fescripts." + i.replace("/","."),fromlist=['object'])
                _proc.setPM(_process_mode.IN_SCRIPT)
                _ = eval("_main_module." + pathilize(i) + "()._pre_start()")
                del _main_module
                _proc.setPM(_process_mode.FREE)
        elif (_cp.IsMultiFesSet(command) != False):
            arged = _cp.IsMultiFesSet(command)
            _s_name = arged[1]
            _s_val = arged[2]
            _fes_name = arged[3]
            _fsc.loadScript(_fes_name)
            setValue("set " + _s_name + " " + _s_val)
        elif (command.casefold() == "version".casefold()):
            print(_COLOR_M.colorful_str("Fat Eagle V" + VERSION_))
        elif (command.casefold() == "fwi".casefold()):
            print(Fore.YELLOW + "Fat Eagle is a hacking and cybersecurity framework written in python by " + DEVELOPER + """ 
you can easily run it everywhere like windows,linux,mac,android and everywehere python can run. with this framework you can access to top security tools like exploits,payloads,hash crackers,phishing tools and e.t.c.""" + Fore.RESET)
        else:
            print(Fore.LIGHTCYAN_EX + command + Fore.LIGHTRED_EX + " is not a valid command." + Fore.RESET)

def showValue(switch):
    if (_fsc.loaded_script != ""):
        found = False

        _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
        props = eval("_main_module." + pathilize(_fsc.loaded_script) + "().allSwitches()")
        del _main_module
        for i in props:
            if (switch in i):
                _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
                eval("_main_module." + pathilize(_fsc.loaded_script) + "().showSwitch(\"" + switch + "\")")
                found = True
                del _main_module
                break
        if (found == False):
            print(Fore.LIGHTRED_EX + "switch " + Fore.LIGHTBLUE_EX + switch + Fore.LIGHTRED_EX + " does not exist!" + Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX + "no module loaded." + Fore.RESET)

def setValue(command):
    if (_fsc.loaded_script != ""):
        other = command[4:len(command)].split()
        found = False

        _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
        props = eval("_main_module." + pathilize(_fsc.loaded_script) + "().allSwitches()")
        del _main_module
        for i in props:
            if (other[0] == i):
                _main_module = locals()[_fsc.loaded_script] = __import__(_fsc.loaded_script.replace("/","."),fromlist=['object'])
                eval("_main_module." + pathilize(_fsc.loaded_script) + "().setSwitch(\"" + other[0] + "\",\"" + other[1] + "\")")
                print(Fore.LIGHTBLUE_EX + other[0] + Fore.RESET + " ---> " + Fore.LIGHTGREEN_EX + other[1] + Fore.RESET)
                found = True
                del _main_module
                break
        if (found == False):
            print(Fore.LIGHTRED_EX + "switch " + Fore.LIGHTBLUE_EX + other[0] + Fore.LIGHTRED_EX + " does not exist!" + Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX + "no module loaded." + Fore.RESET)

def pathilize(_str):
    last = ""
    for i in _str[::-1]:
        if (i == '/'):
            break
        else:
            last += i
    return last[::-1]

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            path = fullPath.replace("\\","/")
            if (path[len(path) - 3:len(path)] == ".py" and "libs" not in path and "temp" not in path):
                allFiles.append(path[0:len(path) - 3])
                
    return allFiles

def updateModulesDB(userRequest = False):
    FeScripts = getListOfFiles("fescripts/")
    data = []
    for _ in FeScripts:
        if ('s' in _):
            _main_module = locals()[_] = __import__(_.replace("/","."),fromlist=['object'])
            info = eval("_main_module." + pathilize(_) + "()._info()")
            data.append({"MODULE_FNAME":_,"MODULE_INFO":info.replace("\n", "")})
            del _main_module
    _file = open("ModulesDB.json","w",encoding="utf8")
    json.dump(data,_file,indent=4, sort_keys=True)
    _file.close()
    if (userRequest):   print(Fore.GREEN + "Modules Database Updated!" + Fore.RESET)

def clearModuleTemp(userRequest = False):
    folder = 'fescripts/temp/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(Fore.RED + ('Failed to delete %s. Reason: %s' % (file_path, e)) + Fore.RESET)
        if (userRequest):   print(Fore.GREEN + "Modules Temp Cleared!" + Fore.RESET)

if (__name__ == "__main__"):
    msg = 'Loading Fat Eagle ...'
    clearConsole()
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(2)
    for _ in range(len(msg)):
        time.sleep(0.1)
        sys.stdout.write('\033[D \033[D')
        sys.stdout.flush()
    if (MODULE_DB_UPDATE_ON_START): updateModulesDB()
    if (CLEAR_MODULE_TEMPS_ON_START):   clearModuleTemp()
    main()