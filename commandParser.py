from fescripts.libs.PFable import fable


class FE_COMMAND_PARSE:
    def isLoading(self,comm):
        d = comm.split()
        if (len(d) == 2 and d[0].casefold() == "load".casefold()):
            if d[1][0:10] == "fescripts/":
                return {"Type":"FESCRIPT","Name":d[1]}
            else:
                return False
        return False
    def IsSet(self,comm):
        if (comm[0:4].casefold() == "set ".casefold()):
            return True
        else:
            return False
    def IsShow(self,comm):
        d = comm.split()
        if (len(d) == 2 and d[0].casefold() == "show".casefold()):
            return d[1]
        return False
    def IsSearch(self,comm):
        if (len(comm.split()) == 2 and comm.split()[0].casefold() == "search".casefold()):
            return comm.split()[1]
        else:
            return False
    def IsAdd(self,comm):
        arged = comm.split()
        if (arged[0].casefold() == "add".casefold()):
            return arged
        else:
            return False
    def IsShowList(self,comm):
        if (comm[0:10].casefold() == "show list ".casefold()):
            return comm[10:len(comm)]
        else:
            return False
    def IsMultiFesSet(self,comm):# set IP 127.0.0.1 Osint/WhoIsWho
        arged = comm.split()
        if (arged[0].casefold() == "mset".casefold()):
            return arged
        else:
            return False
    def isFuncCall(self,comm):
        splited = comm.split()
        if (splited[0].casefold() == "call".casefold() and len(splited) >= 2):
            _funName = splited[1]
            _args = []
            for i in range(2,len(splited)):
                _args.append(splited[i])
            return [_funName,_args]
        else:
            return False
    def isExec(self,comm):
        splited = comm.split()
        if (splited[0].casefold() == "exec".casefold() and len(splited) >= 2):
            _shell = ""
            for i in range(1,len(splited)):
                _shell += splited[i] + " "
            _shell = _shell[0:len(_shell) - 1]
            return _shell
        else:
            return False
    def isFunSearch(self,comm):
        if (len(comm.split()) == 2 and comm.split()[0].casefold() == "funsearch".casefold()):
            return comm.split()[1]
        else:
            return False