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
        pass

    def testGetHitCount(self):
        pass

    def testGetShipsSunk(self):
        pass

    def testGetShipArray(self):
        pass


if __name__ == '__main__':
    unittest.main()
