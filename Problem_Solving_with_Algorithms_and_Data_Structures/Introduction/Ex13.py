class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 or b==0:
            return 0
        else:
            return 1

        if a==1 or b==0:
            return 1
        else:
            return 0

        if a==0 or b==1:
            return 1
        else:
            return 0

        if a==1 or b==1:
            return 0
        else:
            return 1


class bit8Summator(BinaryGate):

    def __init__(self,n, Sum, Carry):
        BinaryGate.__init__(self,n)
        Sum = 0
        Carry = 0

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        Carry = a & b
        Sum = a ^ b
        print("Sum is: ", Sum)
        print("Carry is: ", Carry)
        return Sum, Carry

