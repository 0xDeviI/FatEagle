from os import fstat
import random
from colorama import init
init()
from colorama import Fore,Back

class FE_COLOR:
    def resetColor(self):
        return Fore.RESET
    def colorful_str(self,_str):
        fstr = ""
        for i in _str:
            fstr += self.colorize_str(i)
        return fstr
    def colorize_str(self,_str):
        _ = random.randint(0,11)
        if (_ == 0):
            return Fore.RED + _str
        elif (_ == 1):
            return Fore.GREEN + _str
        elif (_ == 2):
            return Fore.YELLOW + _str
        elif (_ == 3):
            return Fore.BLUE + _str
        elif (_ == 4):
            return Fore.MAGENTA + _str
        elif (_ == 5):
            return Fore.CYAN + _str
        elif (_ == 6):
            return Fore.LIGHTRED_EX + _str
        elif (_ == 7):
            return Fore.LIGHTGREEN_EX + _str
        elif (_ == 8):
            return Fore.LIGHTYELLOW_EX + _str
        elif (_ == 9):
            return Fore.LIGHTBLUE_EX + _str
        elif (_ == 10):
            return Fore.LIGHTMAGENTA_EX + _str
        elif (_ == 11):
            return Fore.LIGHTCYAN_EX + _str
        