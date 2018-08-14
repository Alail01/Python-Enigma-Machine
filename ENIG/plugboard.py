debug = False
'''
Class: Wire
    Purpose: to have concise ability to use a 'wire', where the first value is the start of the wire, and the second value is the other side of the wire.

    Function: init(inp,inp2)
        Input:  Char        inp         The start of the wire.
        Input:  Char        inp2        The end of the wire.

    Function: getStart()
        Purpose: To the get the start of the wire.
        Returns: Returns the first input of the wire (which I considered the start of the wire).

    Function: getEnd()
        Purpose: To the get the end of the wire.
        Returns: Returns the second input of the wire (which I considered the end of the wire).

    Function: change(inp)
        Purpose: To change the value from the start of the wire, to the end of the wire.
        Input:  Char        inp         The input, which is compared to the wires start and end value
        Returns: A character, which is either changed or not, depends on if it is part of the wire or not.

    Function: printself()
        Purpose: To print out both ends of the wire.
'''
class Wire:
    def __init__(self,inp,inp2):
        self.start = inp
        self.end = inp2

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def change(self,inp):
        if inp == self.start:
            out = self.end
        elif inp == self.end:
            out = self.start
        else:
            out = inp
        return out

    def printself(self):
        print("First input: "+self.start+ ",  Second input: "+ self.end)

'''
Class: Plugboard
    Purpose: To keep all the wires in a plugboard.

    Function: init(w,w1,w2,w3,w4,w5,w6,w7,w8,w9)
        *** Defaulted as nothing, so you don't have to have 10 wires ***
        Input:  Wire        w       The first wire, Defaulted as nothing.
        Input:  Wire        w1      The second wire, Defaulted as nothing.
        Input:  Wire        w2      The third wire, Defaulted as nothing.
        Input:  Wire        w3      The fourth wire, Defaulted as nothing.
        Input:  Wire        w4      The fifth wire, Defaulted as nothing.
        Input:  Wire        w5      The sixth wire, Defaulted as nothing.
        Input:  Wire        w6      The seventh wire, Defaulted as nothing.
        Input:  Wire        w7      The eighth wire, Defaulted as nothing.
        Input:  Wire        w8      The nineth wire, Defaulted as nothing.
        Input:  Wire        w9      The tenth wire, Defaulted as nothing.

    Function: change(inp)
        Purpose: To use the change function of the wire, so long as the wire exists.
        Input:  Char        inp         The character to be ran through the change function of the wires on this plugboard

    Function: printself()
        Purpose: To print out all the wires of this plugboard
'''
class Plugboard:
    def __init__(self,w = "",w1 = "",w2 = "",w3 = "",w4 = "",w5 = "",w6 = "",w7 = "",w8 = "",w9 = ""):
        i = 0
        self.length = 0
        self.wireList = []
        testList = [w,w1,w2,w3,w4,w5,w6,w7,w8,w9]
        while i < 10:
            if testList[i] != "":
                self.wireList.append(testList[i])
                self.length += 1
            i+=1

    def change(self, inp):
        i = 0
        out = inp
        limiter = 0
        while i < self.length and limiter == 0  :
            if inp == self.wireList[i].getStart():
                out = self.wireList[i].change(inp)
                limiter = 1
            elif inp == self.wireList[i].getEnd():
                out = self.wireList[i].change(inp)
                limiter = 1
            i+=1
            if debug: print(out)
        return out


    def printself(self):
        i = 0
        while i < self.length:
            self.wireList[i].printself()
            i+=1


def test():
    w = Wire('a','b')
    w.printself()
    w1 = Wire('c','d')
    w1.printself()
    w2 = Wire('e','f')
    w2.printself()
    w3 = Wire('g','h')
    w3.printself()
    print("")
    p = Plugboard(w,w1,w2,w3)
    p.printself()
    print("")

    test = "the quick brown fox jumped over the lazy dog"
    i = 0
    testL = list(test)

    while i < len(testL):
        testL[i] = p.change(testL[i])
        i+=1
    test = "".join(testL)
    print(test)

if __name__ == "__main__":
    debug = True
    test()
