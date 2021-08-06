from enum import Enum
class _process_mode(Enum):
    FREE = 1
    IN_SCRIPT = 2
class FE_PROCESS_MANAGER:
    _pm = _process_mode.FREE
    def __init__(self):
      pass
    def setPM(self,pm):
        if (pm == _process_mode.FREE):
            self._pm = _process_mode.FREE
        elif (pm == _process_mode.IN_SCRIPT):
            self._pm = _process_mode.IN_SCRIPT