import os
from colorama import init
init()
from colorama import Fore,Back

class FE_SCRIPT_MANAGER:
    loaded_script = ""
    def loadScript(self,scr_name):
        if (os.path.exists(scr_name + ".py")):
            self.loaded_script = scr_name
            print(Fore.LIGHTGREEN_EX + "module " + Fore.YELLOW + scr_name + Fore.LIGHTGREEN_EX + " successfully loaded!" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "module " + Fore.YELLOW + scr_name + Fore.LIGHTRED_EX + " not found!" + Fore.RESET)
    def unloadScript(self):
        print(Fore.LIGHTGREEN_EX + "module " + Fore.YELLOW + self.loaded_script + Fore.LIGHTGREEN_EX + " unloaded" + Fore.RESET)
        self.loaded_script = ""