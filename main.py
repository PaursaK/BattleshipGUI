from Ship import Ship
from Battleship import Battleship
from EmptySea import EmptySea
from Cruiser import Cruiser
from Destroyer import Destroyer
from Submarine import Submarine
from Ocean import Ocean

#welcome statement
print("======[Welcome to Battlship!]======")
print()

#create ocean instance and place ships to generate gameboard
ocean_instance = Ocean()
ocean_instance.placeAllShipsRandomly()

turnCount = 1

#setup up game loop
while(True):

    #print turn label and gameboard every turn that is taken
    print("======" + f'[Turn: {turnCount}]'+ "======")
    ocean_instance.gamePrint()
    print()

    #get input from user
    row = int(input("Please enter a row: "))
    column = int(input("Please enter a column: "))

    #use user inputted row and column to check whether their strike lands
    #if so, let the user know, if that hit sinks the ship, let the user know that as well
    if(ocean_instance.shootAt(row, column)):
        print("We have a hit!")
        if(ocean_instance.getShipArray()[row][column].isSunk()):
            print("We have sunk a " + ocean_instance.getShipArray()[row][column].getShipType())

    #if the shot misses, let user know
    else:
        print("Miss!")

    #check if game is over after each turn
    if(ocean_instance.isGameOver()):
        print()
        print(f"Game over! It took you: {ocean_instance.getShotsFired()} shot(s) to sink all the ships!")
        break

    #increment turn count
    turnCount +=1
    print()







