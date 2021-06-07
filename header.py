import random
import colorManager as cm

class FE_HEADER:
    _cm = cm.FE_COLOR()
    headers = [{"Header":"","Body":"""           .---.        .-----------
      /     \  __  /    ------
     / /     \(  )/    -----
    //////   ' \/ `   ---
   //// / // :    : ---
  // /   /  /`    '--
 //          //..\\
        ====UU====UU====
            '//||\\`
              ''``""","Footer":"          Fat Eagle , a hacking framework by 0xDeviI"}]
    def printHeader(self):
        _ = random.randint(0,len(self.headers) - 1)
        print(self._cm.colorize_str(self.headers[_]["Header"] + "\n") +
        self._cm.colorize_str(self.headers[_]["Body"] + "\n") +
        self._cm.colorize_str(self.headers[_]["Footer"] + "\n") + self._cm.resetColor())