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
    '''
    original terminal play version of battleship, used mainly as a template for the GUI design but still
    usable. creates an ocean instance and allows for user input via keyboard entry for coordinates to strike
    hidden ships
    :return:N/A
    '''
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


def new_game():
    '''this function looks to restart the game board for a new game.
    It accesses global game board components like labels and ocean game board array and
    re-initializes them in reference to a new Ocean instance.
    :param: N/A
    :return:N/A
    '''

    #address all variables that need to updated upon restarting the game
    global ocean_original
    global ocean_copy
    global label_shots
    global label_sunkShips
    global label_shotUpdate

    #initialize a new ocean board
    ocean_original = Ocean()
    ocean_original.placeAllShipsRandomly()

    #iterate over the ocean 10x 10 array and reset all the button text to a empty string
    for row in range(len(ocean_original.getShipArray())):
        for column in range(len(ocean_original.getShipArray()[row])):
            ocean_copy[row][column].config(text = "", font =('consolas', 20))

    # update the labels for shots, shotUpdate and sunk Ships
    label_shots.config(text="Shots Fired: " + str(ocean_original.getShotsFired())) #should be initialized to 0
    label_sunkShips.config(text="Ships Sunk: " + str(ocean_original.getShipsSunk())) #should be initialized to 0
    label_shotUpdate.config(text = "") #should be set to an empty string






def next_turn(row, column):
    '''
    called when the tkinter library receives input from the user via mouse clicks on the game board.
    it checks if the game is over, if not, will map shots fired via mouse clicks to the internal game board of ships
    found in the 10x10 array. If a shot lands on a hidden ship, an "x" appears and if the shot sinks a ship the entire
    ship is shown as "s". As shots are fired, the shots fired label gets updated and as ships are sunk the ships sunk label
    is updated. Addresses the 4 global variables necessary for manipulating the GUI: label for shots, ships sunk and the
    internal ocean array and the ocean button array that is tied to the internal ocean array
    :param row: row in the ocean array
    :param column: column in the ocean array
    :return: N/A
    '''
    global ocean_original
    global ocean_copy
    global label_shots
    global label_sunkShips
    global label_shotUpdate

    #while game is not over allow click to occur
    if(ocean_original.isGameOver() is False):

        #take use the click coordinates to fire a shot at the ships
        if ocean_original.shootAt(row,column):
            label_shotUpdate.config(text = "We have a hit!")

            #check if ship is sunk, if so update user with type of ship sunk
            if ocean_original.getShipArray()[row][column].isSunk():
                label_shotUpdate.config(text=f"You have sunk a {ocean_original.getShipArray()[row][column].getShipType()}")
        #if we hit an empty sea object let user know they missed
        else:
            label_shotUpdate.config(text="Missed..")

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

    #when the game is over
    else:
        #create game over after player wins
        game_over = "GAME OVER!"

        # iterate over the rows of the ocean array
        for i in range(len(ocean_original.getShipArray())):
            # iterate over the columns of the ocean array
            for j in range(len(ocean_original.getShipArray()[i])):

                #if the row is equal to 4, start printing the GAME OVER on the buttons
                if i == 4:
                    ocean_copy[i][j].config(text=game_over[j], font = ('consolas', 40))
                else:
                    ocean_copy[i][j].config(text="")







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

# create update label for updating the user on what each shot means
label_shotUpdate = Label(text="", font=("consolas", 20))
label_shotUpdate.pack(side="bottom")


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
                                                    command = lambda row = row, column = column: next_turn(row, column))

        ocean_copy[row][column].grid(row = row, column = column)

#create the window to play in
window.mainloop()






