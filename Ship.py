#from Ocean import Ocean

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
        False if there is a False found in the hit array
        :return: True/False'''

        #check if the False is still in the hit array and return false
        #indicating the ship is not sunk
        if (False in self.hitArray):
            return False
        else:
            #if true occupies the entire array return true
            return True

    def okToPlaceShipAt(self, row, column, horizontal, oceanObject):
        '''Based on given row, column, and orientation, returns true if it is okay to
	    put a ship of this length with its bow in this location; false otherwise. The
	    ship must not overlap another ship, or touch another ship (vertically,
	    horizontally, diagonally), and it must not "stick out" beyond the array. Does
	    not actually change either the ship or the Ocean. It just says if it is legal
	    to do so.
	    For placement consistency, let’s agree that horizontal ships face East (bow at right end) and
	    vertical ships face South (bow at bottom end).
	    :param: int row, int column, boolean horizontal, Ocean instance
	    :return: true/false'''

        shipLength = self.getLength()

        #HORIZONTAL CHECK

        #check placement compatibility for horizontal ships
        if(horizontal):

            #first try and check if ship can be placed at all
            #use try and except block to see if potential placement is out of bounds
            try:
                for i in range(shipLength):
                    newColumn = column - i
                    if(oceanObject.isOccupied(row,newColumn)):
                        return False

            except IndexError as e:
                return False

            #then check if ship can be legally placed (no diagnol or horizontal adjacent)
            for i in range(row - 1, row+2):

                for j in range(column-shipLength, column+2):
                    try:
                        if(oceanObject.isOccupied(i, j)):
                            return False
                    except IndexError as e:
                        continue

        #VERTICAL CHECK
        # check placement compatibility for vertical ships
        if (horizontal is False):

            # first try and check if ship can be placed at all
            # use try and except block to see if potential placement is out of bounds
            try:
                for i in range(shipLength):
                    newRow = row - i

                    if (oceanObject.isOccupied(newRow, column)):
                        return False
            except IndexError as e:
                return False

            # then check if ship can be legally placed (no diagnol or horizontal adjacent)
            for i in range(row - shipLength, row + 2):

                for j in range(column - 1, column + 2):
                    try:
                        if (oceanObject.isOccupied(i, j)):
                            return False
                    except IndexError as e:
                        continue

        #check pass without returning False, its okay to place ship
        return True

    def placeShipAt(self, row, column, horizontal, oceanObject):
        '''Puts the ship in the Ocean. This involves giving values to bowRow, bowColumn, and horizontal
	       instance variables in the ship, and it also involves putting a reference to the ship in
	       each of 1 or more locations (up to 4) in the ships array in the Ocean object.
	      :param: int row, int column, boolean horizontal, Ocean instance'''

        #grab ship array from the ocean instance
        oceanBoard = oceanObject.getShipArray()

        #set bowRow, bowColumn, and horizontal boolean
        self.setBowRow(row)
        self.setBowColumn(column)
        self.setHorizontal(horizontal)

        #check if boolean is true (horizontal)
        if(self.isHorizontal()):

            #iterate over length of the ship
            for i in range(self.getLength()):
                #place ship horizontally along the same row, bow starts east and moves west
                #and place the same ship in the ships array
                oceanBoard[self.bowRow][self.bowColumn -i] = self

        #in case the ship is vertical
        else:
            #iterate over the length of the ship
            for i in range(self.getLength()):
                # place ship vertically along the same column, bow starts south and moves north
                # and place the same ship in the ships array
                oceanBoard[self.bowRow-i][self.bowColumn] = self




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





