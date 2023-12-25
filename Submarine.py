from Ship import Ship
class Submarine(Ship):

    length = 1

    shipType = "submarine"

    def __init__(self):
        super().__init__(self.length)