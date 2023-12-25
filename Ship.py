class Ship:

    #instance variables
    bowRow = 0
    bowColumn = 0

    length = 0

    horizontal = False

    hitArray =[]

    shipType = "Base"

    def __init__(self, length):
        '''Constructor that establishes the length of the shit and the boolean hit array to keep track of whether
        shots hit the ship'''
        self.length = length
        self.hitArray = [False for i in range(length)]


    #getters and setters
    def getBowRow(self):
        return self.bowRow

    def getBowColumn(self):
        return self.bowColumn

    def setBowRow(self, row):
        self.bowRow = row

    def setBowColumn(self, column):
        self.bowColumn = column

    def isHorizontal(self):
        return self.horizontal

    def setHorizontal(self, horizontal):
        self.horizontal = horizontal

    def getLength(self):
        return self.length

    def getHitArray(self):
        return self.hitArray

    def getShipType(self):
        return self.shipType

    def __str__(self):
        return f'{self.shipType}'





