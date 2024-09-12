import unittest
from EmptySea import *
from Battleship import *
from Cruiser import *
from Destroyer import *
from Submarine import *
from Ocean import *

class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.ocean = Ocean()

    def testGetLength(self):
        ship = Battleship()
        self.assertEquals(4, ship.getLength())
		#test Cruiser length
        self.assertEquals(3, Cruiser().getLength())
		#test Destroyer length
        self.assertEquals(2, Destroyer().getLength())
		#test Submarine length
        self.assertEquals(1, Submarine().getLength())

    def testGetBowRow(self):
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        battleship.placeShipAt(row, column, horizontal, self.ocean)
        self.assertEquals(row, battleship.getBowRow())
		
		
		#Test cruiser
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = True
        cruiser.placeShipAt(row, column, horizontal, self.ocean)
        self.assertEquals(row, cruiser.getBowRow())
		
		# test submarine
        sub = Submarine()
        row = 5
        column = 5
        horizontal = False
        sub.placeShipAt(row, column, horizontal, self.ocean)
        self.assertEquals(row, sub.getBowRow())

    def testGetBowColumn(self):
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        battleship.placeShipAt(row, column, horizontal, self.ocean)
        battleship.setBowColumn(column)
        self.assertEquals(column, battleship.getBowColumn())
		
		#Test cruiser (Scenario 2)
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = True
        cruiser.placeShipAt(row, column, horizontal, self.ocean)
        self.assertEquals(column, cruiser.getBowColumn())

		# test submarine (Scenario 3)
        sub = Submarine()
        row = 5
        column = 5
        horizontal = False
        sub.placeShipAt(row, column, horizontal, self.ocean)
        self.assertEquals(column, sub.getBowColumn())

    def testGetHit(self):
        ship = Battleship()
        hits = [False, False, False, False]
        self.assertEquals(hits, ship.getHitArray())
        self.assertFalse(ship.getHitArray()[0])
        self.assertFalse(ship.getHitArray()[1])
		
		# Scenario 2 - Test hit array on cruiser
        cruiser = Cruiser()
        hits = [False for i in range(cruiser.getLength())]
        self.assertEquals(hits,cruiser.getHitArray())
		# Test cruiser by placing it and shooting at it and checking hit array. 
        row = 3
        column = 0
        horizontal = False
        cruiser.placeShipAt(row, column, horizontal, self.ocean)
        cruiser.shootAt(row, column) # shoot at 3,0
        cruiser.shootAt(1, column) # shoot at 1,0
        self.assertTrue(cruiser.getHitArray()[0]) # check hit array
        self.assertTrue(cruiser.getHitArray()[2]) # check hit array
		
		# Scenario 3 - Test hit array on submarine
        submarine = Submarine()
        hits = [False for i in range(submarine.getLength())]
        self.assertEquals(hits, submarine.getHitArray()) # test default
        row = 9
        column = 9
        submarine.placeShipAt(row, column, horizontal, self.ocean)
        submarine.shootAt(row, column)
        self.assertTrue(cruiser.getHitArray()[0]) # check hit array

    def testGetShipType(self):
        ship = Battleship()
        self.assertEquals("battleship", ship.getShipType())
		# test Cruiser
        ship = Cruiser()
        self.assertEquals("cruiser", ship.getShipType())
		# test Destroyer
        ship = Destroyer()
        self.assertEquals("destroyer", ship.getShipType())
		# test Submarine
        ship = Submarine()
        self.assertEquals("submarine", ship.getShipType())
    
    def testIsHorizontal(self):
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        battleship.placeShipAt(row, column, horizontal, self.ocean)
        self.assertTrue(battleship.isHorizontal())
                
        # Scenario 2 - testing cruiser 
        ship = Cruiser()
        row = 9
        column = 9
        horizontal = True
        ship.placeShipAt(row, column, horizontal, self.ocean)
        self.assertTrue(ship.isHorizontal())
                
        # Scenario 3 - testing destroyer
        ship = Destroyer()
        row = 1
        column = 9
        horizontal = False
        ship.placeShipAt(row, column, horizontal, self.ocean)
        self.assertFalse(ship.isHorizontal())
    
    def testSetBowRow(self):
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        battleship.setBowRow(row)
        self.assertEquals(row, battleship.getBowRow())
		
		#Test cruiser
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = True
        cruiser.setBowRow(row)
        self.assertEquals(row, cruiser.getBowRow())

		#test submarine
        sub = Submarine()
        row = 5
        column = 5
        horizontal = False
        sub.setBowRow(row)
        self.assertEquals(row, sub.getBowRow())

    def testSetBowColumn(self):
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        battleship.setBowColumn(column)
        self.assertEquals(column, battleship.getBowColumn())
		
		# Test cruiser
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = True
        cruiser.setBowColumn(column)
        self.assertEquals(column, cruiser.getBowColumn())

		# test submarine
        sub = Submarine()
        row = 5
        column = 5
        horizontal = False
        sub.setBowColumn(column)
        self.assertEquals(column, sub.getBowColumn())

    def testSetHorizontal(self):
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        battleship.setHorizontal(horizontal)
        self.assertTrue(battleship.isHorizontal())
	
		# Test cruiser
        cruiser = Cruiser()
        row = 9
        column = 9
        horizontal = True
        cruiser.setHorizontal(horizontal)
        self.assertTrue(cruiser.isHorizontal())

		# test submarine
        sub = Submarine()
        row = 5
        column = 5
        horizontal = False
        sub.setHorizontal(horizontal)

    def testOkToPlaceShipAt(self):
        #test when other ships are not in the ocean
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        ok = battleship.okToPlaceShipAt(row, column, horizontal, self.ocean)
        self.assertTrue(ok, "OK to place ship here.")
		
		# Scenario 2 - test invalid vertical placement out of bounds (edge case)
        battleship2 = Battleship()
	
        row = 0
        column = 9
        horizontal = False
        self.assertFalse(battleship2.okToPlaceShipAt(row, column, horizontal, self.ocean))
	
		# Scenario 3 - test cruiser for horizontal out of bounds (edge case)
        cruiser2 = Cruiser()
        row = 0
        column = 0
        horizontal = True
        self.assertFalse(cruiser2.okToPlaceShipAt(row, column, horizontal, self.ocean))

    def testOkToPlaceShipAtAgainstOtherShipsOneBattleship(self):
        '''test when other ships are in the ocean'''
		
		#place first ship
        battleship1 = Battleship()
        row = 0
        column = 4
        horizontal = True
        ok1 = battleship1.okToPlaceShipAt(row, column, horizontal, self.ocean)
        self.assertTrue(ok1, "OK to place ship here.")
        battleship1.placeShipAt(row, column, horizontal, self.ocean)
		

		#test second ship
        battleship2 = Battleship()
        row = 1
        column = 4
        horizontal = True
        ok2 = battleship2.okToPlaceShipAt(row, column, horizontal, self.ocean)
        self.assertFalse(ok2, "Not OK to place ship vertically adjacent below.")
		
		
		# Scenario 2 - test if new ship 'cruiser' can be place at that same spot where
		# battleship1 was placed
        cruiser = Cruiser()
        row = 0
        column = 4
        self.assertFalse(cruiser.okToPlaceShipAt(row, column, horizontal, self.ocean))

		# Scenario 3 - test if new ship 'cruiser' can be placed adjacent and diagonal
		# to battleship1 (no)
        row = 1
        column = 5
        self.assertFalse(cruiser.okToPlaceShipAt(row, column, horizontal, self.ocean))
		
		# Scenario 4 - place cruiser at a real spot and see if submarine can be placed near it
        row = 9
        column = 1
        horizontal = False
        self.assertTrue(cruiser.okToPlaceShipAt(row, column, horizontal, self.ocean))
        cruiser.placeShipAt(row, column, horizontal, self.ocean) # place cruiser
		
        sub = Submarine() # init new submarine to try and place near cruiser
		# test 4 corners and sides (even out of bounds) for cruiser
        self.assertFalse(sub.okToPlaceShipAt(6, 0, horizontal, self.ocean))
        self.assertFalse(sub.okToPlaceShipAt(6, 2, horizontal, self.ocean))
        self.assertFalse(sub.okToPlaceShipAt(10, 0, horizontal, self.ocean))
        self.assertFalse(sub.okToPlaceShipAt(10, 2, horizontal, self.ocean))
        self.assertFalse(sub.okToPlaceShipAt(9, 0, horizontal, self.ocean))
        self.assertFalse(sub.okToPlaceShipAt(9, 2, horizontal, self.ocean))

    def testPlaceShipAt(self):
        battleship = Battleship()
        row = 0
        column = 4
        horizontal = True
        battleship.placeShipAt(row, column, horizontal, self.ocean)
        self.assertEquals(row, battleship.getBowRow())
        self.assertEquals(column, battleship.getBowColumn())
        self.assertTrue(battleship.isHorizontal())
        self.assertEquals("empty", self.ocean.getShipArray()[0][0].getShipType())
        self.assertEquals(battleship, self.ocean.getShipArray()[0][1])
		
		
		# Scenario 2 - init submarine and place it at 9,9. 
		# Check if submarine is occupied at 9,9
        submarine = Submarine()
        row = 9
        column = 9
        horizontal = False
        submarine.placeShipAt(row, column, horizontal, self.ocean)
        self.assertTrue(self.ocean.isOccupied(row, column))
        self.assertEquals("submarine", self.ocean.getShipArray()[row][column].getShipType())
		
		# Scenario 3 - init destroyer at 9,1
		# check if destroyer is occupied at 9,1
        destroyer = Destroyer()
        row = 9
        column = 1
        horizontal = True
        destroyer.placeShipAt(row, column, horizontal, self.ocean)
        self.assertTrue(self.ocean.isOccupied(row, column))
        self.assertEquals("destroyer", self.ocean.getShipArray()[row][column].getShipType())

    def testShootAt(self):
        #SCENARIO 1 (provided) - test that ship hit array is not influenced by missed shots
        battleship = Battleship()
        row = 0
        column = 9
        horizontal = True
        battleship.placeShipAt(row, column, horizontal, self.ocean)
	
        self.assertFalse(battleship.shootAt(1, 9))
        hitArray0 = [False, False, False, False]
        self.assertEquals(hitArray0, battleship.getHitArray())
		
		
		#SCENARIO 2 - Test that hit array populates true at the correct index
        self.assertTrue(battleship.shootAt(0, 9))
		
		#shooting the bow triggers first index to turn true
        hitArray1 = [True, False, False, False]
        self.assertEquals(hitArray1, battleship.getHitArray())
		
		#test the second part of the ship hit array populates true
        self.assertTrue(battleship.shootAt(0, 8))
        hitArray2 = [True, True, False, False]
        self.assertEquals(hitArray2, battleship.getHitArray())
		
		#check that the end part of the ship populates true
        self.assertTrue(battleship.shootAt(0, 6))
        hitArray3 = [True, True, False, True]
        self.assertEquals(hitArray3, battleship.getHitArray())
		
		#SCENARIO 3 - Shooting the same spot does not to change the array
		
		#check that the end part of the ship populates true
        self.assertTrue(battleship.shootAt(0, 6))
        self.assertEquals(hitArray3, battleship.getHitArray())
		
		#check that the last part of the ship populates true
        self.assertTrue(battleship.shootAt(0, 7))
        hitArray4 = [True, True, True, True]
        self.assertEquals(hitArray4, battleship.getHitArray())
		
		#ship is now sunk, should return false
        self.assertFalse(battleship.shootAt(0, 7))
		#ship is now sunk, check if true
        self.assertTrue(battleship.isSunk())

    def testIsSunk(self):
        #SCENARIO 1 (provided) - test that ship initialized to not sunk and 
		# 						  missed shots don't influence isSunk property
		
        submarine = Submarine()
        row = 3
        column = 3
        horizontal = True
        submarine.placeShipAt(row, column, horizontal, self.ocean)
	
        self.assertFalse(submarine.isSunk())
        self.assertFalse(submarine.shootAt(5, 2))
        self.assertFalse(submarine.isSunk())
		
		
		
        #SCENARIO 2 - Check that ship sinks with the right number of shots
        #check that submarine was sunk
        self.assertTrue(submarine.shootAt(3, 3))
        self.assertTrue(submarine.isSunk())
        self.assertFalse(submarine.shootAt(4, 3))
		
        destroyer1 = Destroyer()
        row = 9
        column = 9
        horizontal = False
        destroyer1.placeShipAt(row, column, horizontal, self.ocean)
		
		#first shot hits
        self.assertFalse(destroyer1.isSunk())
        self.assertTrue(destroyer1.shootAt(9, 9))
        self.assertFalse(destroyer1.isSunk())
		

		#second shot to sink
        self.assertTrue(destroyer1.shootAt(8, 9))
        self.assertTrue(destroyer1.isSunk())
		
		
		
		#SCENARIO 3 - Test that ships do not change status of sunk after being sunk
        destroyer2 = Destroyer()
        row = 5
        column = 5
        horizontal = False
        destroyer2.placeShipAt(row, column, horizontal, self.ocean)
        self.assertFalse(destroyer2.isSunk())
        self.assertTrue(destroyer2.shootAt(5, 5))
        self.assertFalse(destroyer2.isSunk())
        self.assertTrue(destroyer2.shootAt(4, 5))
        self.assertTrue(destroyer2.isSunk())
		#make sure that same shot doesn't ship sunk status
        self.assertFalse(destroyer2.shootAt(5, 5))
        self.assertTrue(destroyer2.isSunk())

    def testToString(self):
        
        battleship = Battleship()
        self.assertEquals("x", battleship.__str__())
		
        row = 9
        column = 1
        horizontal = False
        battleship.placeShipAt(row, column, horizontal, self.ocean)
        battleship.shootAt(9, 1)
        self.assertEquals("x", battleship.__str__())
		
		# Scenario 2 - test a submarine and shoot and sink it
        submarine = Submarine()
        self.assertEquals("x", submarine.__str__()); #test original
		
        row = 9
        column = 9
        submarine.placeShipAt(row, column, horizontal, self.ocean)
        submarine.shootAt(row, column)
        self.assertEquals("s", submarine.__str__())
		
		# Scenario 3 - test a Destroyer and sink it
        destroyer = Destroyer()
        row = 5
        column = 5
        horizontal = True
        destroyer.placeShipAt(row, column, horizontal, self.ocean)
        self.assertEquals("x", destroyer.__str__()); #test original ship state (not sunk)
		
        destroyer.shootAt(row, column); # shoot at it but not sink it
        self.assertEquals("x", destroyer.__str__()); # test that it is still standing "x"
		
        destroyer.shootAt(row, column-1); # shoot at it one more time, sinking it
        self.assertEquals("s", destroyer.__str__()); #testing sink
        


if __name__ == '__main__':
    unittest.main()
