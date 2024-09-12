from EmptySea import EmptySea
from Battleship import Battleship
from Cruiser import Cruiser
from Destroyer import Destroyer
from Submarine import Submarine
from random import *
class Ocean:

    #INSTANCE VARIABLES

    #ship array for the game board setup
    shipArray = [[0 for i in range(10)] for i in range(10)]

    #total number of shots fired by the user
    shotsFired = 0

    #number of times a shot hit a ship
    hitCount = 0

    #number of ships sunk (max 10, 10 ships total in play)
    shipsSunk = 0

    def __init__(self):
        '''initialized the Ocean (gameboard) it places emptySea objects in every slot available'''

        #iterate over the rows of the ship array
        for i in range(len(self.shipArray)):
            #iterate over the columns of the ship array
            for j in range(len(self.shipArray[i])):

                #initialize an empty sea object each iteration
                emptySea_instance = EmptySea()
                horizontal = False

                #place ship in array
                emptySea_instance.placeShipAt(i, j, horizontal, self)
                self.shipArray[i][j] = emptySea_instance

    #GETTERS
    def getShipArray(self):
        '''returns ship array (aka the gameboard)'''
        return self.shipArray

    def getShipsSunk(self):
        '''returns the number of ships sunk thus far'''
        return self.shipsSunk

    def isGameOver(self):
        '''returns true if all 10 ships are sunk, indicating the end of the game'''
        #check whether number of sunk ships is equivalent to 10
        if(self.getShipsSunk() == 10):
            return True

        return False

    def getHitCount(self):
        '''returns the number of hits accumulated in the game thus far'''
        return self.hitCount

    def getShotsFired(self):
        '''returns the total number of shots fired'''
        return self.shotsFired

    def placeAllShipsRandomly(self):
        '''populate the game board by placing ships randomly from largest to smallest ships.
        Using the random module methods we randomly select coordinates for the ships Bow and whether it is
        horizontal or vertical.'''

        #grab the list of ships (largest to smallest, total of 10 ships)
        listOfShips = self.addAllShipsToArray()

        #iterate through the list of ships
        for ship in listOfShips:

            #enter a while loop condiiton
            while(True):

                #generate coordinates and orientation of ship with the random module methods
                row = randint(0,9)
                column = randint(0, 9)
                horizontal = False if randint(0, 1) == 1 else True

                #check that the space is not occupied by legitimate ships
                if(self.isOccupied(row, column) is False):

                    #verify you can place a ship at those coordinates(cannot be adjacent to another ship)
                    canPlace = ship.okToPlaceShipAt(row, column, horizontal, self)

                    #if you can, place the ship there and break out of while loop to move onto next ship
                    if(canPlace):
                        ship.placeShipAt(row, column, horizontal, self)
                        break


    def addAllShipsToArray(self):
        '''returns an array of all the ships from the longest to shortest and their quantity
        :return: List of Ship objects from longest to shortest'''
        #create empty list for ship appending
        listOfShips_Longest_to_Shortest = []

        #iterate 10 times
        for i in range(10):

            #add battleship once and at the beginning
            if (i == 0):
                listOfShips_Longest_to_Shortest.append(Battleship())

            # add cruiser twice and at the after battleship
            elif (1 <= i <= 2):
                listOfShips_Longest_to_Shortest.append(Cruiser())

            # add destroyer thrice and at the after cruiser(s)
            elif (3 <= i <= 5):
                listOfShips_Longest_to_Shortest.append(Destroyer())

            # add submarine 4 times and at the after destroyer(s)
            elif (6 <= i < 10):
                listOfShips_Longest_to_Shortest.append(Submarine())

        #return list of ships
        return listOfShips_Longest_to_Shortest

    def isOccupied(self, row, column):
        '''returns true or false on whether a given location contains a valid ship (not empty sea object)
        :param: int row, int column
        :return: true/false'''

        #check whether the coordinates provided are an empty sea object or not
        if(self.shipArray[row][column].getShipType() == "empty"):
            return False

        return True

    def shootAt(self, row, column):
        '''returns true if the given location contains a "real" ship, still a float (Not
        an EmptySea), false if it does not. In addition, this method updates the
        number of shots that have been fired, and the number of hits
        :param: int row, int column
        :return: boolean - true/false'''

        #accumulate shotsFired every time a shot is taken
        self.shotsFired+=1

        #grab ship array and index row and column and call ship shootAt method
        if(self.getShipArray()[row][column].shootAt(row, column)):

            #if a legitimate ship is there increment hit count by 1
            self.hitCount+=1

            #next check whether that ship is sunk because of that hit, if true increment shipsSunk count
            if(self.getShipArray()[row][column].isSunk()):
                self.shipsSunk+=1

            #return true if shot strikes a ship
            return True

        #return false if EmptySea object was there (no hit registered)
        return False

    def gamePrint(self):
        '''Prints the Ocean Top left corner square is indexed at 0,0 Numbers should be 0 -> 9
	       "x" - indicates a location that has been fired upon and hit a real ship
	       "-" - indicates a location that has been fired upon and found nothing.
  	       "s" - indicates a location containing a sunken ship.
           "." - indicates a location that has never been fired upon'''

        #grab ship array
        shipArr = self.getShipArray()

        #print the labels for the column coordinates
        print(" ", end = " ")
        for i in range(len(shipArr)):
            print(i, end = " ")

        #print the labels for the row coordinates
        for i in range(len(shipArr)):
            print()
            print(i, end = " ")

            #now iterate over columns
            for j in range(len(shipArr)):


                #check if ship at each location is sunk
                if(shipArr[i][j].isSunk()):
                    print(shipArr[i][j], end =  " ")

                #for vertical ships
                #get hit array, if index of hit array is true and the column matches iterated column
                elif(shipArr[i][j].isHorizontal() == False and shipArr[i][j].getHitArray()[shipArr[i][j].getBowRow()-i] and shipArr[i][j].getBowColumn() == j):
                    #print the type of hit either 'x' for ship or '-' for empty sea object
                    print(shipArr[i][j], end = " ")

                # for horizontal ships
                # get hit array, if index of hit array is true and the row matches iterated row
                elif(shipArr[i][j].isHorizontal() == True and shipArr[i][j].getHitArray()[shipArr[i][j].getBowColumn()-j] and shipArr[i][j].getBowRow() == i):
                    # print the type of hit either 'x' for ship or '-' for empty sea object
                    print(shipArr[i][j], end = " ")

                else:
                    #print for a spot that has not been fired upon
                    print(".", end = " ")


    def printWithShips(self):
        '''for testing purposes'''
        # grab ship array
        shipArr = self.getShipArray()

        # print the labels for the column coordinates
        print(" ", end=" ")
        for i in range(len(shipArr)):
            print(i, end=" ")

        # print the labels for the row coordinates
        for i in range(len(shipArr)):
            print()
            print(i, end=" ")

            # now iterate over columns
            for j in range(len(shipArr)):

                if(shipArr[i][j].getShipType() == "battleship"):
                    print("b", end = " ")
                elif(shipArr[i][j].getShipType() == "cruiser"):
                    print("c", end=" ")
                elif(shipArr[i][j].getShipType() == "destroyer"):
                    print("d", end=" ")
                elif(shipArr[i][j].getShipType() == "submarine"):
                    print("s", end=" ")
                else:
                    print("-", end = " ")













