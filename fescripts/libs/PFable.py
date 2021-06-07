from enum import Enum
class fable_mode(Enum):
    SLICED = "sliced"
    BOLD_COLUMNS = "boldColumns"
class fable:
    v = ""
    def __init__(self,colNames,data,f_mode):
        error = False
        for i in data:
            if (len(i) != len(colNames)):
                error = True
                break
        if (error):
            print("Data Error <::> len error")    
        else:
            if (f_mode == fable_mode.SLICED):
                data.insert(0,colNames)
                self.v += self.drawRowLine(colNames,data)
                for i in data:
                    for c in range(0,len(i)):
                        if (c < len(i) - 1):
                            if (len(i[c]) < self.getBiggestStringArrayLength(data,c)):
                                self.v += "| " + self.dataSpaceAdder(i[c],self.getBiggestStringArrayLength(data,c)) + " "
                            else:
                                self.v += "| " + i[c] + " "
                        else:
                            if (len(i[c]) < self.getBiggestStringArrayLength(data,c)):
                                self.v += "| " + self.dataSpaceAdder(i[c],self.getBiggestStringArrayLength(data,c)) + " |\n" + self.drawRowLine(colNames,data)
                            else:
                                self.v += "| " + i[c] + " |\n" + self.drawRowLine(colNames,data)
            elif (f_mode == fable_mode.BOLD_COLUMNS):
                data.insert(0,colNames)
                self.v += self.drawRowLine(colNames,data)
                for i in data:
                    for c in range(0,len(i)):
                        if (c < len(i) - 1):
                            if (len(i[c]) < self.getBiggestStringArrayLength(data,c)):
                                self.v += "| " + self.dataSpaceAdder(i[c],self.getBiggestStringArrayLength(data,c)) + " "
                            else:
                                self.v += "| " + i[c] + " "
                        else:
                            if (data[0] == i):
                                if (len(i[c]) < self.getBiggestStringArrayLength(data,c)):
                                    self.v += "| " + self.dataSpaceAdder(i[c],self.getBiggestStringArrayLength(data,c)) + " |\n" + self.drawRowLine(colNames,data)
                                else:
                                    self.v += "| " + i[c] + " |\n" + self.drawRowLine(colNames,data)                          
                            else:
                                if (len(i[c]) < self.getBiggestStringArrayLength(data,c)):
                                    self.v += "| " + self.dataSpaceAdder(i[c],self.getBiggestStringArrayLength(data,c)) + " |\n"
                                else:
                                    self.v += "| " + i[c] + " |\n"
    def getBiggestStringArrayLength(self,data,index):
        big = 0
        for i in range(0,len(data)):
            for c in range(0,len(data[i])):
                if (c == index):
                    if (len(data[i][c]) >= big):
                        big = len(data[i][c])
        return big
    def drawRowLine(self,colNames,data):
        v = ""
        blens = [0] * len(colNames)
        for i in range(0,len(data)):
            for c in range(0,len(data[i])):
                if (len(data[i][c]) >= blens[c]):
                    blens[c] = len(data[i][c])
        maxLen = 0
        for i in blens:
            maxLen += i
        maxLen += (len(colNames) + 1) + (len(colNames) * 2)
        for i in range(0,maxLen):
            if (i < maxLen - 1):
                v += "-"
            else:
                v += "-\n"
        return v
    def popData(self):
        return self.v
    def dataSpaceAdder(self,data,spaces):
        for i in range(spaces - len(data)):
            data += " "
        return data