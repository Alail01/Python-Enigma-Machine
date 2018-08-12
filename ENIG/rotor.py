## Used conv.py to make these. See the rotor section in the readme for the letters.
rotor1 = [74, 71, 68, 81, 79, 88, 85, 83, 67, 65, 77, 73, 70, 82, 86, 84, 80, 78, 69, 87, 75, 66, 76, 90, 89, 72]
rotor2 = [78, 84, 90, 80, 83, 70, 66, 79, 75, 77, 87, 82, 67, 74, 68, 73, 86, 76, 65, 69, 89, 85, 88, 72, 71, 81]
rotor3 = [74, 86, 73, 85, 66, 72, 84, 67, 68, 89, 65, 75, 69, 81, 90, 80, 79, 83, 71, 88, 78, 82, 77, 87, 70, 76]
rotor4 = [81, 89, 72, 79, 71, 78, 69, 67, 86, 80, 85, 90, 84, 70, 68, 74, 65, 88, 87, 77, 75, 73, 83, 82, 66, 76]
rotor5 = [81, 87, 69, 82, 84, 90, 85, 73, 79, 65, 83, 68, 70, 71, 72, 74, 75, 80, 89, 88, 67, 86, 66, 78, 77, 76]

rotorList = [rotor1,rotor2,rotor3,rotor4,rotor5]

## Rotor of the basic abhabet, Used to start comparing.
rotorB = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
debug = False
'''
Class: Rotor
    Purpose: To make a object of a rotor, allowing the program to re-use functions that will help with the rotors.

    Function: init(Rot,Start)
        input: Rot      Is a Rotor List of the above ones (rotor1 - rotor5). Defaulted as rotor 1 from above
        input: Start    Starting position of the rotor. Defaulted as 0.

    Function: getRot()
        Purpose: To the get Rotor List that is used.
        Returns: Returns the Rotor List.

    Function: getPos()
        Purpose: To get the position value of the list.
        Returns: Returns the postion of the rotor, where the position is how many times the rotor has moved from the start position.

    Function: resetPos()
        Purpose: Resets the position value for the list. Used once the value hits 26.

    Function: start()
        Purpose: To initialize the rotor into the starting position, allowing for the rotor to not start on what the 'A' should be before moving.

    Function: rotate()
        Purpose: Rotates the list one value to the left and increases the position value.

    Function: changeChartoInt(inv)
        Purpose:  To change a character to an int, to be used for the list. Will be compared to the original abhabet, and then to this rotor. Only used in the first rotor.
        Input:      Character       inv        The input value into the function.
        Returns:    Int                        Output of the list.

    Function: changeInttoInt(inval,rotf)
        Purpose: To change the input of the last value, compare it to the list of the rotor last used, and then use it in this rotor.
        Input:      Int             inval       The input value for this rotor.
        Input:      List            rotf        The last list used.
        Returns:    Int                         The integer for the next rotor to use.

    Function: changeInttoChar(inval)
        Purpose: To change the value inputed into the rotor into a character that can be used for the next step in the machine.
        Input:      Int             inval       The input value to be changed into a character.
        Returns:    Char                        The character value of the input.

    Function: printself()
        Purpose: To print the list of the rotor.
'''
class Rotor:
    def __init__ (self, rot = rotorList[0],start = 0):
        self.startPos = start
        self.List = rot
        self.pos = -start

    def getRot(self):
        return self.List

    def getPos(self):
        return self.pos

    def resetPos(self):
        self.pos = 0

    def start(self):
        i = 0
        while i != self.startPos:
            self.rotate()
            i+=1

    def rotate(self):
        #if debug:print(self.rot)
        z = self.List.pop(0)
        self.List.append(z)
        self.pos+=1
        #if debug:print(self.rot)

    def changeChartoInt (self, inv):
        inval = ord(inv)
        inpos = rotorB.index(inval)
        outval = self.List[inpos]
        if debug:print(outval)
        return outval

    def changeInttoInt(self, inval,rotf):
        inpos = rotf.index(inval)
        outval = self.List[inpos]
        if debug:print(outval)
        return outval

    def changeInttoChar(self, inval):
        return char(inval)

    def printself(self):
        print(self.List)


