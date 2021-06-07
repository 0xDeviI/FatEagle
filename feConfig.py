from enum import Enum

class MSM(Enum):
    # an enum for module search mode status
    USING_DB = 0
    USING_FILE_SEARCH = 1


MODULE_DB_UPDATE_ON_START = True
DEVELOPER = "0xDeviI"
VERSION = "1.0"
VERSION_NAME = "Alpha"
_VERSION = VERSION + ' ' + VERSION_NAME
