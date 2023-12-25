from Ship import Ship
class Battleship(Ship):

    length = 4

    shipType = "battleship"

    def __init__(self):
        super().__init__(self.length)
