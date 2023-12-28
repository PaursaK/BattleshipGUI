from Ship import Ship
class EmptySea(Ship):

    # INSTANCE VARIABLES
    length = 1

    shipType = "empty"

    def __init__(self):
        '''calls super constructor and initializes emptysea object with a length of one'''
        super().__init__(self.length)

    def shootAt(self, row, column):
        '''this method overrides shootAt from parent class Ship. It always
        returns False to indicate that nothing was hit
        :param: row, column
        :return: returns False(always)'''
        self.getHitArray()[0] = True
        return False

    def isSunk(self):
        '''overrides the isSunk method from parent class Ship. It always
        returns false indicating that a player did not sink any tnagible ship
        :return: False (always)'''
        return False

    def __str__(self):
        '''returns a single character String representing the empty sea object when fired upon.
        indicates that nothing was hit since it is an empty sea object.
        return: "-" for empty sea objects'''
        return "-"
