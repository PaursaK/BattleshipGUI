import unittest
from EmptySea import *
from Battleship import *
from Cruiser import *
from Destroyer import *
from Submarine import *
from Ocean import *

class OceanTest(unittest.TestCase):

    NUM_BATTLESHIPS = 1
    NUM_CRUISERS = 2
    NUM_DESTROYERS = 3
    NUM_SUBMARINES = 4
    OCEAN_SIZE = 10

    def setUp(self):

        self.ocean = Ocean()

        self.NUM_BATTLESHIPS = 1
        self.NUM_CRUISERS = 2
        self.NUM_DESTROYERS = 3
        self.NUM_SUBMARINES = 4
        self.OCEAN_SIZE = 10

    def testEmptyOcean(self):

        #get the ship array
        oceanArray = self.ocean.getShipArray()

        #iterate over rows and columns and test that each element in the array is an empty sea object
        for i in range(len(oceanArray)):
            for j in range(len(oceanArray[i])):
                ship = oceanArray[i][j]
                self.assertEqual("empty", ship.getShipType())

        #check that bow rows and columns are set to the exact coordinates the empty sea objects are placed
        self.assertEqual(0, oceanArray[0][0].getBowRow())
        self.assertEqual(0, oceanArray[0][0].getBowColumn())

        self.assertEqual(5, oceanArray[5][5].getBowRow())
        self.assertEqual(5, oceanArray[5][5].getBowColumn())

        self.assertEqual(9, oceanArray[9][0].getBowRow())
        self.assertEqual(0, oceanArray[9][0].getBowColumn())

    def testPlaceAllShipsRandomly(self):

        #tests that the correct numer of each ship type is placed in the ocean

        # get the ship array and place ships randomly
        self.ocean.placeAllShipsRandomly()
        oceanArray = self.ocean.getShipArray()

        #datastructure to collect the number of ships found
        shipsFoundList = []

        numBattleships = 0
        numCruisers = 0
        numDestroyers = 0
        numSubmarines = 0
        numEmptySeas = 0

        #iterate over rows and columns
        for i in range(len(oceanArray)):
            for j in range(len(oceanArray[i])):
                #save ship at specified index
                ship = oceanArray[i][j]
                #check if ship is found in the ship found list, if not add it
                if (ship not in shipsFoundList):
                    shipsFoundList.append(ship)

        for object in shipsFoundList:
            if object.getShipType() == "battleship":
                numBattleships +=1
            elif object.getShipType() == "destroyer":
                numDestroyers +=1
            elif object.getShipType() == "cruiser":
                numCruisers += 1
            elif object.getShipType() == "submarine":
                numSubmarines += 1
            elif object.getShipType() == "empty":
                numEmptySeas += 1

        #check if there are the correct number of ships in total of each type
        self.assertEqual(self.NUM_BATTLESHIPS, numBattleships)
        self.assertEqual(self.NUM_CRUISERS, numCruisers)
        self.assertEqual(self.NUM_DESTROYERS, numDestroyers)
        self.assertEqual(self.NUM_SUBMARINES, numSubmarines)

        #calculate total number of available spaces and occupied spaces
        totalSpaces = self.OCEAN_SIZE **2
        occupiedSpaces = (self.NUM_BATTLESHIPS*4) + (self.NUM_CRUISERS*3) + (self.NUM_SUBMARINES*1) + (self.NUM_DESTROYERS*2)

        #test number of empty sea objects, each with a length of 1
        self.assertEqual(totalSpaces - occupiedSpaces, numEmptySeas)

    def testIsOccupied(self):

        #place destroyer at an acceptable coordinate
        destroyer = Destroyer()
        row = 1
        column = 5
        horizontal = False
        destroyer.placeShipAt(row, column, horizontal, self.ocean)

        #test that destroyer is at 1,5 and whether it is actually a destroyer
        self.assertTrue(self.ocean.isOccupied(1, 5))
        self.assertEqual("destroyer", self.ocean.getShipArray()[1][5].getShipType())

        #place submarine at an acceptable coordinate
        submarine = Submarine()
        row = 0
        column = 0
        horizontal = False
        submarine.placeShipAt(row, column, horizontal, self.ocean)

        #test that destroyer is at 1,5 and whether it is actually a destroyer
        self.assertTrue(self.ocean.isOccupied(0, 0))
        self.assertEqual("submarine", self.ocean.getShipArray()[0][0].getShipType())

        #place battleship at an acceptable coordinate
        battleship = Battleship()
        row = 9
        column = 9
        horizontal = True
        battleship.placeShipAt(row, column, horizontal, self.ocean)

        #check that the correct positions are being occupied by the same battleship instance
        self.assertTrue(self.ocean.isOccupied(9, 9))
        self.assertTrue(self.ocean.isOccupied(9, 8))
        self.assertTrue(self.ocean.isOccupied(9, 7))
        self.assertTrue(self.ocean.isOccupied(9, 6))
        self.assertEqual("battleship", self.ocean.getShipArray()[9][9].getShipType())
        self.assertEqual("battleship", self.ocean.getShipArray()[9][6].getShipType())

    def testShootAt(self):

        #SCENARIO 1 - EMPTY SEA OBJECT FIRED UPON
        #no ship is placed here, so function should return false
        self.assertFalse(self.ocean.shootAt(0,0))
        self.assertFalse(self.ocean.shootAt(9, 9))

        #SCENARIO 2 - REAL SHIPS BEING FIRED UPON
        destroyer = Destroyer()
        row = 1
        column = 5
        horizontal = False
        destroyer.placeShipAt(row, column, horizontal, self.ocean)

        #test each fire is registered and the status of the ship (sunk or not)
        self.assertTrue(self.ocean.shootAt(1, 5))
        self.assertFalse(destroyer.isSunk())
        self.assertTrue(self.ocean.shootAt(0, 5))
        self.assertTrue(destroyer.isSunk())
        self.assertEqual(self.ocean.getShipsSunk(), 1)

        #SCENARIO 3 - TEST AGAINST SHIPS THAT HAVE ALREADY BEEN HIT (BOTH SUNK AND NOT SUNK)
        sub1 = Submarine()
        row = 0
        column = 0
        horizontal = False
        sub1.placeShipAt(row, column, horizontal, self.ocean)

        sub2 = Submarine()
        row = 9
        column = 9
        horizontal = False
        sub2.placeShipAt(row, column, horizontal, self.ocean)

        #check that submarines were successfully fired upon
        self.assertTrue(self.ocean.shootAt(0,0))
        self.assertTrue(self.ocean.shootAt(9, 9))
        #check that they are successfully registered a sunk
        self.assertTrue(sub1.isSunk())
        self.assertTrue(sub2.isSunk())
        #check that hits do not register anymore after a ship has been sunk
        self.assertFalse(self.ocean.shootAt(0, 0))
        self.assertFalse(self.ocean.shootAt(9, 9))

        destroyer2 = Destroyer()
        row = 5
        column = 5
        horizontal = False
        destroyer2.placeShipAt(row, column, horizontal, self.ocean)

        #check that hitting a destroyer ship (length 2) in the same spot is registered as long as the ship is
        #not considered sunk
        self.assertTrue(self.ocean.shootAt(5, 5))
        self.assertFalse(destroyer2.isSunk())
        self.assertTrue(self.ocean.shootAt(5, 5))
        self.assertFalse(destroyer2.isSunk())

    def testGetShotsFired(self):
		#SCENARIO 1 - should be all false since no ships added yet 
        self.assertFalse(self.ocean.shootAt(0, 1))
        self.assertFalse(self.ocean.shootAt(1, 0))
        self.assertFalse(self.ocean.shootAt(3, 3))
        self.assertFalse(self.ocean.shootAt(9, 9))
        self.assertEquals(4, self.ocean.getShotsFired())
		
        destroyer = Destroyer()
        row = 1
        column = 5
        horizontal = False
        destroyer.placeShipAt(row, column, horizontal, self.ocean)

        #SCENARIO 2 - shotsFired accrue regardless of hit/sunk status of the ship(s)
        submarine = Submarine()
        row = 0
        column = 0
        horizontal = False
        submarine.placeShipAt(row, column, horizontal, self.ocean)

        self.assertTrue(self.ocean.shootAt(1, 5))
        self.assertFalse(destroyer.isSunk())
        self.assertTrue(self.ocean.shootAt(0, 5))
        self.assertTrue(destroyer.isSunk())
        self.assertEquals(6, self.ocean.getShotsFired())

        #SCENARIO 3 - Test the same spot still triggers shotsFired counter to increase
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = False
        cruiser.placeShipAt(row, column, horizontal, self.ocean)
		
        #fire one shot and hit
        self.assertTrue(self.ocean.shootAt(9, 9))
		#ship should not be sunk
        self.assertFalse(cruiser.isSunk())
	    #shot counter should increase by 1
        self.assertEquals(7, self.ocean.getShotsFired())
		
		#fire at the same spot and check
        self.assertTrue(self.ocean.shootAt(9, 9))
        self.assertFalse(cruiser.isSunk())
        self.assertEquals(8, self.ocean.getShotsFired())




    def testGetHitCount(self):
		
        #SCENARIO 1 (provided) - one shot that hits part of the ship should be registered
        destroyer = Destroyer()
        row = 1
        column = 5
        horizontal = False
        destroyer.placeShipAt(row, column, horizontal, self.ocean)
		
        self.assertTrue(self.ocean.shootAt(1, 5))
        self.assertFalse(destroyer.isSunk())
        self.assertEquals(1, self.ocean.getHitCount())
		
		

		#SCENARIO 2 - Shot that hits the same spot should be registered if ship has not sunk
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = False
        cruiser.placeShipAt(row, column, horizontal, self.ocean)
		
		#fire one shot and hit
        self.assertTrue(self.ocean.shootAt(9, 9))
		#ship should not be sunk
        self.assertFalse(cruiser.isSunk())
	    #shot counter should increase by 1
        self.assertEquals(2, self.ocean.getHitCount())

		#fire same shot, ship still not sunk but hitCount increases again
        self.assertTrue(self.ocean.shootAt(9, 9))
        self.assertFalse(cruiser.isSunk())
        self.assertEquals(3, self.ocean.getHitCount())
		
		#SCENARIO 3 - hit count should not increase if a shot strikes a sunken ship
		
		#fire another shot, ship still not sunk but hitCount increases again
        self.assertTrue(self.ocean.shootAt(8, 9))
        self.assertFalse(cruiser.isSunk())
        self.assertEquals(4, self.ocean.getHitCount())
                
        #fire final shot, ship should be sunk and hitCount increases again
        self.assertTrue(self.ocean.shootAt(7, 9))
        self.assertTrue(cruiser.isSunk())
        self.assertEquals(5, self.ocean.getHitCount())
                
        #fire shot to hit sunken boat, ship should be sunk but hitCount should not increase
        self.assertFalse(self.ocean.shootAt(9, 9))
        self.assertTrue(cruiser.isSunk())
        self.assertEquals(5, self.ocean.getHitCount())
                
        #SCENARIO 4 - Fire on an EmptySea object and make sure hitCount does not increase        
        self.assertFalse(self.ocean.shootAt(0, 0))
        self.assertEquals(5, self.ocean.getHitCount())
        self.assertEquals(7, self.ocean.getShotsFired())


    def testGetShipsSunk(self):
        #SCENARIO 1 - Test that one shot does not sink a destroyer
        destroyer = Destroyer()
        row = 1
        column = 5
        horizontal = False
        destroyer.placeShipAt(row, column, horizontal, self.ocean)
                
        self.assertTrue(self.ocean.shootAt(1, 5))
        self.assertFalse(destroyer.isSunk())
        self.assertEquals(1, self.ocean.getHitCount())
        self.assertEquals(0, self.ocean.getShipsSunk())
		
		
		#SCENARIO 2 - Test that a cruiser and submarine are sunken after all required shots are made
		
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = False
        cruiser.placeShipAt(row, column, horizontal, self.ocean)
                
        #fire one shot and hit
        self.assertTrue(self.ocean.shootAt(9, 9))
        #ship should not be sunk
        self.assertFalse(cruiser.isSunk())
        #no ships sunk yet
        self.assertEquals(0, self.ocean.getShipsSunk())
                
        #fire second shot and hit
        self.assertTrue(self.ocean.shootAt(8, 9))
        #ship should not be sunk
        self.assertFalse(cruiser.isSunk())
        #no ships sunk yet
        self.assertEquals(0, self.ocean.getShipsSunk())
                
        #fire third shot and final shot
        self.assertTrue(self.ocean.shootAt(7, 9))
        #ship should be sunk
        self.assertTrue(cruiser.isSunk())
        #1 ship(s) sunk
        self.assertEquals(1, self.ocean.getShipsSunk())

                
        submarine = Submarine()
        row = 0
        column = 0
        horizontal = False
            
        submarine.placeShipAt(row, column, horizontal, self.ocean)
                
        #fire one shot and hit
        self.assertTrue(self.ocean.shootAt(0, 0))
        #ship should be sunk
        self.assertTrue(submarine.isSunk())
        #2 ships sunk
        self.assertEquals(2, self.ocean.getShipsSunk())
                
        #SCENARIO 3 - Test that an already sunken ship does not get double counted
                
        #fire same shot that sunk submarine
        self.ocean.shootAt(0, 0)
        #2 ships sunk still after repeat fire
        self.assertEquals(2, self.ocean.getShipsSunk())
        #fire same shot that sunk cruiser
        self.ocean.shootAt(9, 9)
        #2 ships sunk still
        self.assertEquals(2, self.ocean.getShipsSunk())

    def testGetShipArray(self):

        shipArray = self.ocean.getShipArray()
        self.assertEquals(self.OCEAN_SIZE, len(shipArray))
        self.assertEquals(self.OCEAN_SIZE, len(shipArray[0]))

        self.assertEquals("empty", shipArray[0][0].getShipType())

        #Scenario 1 - place Cruiser at 2,0 and see if it is in the shipArray
        cruiser = Cruiser()
        row = 2
        column = 0
        horizontal = False
        cruiser.placeShipAt(row, column, horizontal, self.ocean)

        # testing all 3 places where cruiser is. 
        self.assertEquals("cruiser", shipArray[row][column].getShipType())
        self.assertEquals("cruiser", shipArray[row-1][column].getShipType())
        self.assertEquals("cruiser", shipArray[row-2][column].getShipType())

        # Scenario 2 - place Submarine at 9,9 and shoot at it and sink it and test the shipArray
        sub = Submarine()
        row = 9
        column = 9
        sub.placeShipAt(row, column, horizontal, self.ocean) # place sub
        sub.shootAt(row, column) # shoot and sink sub
        self.assertEquals("s",shipArray[row][column].__str__()) # see if shipArray outputs correct to String

        shipsFound = []
        for column in range (len(shipArray)):
            for row in range (len(shipArray)):
                ship = shipArray[column][row]
                if (ship not in shipsFound) and (ship.getShipType() != "empty"):
                    shipsFound.append(ship)

        self.assertEquals(2,len(shipsFound)) # expected number of ships
        self.assertTrue(sub in shipsFound) # check if it contains submarine 
        self.assertTrue(cruiser in shipsFound) # check if it contains cruiser
            


if __name__ == '__main__':
    unittest.main()
