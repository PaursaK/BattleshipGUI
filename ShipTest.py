import unittest
from EmptySea import *
from Battleship import *
from Cruiser import *
from Destroyer import *
from Submarine import *
from Ocean import *

###IN PROGRESS###

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
        pass

    def testPlaceShipAt(self):
        pass

    def testShootAt(self):
        pass

    def testIsSunk(self):
        pass
    
    def testToString(self):
        pass


if __name__ == '__main__':
    unittest.main()
