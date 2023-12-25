from Ship import Ship
class Destroyer(Ship):

    length = 2

    shipType = "destroyer"

    def __init__(self):
        super().__init__(self.length)