from Ship import Ship
class Submarine(Ship):

    # INSTANCE VARIABLES
    length = 1

    shipType = "submarine"

    def __init__(self):
        super().__init__(self.length)