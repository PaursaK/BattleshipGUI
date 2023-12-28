from Ocean import Ocean

class Ship:
    '''generic ship object that is the backbone for the ships used in the battlship game'''

    #INSTANCE VARIABLES

    #coordinates for the ship bow
    bowRow = 0
    bowColumn = 0

    #length of ship
    length = 0

    #boolean for whether the ship is horiztonal
    horizontal = False

    #the position available to hit for the ship(boolean array)
    hitArray =[]

    #ship type
    shipType = "Generic"

    def __init__(self, length):
        '''Constructor that establishes the length of the ship and the boolean hit array to keep track of whether
        shots hit the ship'''
        self.length = length
        self.hitArray = [False for i in range(length)]


    #getters and setters
    def getBowRow(self):
        '''returns the bowRow instance variable integer'''
        return self.bowRow

    def getBowColumn(self):
        '''returns the bowColumn instance variable integer'''
        return self.bowColumn

    def setBowRow(self, row):
        '''param: integer row
        sets the bowRow to the integer passed'''
        self.bowRow = row

    def setBowColumn(self, column):
        '''param: integer column
        sets the bowColumn to the integer passed'''
        self.bowColumn = column

    def isHorizontal(self):
        '''returns the Horizontal instance variable (true or false)'''
        return self.horizontal

    def setHorizontal(self, horizontal):
        '''param: horizontal boolean (true/false)
        sets the horizontal variable to the boolean passed'''
        self.horizontal = horizontal

    def getLength(self):
        '''returns the length of the ship'''
        return self.length

    def getHitArray(self):
        '''returns the hit array/list'''
        return self.hitArray

    def getShipType(self):
        '''returns a string with the ship type'''
        return self.shipType

    def isSunk(self):
        '''returns true or false indicating whether the ship is sunk or not.
        true if there is no False spot found in the hit array
        False if there is a False found in the hit array'''

        #check if the False is still in the hit array and return false
        #indicating the ship is not sunk
        if (False in self.hitArray):
            return False
        else:
            #if true occupies the entire array return true
            return True

    def okToPlaceShipAt(self, row, column, horizontal, oceanObject):
        pass

    def placeShipAt(self, row, column, horizontal, oceanObject):


    def shootAt(self, row, column):
        '''If a part of the ship occupies the given row and column, and the ship hasn't been sunk,
	    mark that part of the ship as "hit" and return true; otherwise return false
	    :param: int row coordinates, int column coordinates
	    :return: true or false depending on if the ship has been successfully "hit"'''

        #check whether the ship being shot at is sunk already
        if(self.isSunk() is False):

            #check whether the ship is vertical
            if(self.isHorizontal() is False):

                #check if the bowColumn is equal to the column passed
                if(self.getBowColumn() == column):

                    # check if row passed is within the bowRow and bowRow  minus the ship length
                    if (self.getBowRow() >= row and row >= (self.getBowRow() - self.getLength())):

                        #update hit array to reflect the hit and return true
                        self.getHitArray()[self.getBowRow() - row] = True
                        return True

            #This is when the ship is horizontal
            else:

                # check if the bowColumn is equal to the column passed
                if (self.getBowRow() == row):

                # check if column passed is within the bowColumn and bowColumn minus the ship length
                    if (self.getBowColumn() >= column and column >= (self.getBowColumn() - self.getLength())):

                        #update hit array to reflect the hit and return true
                        self.getHitArray()[self.getBowColumn() - column] = True
                        return True

        #if a hit does not land, return false
        return False






    def __str__(self):
        '''returns a single character String representing the object
        return: "s" if sunk and "x" if not sunk (but hit)'''

        #if ships is sunk, return "s" character
        if(self.isSunk()):
            return "s"

        #return "x" for hit but not sunk
        return "x"





