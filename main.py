from Ship import Ship
from Battleship import Battleship
from EmptySea import EmptySea
from Cruiser import Cruiser
from Destroyer import Destroyer
from Submarine import Submarine
from Ocean import Ocean


Battleship_instance = Battleship()
Cruiser_instance = Cruiser()
Destroyer_instance = Destroyer()
Submarine_instance = Submarine()


ocean_instance = Ocean()

#ocean_instance.gamePrint()
print()
print()

ocean_instance.placeAllShipsRandomly()



ocean_instance.printWithShips()
ocean_instance.shootAt(0, 0)
print()
print()
ocean_instance.gamePrint()