class FE_SCRIPTS:
    _fesname = ""
    _miniDesc = ""
    _totalDesc = ""
    _Opt = {}
    _author = ""
    def __init__(self, fesname,miniDesc,totalDesc,Opt,author):
        self._fesname = fesname
        self._miniDesc = miniDesc
        self._totalDesc = totalDesc
        self._Opt = Opt
        self._author = author