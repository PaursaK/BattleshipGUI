from Ship import Ship
from Battleship import Battleship
from EmptySea import EmptySea
from Cruiser import Cruiser
from Destroyer import Destroyer
from Submarine import Submarine
from Ocean import Ocean
from tkinter import *
from copy import *

def main_terminal_play():
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

def main_GUI_play():

    #create window object
    window = Tk()
    #create title for window object
    window.title("===BATTLESHIP===")

    #ocean array
    ocean_original = Ocean()
    ocean_original.placeAllShipsRandomly()
    ocean_copy = [[0 for i in range(10)] for j in range(10)]


    #create label for shots fired and hit count
    label_shots = Label(text = "Shots Fired: " + str(ocean_original.getShotsFired()), font = ("consolas", 20))
    label_shots.pack(side = "top")
    label_sunkShips = Label(text="Ships Sunk: " + str(ocean_original.getShipsSunk()), font=("consolas", 20))
    label_sunkShips.pack(side = "top")

    #create reset button
    reset_button = Button(text = "restart", font = ("consolas", 20), command = new_game)
    reset_button.pack(side="top")

    #create frame for buttons
    frame = Frame(window)
    frame.pack()

    #create a button for each empty ship in the array
    for row in range(10):
        for column in range(10):
            ocean_copy[row][column] = Button(frame, text = '', font=('consolas', 20), width = 2, height = 2,
                                                        command = lambda row = row, column = column: next_turn(label_shots, label_sunkShips, ocean_copy, ocean_original, row, column))

            ocean_copy[row][column].grid(row = row, column = column)

    #create the window to play in
    window.mainloop()


def new_game():
    main_GUI_play()




def next_turn(label_shots, label_sunkShips, ocean_copy, ocean_original, row, column):

    #while game is not over allow click to occur
    if(ocean_original.isGameOver() is False):

        #take use the click coordinates to fire a shot at the ships
        ocean_original.shootAt(row,column)
        #set the text of the button on the ocean copy array to the ship __str__ return value
        ocean_copy[row][column]['text'] = ocean_original.getShipArray()[row][column]

        #update the labels for shots and sunk Ships
        label_shots.config(text = "Shots Fired: " + str(ocean_original.getShotsFired()))
        label_sunkShips.config(text="Ships Sunk: " + str(ocean_original.getShipsSunk()))

    #iterate over the rows of the ocean array
    for i in range(len(ocean_original.getShipArray())):
        # iterate over the columns of the ocean array
        for j in range(len(ocean_original.getShipArray()[i])):
            #if a ship is sunk, then update all the buttons that share that ship object
            #with the updated __str__ signature ('s')
            if ocean_original.getShipArray()[i][j].isSunk():
                ocean_copy[i][j].config(text = ocean_original.getShipArray()[i][j])


if __name__ == '__main__':
    main_GUI_play()