'''
Class: RotorBlock

    Purpose: To make the three rotors into a single object that can be used.

    Function: init (r,r1,r2)
        Purpose: To initialize the rotor block for use.
        Input:      Rotor       r           Rotor that will be considered in the first position.
        Input:      Rotor       r1          Rotor that will be considered in the second position.
        Input:      Rotor       r1          Rotor that will be considered in the third position.

    Function: rotate()
        Purpose: To rotate the block in the correct way. The first rotor will complete a full rotation before the second rotor will rotate.

    Funtion: printblock()
        Purpose: To print the block of rotors list to the command line.

    Function: inputs(inp)
        Purpose: This is the main body of the class. This function allows for the actual input to go through the rotors as discribed in the readme.
        Input:      Char        inp         The character that you wish to input into the rotors.
        Returns:    Char                    The character that will return after going through all the rotors.
'''
class RotorBlock:
    def __init__(self,r = Rotor(rotorList[0]),r1 = Rotor(rotorList[1]),r2 = Rotor(rotorList[2])):
        self.a = r
        print(self.a.printself())
        print(len(self.a.List))
        self.b = r1
        self.c = r2

    def rotate(self):
        if self.a.getPos() == 26:
            self.a.resetPos()
            if self.b.getPos() == 26:
                self.b.resetPos()
                self.c.rotate()
            else:
                self.b.rotate()
        else:
            self.a.rotate()

    def printblock(self):
        self.a.printself()
        self.b.printself()
        self.c.printself()

    def inputs(self,inp):
        z = self.a.changeChartoInt(inp)
        self.rotate()
        z = self.b.changeInttoInt(z ,self.a.getRot())
        self.rotate()
        z = self.c.changeInttoInt(z ,self.b.getRot())
        self.rotate()
        z = self.c.changeInttoInt(z ,self.c.getRot())
        self.rotate()
        z = self.b.changeInttoInt(z ,self.c.getRot())
        self.rotate()
        outp = chr(self.a.changeInttoInt(z ,self.b.getRot()))
        return outp


'''
Function: makeRotor(rotor, startval)
    Purpose: This allows for the rotor to be made and started at the correct position.
    Input:      list        rotor           The Rotor list to be used.
    Input:      Int         startval        The starting position that the rotor will start in. Defaulted to 0.
'''
def makeRotor(rotor,startval = 0):
    rotor = Rotor(rotor,startval)
    rotor.start()
    return rotor


'''
Function: rotors()
    Purpose: To have a rudamentary ability to have the user chose a rotor (given that they must know what they look like before runtime) and a start position.
'''
def rotors():
    limiter = 1
    rotor = []
    start = []
    i=1
    while limiter == 1:
        inp = input("What rotor " + str(i) + " do you want?")
        try:
            intinp = int(inp)
            try:
                rotor.index(intinp)
                print("Please enter a new number")
            except ValueError:
                if intinp <= 5 and intinp > 0:
                    rotor.append(intinp)
                    limiter = 2
                    while limiter == 2:
                        startVal = input("what start val did you want of rotor "+str(i)+"?")
                        try:
                            startint = int(startVal)
                            if startint < 27 and startint >= 0:
                                start.append(startint)
                                i+=1
                                limiter = 1
                                if(len(rotor) == 3):
                                    limiter = 0
                            else:
                                print("Please input a value between 0 and 26")
                        except ValueError:
                            print("Please input a integer")
                else:
                    print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter an Integer")
    rotora = makeRotor(rotorList[rotor[0]-1],start[0])
    rotorb = makeRotor(rotorList[rotor[1]-1],start[1])
    rotorc = makeRotor(rotorList[rotor[2]-1],start[2])
    block = RotorBlock(rotora,rotorb,rotorc)
    return block



def test():
    i = 0
    #rotors()
    rotoa = makeRotor(rotor1,0)
    rotob = makeRotor(rotor2,1)
    rotoc = makeRotor(rotor3,2)
    rotoa.printself()
    d = RotorBlock(rotoa,rotob,rotoc)
    c = RotorBlock(rotoa,rotob,rotoc)
    c.printblock()
    print()
    '''while i < 27:
        c.rotate()
        c.printblock()
        print()
        i+=1'''

    outp = c.inputs("A")
    print (outp)
    outb = d.inputs(outp)
    print(outb)
    #print(chr(rotoa.changeInttoInt(rotob.changeInttoInt(rotoc.changeInttoInt(rotoc.changeInttoInt(rotob.changeInttoInt(rotoa.changeChartoInt("A"),rotoa.getRot()),rotob.getRot()),rotoc.getRot()),rotoc.getRot()),rotob.getRot())))
    #roto.change('A')
    #roto.rotate()


if __name__=="__main__":
    debug = True
    test()
