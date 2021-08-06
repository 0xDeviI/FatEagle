class AlphaHashV1:    
    _totalAsciiSum = 0
    def totalAsciiSum(self,input):
        tot = 0
        for i in range(0, len(input)):
            tot += (ord(input[i]) % 12)
        return tot


    def Alphicage(self,input):
        # Alpha Number System
        a = 5
        A = 10
        b = 15
        B = 20
        c = 25
        C = 30
        d = 35
        D = 40
        e = 45
        E = 50
        f = 55
        F = 60

        CentralizedTo64 = [None] * len(input)

        for i in range(0, len(input)):
            CentralizedTo64[i] = (ord(input[i]) + i + (self._totalAsciiSum % 12)) % 64

        R_ID = ""

        for i in range(0, len(input)):
            # // input length is equals to CentralizedTo64 length
            if (CentralizedTo64[i] <= 0):
                R_ID += "0"
            elif (CentralizedTo64[i] < a):
                R_ID += str(CentralizedTo64[i])
            elif (CentralizedTo64[i] - a < 10):
                if (CentralizedTo64[i] - a == 0):
                    R_ID += "a"
                else:
                    R_ID += "a" + str(CentralizedTo64[i] - a)
            elif (CentralizedTo64[i] - A < 10):
                if (CentralizedTo64[i] - A == 0):
                    R_ID += "A"
                else:
                    R_ID += "A" + str(CentralizedTo64[i] - A)
            elif (CentralizedTo64[i] - b < 10):
                if (CentralizedTo64[i] - b == 0):
                    R_ID += "b"
                else:
                    R_ID += "b" + str(CentralizedTo64[i] - b)
            elif (CentralizedTo64[i] - B < 10):
                if (CentralizedTo64[i] - B == 0):
                    R_ID += "B"
                else:
                    R_ID += "B" + str(CentralizedTo64[i] - B)
            elif (CentralizedTo64[i] - c < 10):
                if (CentralizedTo64[i] - c == 0):
                    R_ID += "c"
                else:
                    R_ID += "c" + str(CentralizedTo64[i] - c)
            elif (CentralizedTo64[i] - C < 10):
                if (CentralizedTo64[i] - C == 0):
                    R_ID += "C"
                else:
                    R_ID += "C" + str(CentralizedTo64[i] - C)
            elif (CentralizedTo64[i] - d < 10):
                if (CentralizedTo64[i] - d == 0):
                    R_ID += "d"
                else:
                    R_ID += "d" + str(CentralizedTo64[i] - d)
            elif (CentralizedTo64[i] - D < 10):
                if (CentralizedTo64[i] - D == 0):
                    R_ID += "D"
                else:
                    R_ID += "D" + str(CentralizedTo64[i] - D)
            elif (CentralizedTo64[i] - e < 10):
                if (CentralizedTo64[i] - e == 0):
                    R_ID += "e"
                else:
                    R_ID += "e" + str(CentralizedTo64[i] - e)
            elif (CentralizedTo64[i] - E < 10):
                if (CentralizedTo64[i] - E == 0):
                    R_ID += "E"
                else:
                    R_ID += "E" + str(CentralizedTo64[i] - E)
            elif (CentralizedTo64[i] - f < 10):
                if (CentralizedTo64[i] - f == 0):
                    R_ID += "f"
                else:
                    R_ID += "f" + str(CentralizedTo64[i] - f)
            elif (CentralizedTo64[i] - F < 10):
                if (CentralizedTo64[i] - F == 0):
                    R_ID += "F"
                else:
                    R_ID += "F" + str(CentralizedTo64[i] - F)
        return R_ID

    def _generate_alpha(self,input):
        # ver 2:
        self._totalAsciiSum = self.totalAsciiSum(input)
        __HASH = ""
        if (len(input) % 64 == 0):  __HASH = input + input[0]
        else:   __HASH = input
        #__HASH = len(input) % 64 == 0 if input + input[0] else input;
        while (len(__HASH) < ((len(__HASH) % 64) + 1) * 64):
            __HASH = self.Alphicage(__HASH)
        return __HASH[len(__HASH) - 64::]

    def Hash(self,input):
        return self._generate_alpha(input)