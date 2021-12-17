from data.Ch115.lib.archive import *


class Score():

    def __init__(self):
        self.arquivo = 'c:\ProtTech\data\data.txt'
        self.a = open(self.arquivo, 'at')
        self.a2 = open(self.arquivo, 'rt+')
        self.scr = 0
        self.count = 0

    def add_points(self):
        k = True
        self.a2 = open(self.arquivo, 'rt+')
        s = self.a2.readlines()[1]
        self.a2.close()
        a = open(self.arquivo, 'r')
        b = a.read()
        c = b
        try:
            if s[s.index("=")+2] == ";":
                num = s[s.index("=") + 1]
                c = c.replace(b[12], str(self.scr + int(num)))
                #z = z.replace(b[6], str(self.scr + int(num)))
            elif s[s.index("=") + 3] == ";":
                #for i in range(0, len(b)):
                 #    print(f'{i} : {b[i]}')
                num = s[s.index("=") + 1] + s[s.index("=") + 2]
                if (self.scr + int(num)) <= 100:
                    c = c.replace(c[12], "",1)
                    c = c.replace(c[12], str(self.scr + int(num)))
                elif self.scr + int(num) > 100 and self.scr + int(num) != 102:
                    c = c.replace(c[13], " ",)
                    c = c.replace(c[12], "",)
                    c = c.replace(" ", str(self.scr + int(num)), 1)
                    c = c.replace(" ", "", 1)
                elif self.scr + int(num) == 102:
                    c = c.replace(c[13], " ")
                    c = c.replace(" ", '102', 1)
                    c = c.replace(" ", "", 1)
                k = False
            elif s[s.index("=") + 4] == ";" and k:
                num = s[s.index("=") + 1] + s[s.index("=") + 2] + s[s.index("=") + 3]
                c = c.replace(c[14], " ",)
                c = c.replace(c[13], "", 1)
                c = c.replace(c[12], "",1)
                c = c.replace(" ", str(self.scr + int(num)), 1)
                c = c.replace(" ", "", 1)
                #print(c)
                #b = b.replace(b[12], str(self.scr + int(num)))
            #self.scr += int(num)
            #print(b)
            a = open(self.arquivo, 'w')
            a.write(c)
            a.close()
            b.close()

        except:
            i = True

    def alternatives(self, answ, feed):
        if answ == feed:
            if self.count == 0:
                self.scr += 3
                self.count = 0
            else:
                if self.count <= 2:
                    self.scr += 3 - self.count
        else:
            self.count += 1
        if answ == feed:
            self.add_points()
            return True
