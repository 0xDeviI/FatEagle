class FE_COMMAND_PARSE:
    def isLoading(self,comm):
        if (comm[0:14].casefold() == "load fescript ".casefold()):
            return comm[14:len(comm)]
        else:
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
        if (comm[0:7].casefold() == "search ".casefold()):
            return comm[7:len(comm)]
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