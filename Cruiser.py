from Ship import Ship
class Cruiser(Ship):

    length = 3

    shipType = "cruiser"

    def __init__(self):
        super().__init__(self.length)