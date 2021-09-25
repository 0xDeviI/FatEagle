"""Fat Eagle Input/Output

    Type Check
    -----
           check for specific data types in both input and output.

    Type Compare
    --------
           compare and validate specific data types in both input and output.

"""

class IPv4:
    def __init__(self) -> None:
        pass

    def isValidIPV4Addr(self, ip):
        octets = ip.split(".")
        if (len(octets) != 4):
            return False
        for i in octets:
            if (int(i) >= 0x100):
                return False
        return True


    def convert_ipv4(self, ip):
        return tuple(int(n) for n in ip.split('.'))

    def check_ipv4_in(self, addr, start, end):
        return self.convert_ipv4(start) < self.convert_ipv4(addr) < self.convert_ipv4(end)
