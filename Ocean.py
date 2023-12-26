from EmptySea import EmptySea
class Ocean:

    #INSTANCE VARIABLES

    #ship array for the game board setup
    ShipArray = [[0 for i in range(10)] for i in range(10)]

    #total number of shots fired by the user
    shotsFired = 0

    #number of times a shot hit a ship
    hitCount = 0

    #number of ships sunk (max 10, 10 ships total in play)
    shipsSunk = 0

    def __init__(self):

        #iterate over the rows of the ship array
        for i in range(len(self.ShipArray)):
            #iterate over the columns of the ship array
            for j in range(len(self.ShipArray[i])):
                #initialize an empty sea object each iteration
                emptySea = EmptySea()




