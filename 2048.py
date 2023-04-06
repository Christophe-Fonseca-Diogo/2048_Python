#####################################
# Project 2048 V.03                 #
# Date : 26.01.2023                 #
# Made by Christophe Fonseca Diogo  #
#####################################

from tkinter import *
import tkinter.font
import random
from tkinter import messagebox

#########################################
# Table for the grid                    #
#########################################

grid_2048 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

#########################################
# Dictionary  for the colors            #
#########################################

colors_bg = {2: "#22FF00", 4: "#2B78E4", 8: "#6FA8DC", 16: "#FF9900", 32: "#DDDDDD", 64: "#8518B3", 128: "#C08ED5",
             256: "#FF6666", 512: "#45818E", 1024: "#FF00FF", 2048: "#FF0000"}

#########################################
# Variables                             #
#########################################

movement = 0
win = 2048
window = Tk()
score = 0


#########################################
# Window settings                       #
#########################################

# This function is all the settings about the window.
# In the top frame there's the title "2048 by Christophe", the score and the movement
# In the middle frame there's the grid
# In the bottom frame there's the button for restarting a game

def display_window():
    global middle_frame, score_show_textvar, movement_show_textvar
    window_width = 400
    window_height = 550
    window.geometry(f"{window_width}x{window_height}")
    window.title("2048 |Christophe Fonseca Diogo| V0.3")

    # When the game start the game pop up in the middle of the screen.
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_left = int(screen_width / 2 - window_width / 2)
    y_top = int(screen_height / 2 - window_height / 2)
    window.geometry("+{}+{}".format(x_left, y_top))

    # For not resizing the windows, because if we resize the window the interface gonna not be like wanted
    window.resizable(False, False)
    # ALL THE GRAPHIC PART #
    window.config(bg="#ea9999")

    main_frame = Frame(window, bg="#ea9999")
    main_frame.pack(padx=20, pady=20, fill=BOTH)

    top_frame = Frame(window, bg="#ea9999")
    top_frame.pack(fill=X)

    title = Label(top_frame, text="2048 by Christophe", font="Arial, 30", bg="#ea9999", borderwidth=5, relief="groove")
    title.pack(anchor=N)

    middle_frame = Frame(window, bg="Cyan", borderwidth=5, relief="groove")
    middle_frame.pack()

    bottom_frame = Frame(window)
    bottom_frame.pack()

    # This is for the score in the window
    score_show_textvar = StringVar()
    score_show_textvar.set("Score: " + str(score))
    score_show = Label(top_frame, textvariable=score_show_textvar, font="Arial, 15", bg="#ea9999", borderwidth=5,
                       relief="flat")
    score_show.pack(side=LEFT)

    # This is for the movement in the window
    movement_show_textvar = StringVar()
    movement_show_textvar.set("Mouvements: " + str(movement))
    movement_show = Label(top_frame, textvariable=movement_show_textvar, font="Arial, 15", bg="#ea9999", borderwidth=5,
                          relief="flat")
    movement_show.pack(side=RIGHT)

    # It's how the button is created and i call the function reset.
    button_restart = tkinter.Button(bottom_frame, text="Recommencer", command=reset_game, borderwidth=5,
                                    relief="groove", bg="#ea9999")
    button_restart.pack()
    # The functions for the game
    obj_refresh()
    generate_random_value()
    window.bind('<Key>', click_on_letter)


#########################################
# Functions for delete the 0            #
#########################################
def delete_zeros(list, rev):
    # Determine the starting index for iterating through the list
    if not rev:
        i = len(list) - 1
        while i != 0 and list[i] == 0:
            i -= 1
    else:
        i = 0
        while i < len(list) and list[i] == 0:
            i += 1
    # Remove all zeros from the list using the remove() method
    for obj in list:
        if 0 in list:
            list.remove(0)


#########################################
# Function for mix the grid             #
#########################################


def mix(list, rev):
    # Declare global variables used in this function
    global movement, score
    delete_zeros(list, rev)
    # Iterate through the list and merge adjacent equal values
    for obj in range(len(list) - 1):
        if list[obj] == list[obj + 1]:
            # Merge adjacent equal values and update the score
            list[obj] += list[obj + 1]
            score += list[obj]
            score_show_textvar.set("Score: " + str(score))
            # Count the number of movements made to merge the values
            movement += 1
            # Set the value of the next element to zero
            list[obj + 1] = 0

    delete_zeros(list, rev)
    # If rev is True, add zeros to the beginning of the list
    if rev:
        totalnumbers = 4 - len(list)
        while totalnumbers != 0:
            totalnumbers -= 1
            list.insert(0, 0)
    # If rev is False, add zeros to the end of the list
    else:
        while len(list) < 4:
            list.append(0)
    # Return the modified list
    return list


#########################################
# Functions when the user presses a keybind
#########################################


def click_on_letter(event):
    global score
    prev_positions_value = [row[:] for row in grid_2048]
    # If the user presses the Left key or the key "a" the grid will mix to the Left
    if event.keysym == 'Left' or event.keysym == 'a':
        for line in range(len(grid_2048)):
            grid_2048[line] = mix(grid_2048[line], False)
        # Refresh the grid
        obj_refresh()
    # If the user presses the Right key or the key "d" the grid will mix to the Left
    elif event.keysym == 'Right' or event.keysym == 'd':
        for line in range(len(grid_2048)):
            grid_2048[line] = mix(grid_2048[line], True)
        # Refresh the grid
        obj_refresh()
    # If the user presses the Up key or the key "w" the grid will mix to the Left
    elif event.keysym == 'Up' or event.keysym == 'w':
        for col in range(len(grid_2048)):
            column = [grid_2048[line][col] for line in range(len(grid_2048))]
            mix_column = mix(column, False)
            for line in range(len(grid_2048)):
                grid_2048[line][col] = mix_column[line]
        # Refresh the grid
        obj_refresh()
    # If the user presses the Down key or the key "s" the grid will mix to the Left
    elif event.keysym == 'Down' or event.keysym == 's':
        for col in range(len(grid_2048)):
            column = [grid_2048[line][col] for line in range(len(grid_2048))]
            reversed_column = column[::-1]
            mix_column = mix(reversed_column, False)
            for line in range(len(grid_2048)):
                grid_2048[line][col] = mix_column[::-1][line]
        # Refresh the grid
        obj_refresh()
    movement_show_textvar.set("Mouvements: " + str(movement))
    if grid_2048 != prev_positions_value:
        changerandomvalue()
    else:
        table_state()


def table_state():
    empty_positions = []
    # For each row we are going to search in the table for a value that's equal to 2048, otherwise, we'll just create a
    # temporal table with all the available cases.
    for i in range(4):
        if 2048 in grid_2048[i]:
            answer = messagebox.askquestion(title="Felicitation !", message="Vous avez gagné ! On recommence ?")
            print(answer)
            if answer == "yes":
                reset_game()
                obj_refresh()
            else:
                quit()
            return "Other"
        for j in range(4):
            if grid_2048[i][j] == 0:
                empty_positions.append((i, j))
    # If there are no available cases then we will check if the user can still move otherwise he lost.
    if len(empty_positions) == 0:
        # There are no empty spaces, we'll test movements.
        movable = movement_checker()
        if movable:
            return "Other"
        else:
            answer = messagebox.askquestion(title="Dommage tu as perdu", message="On recommence ?")
            if answer == "yes":
                reset_game()
                obj_refresh()
            else:
                quit()
            return "Other"
    else:
        return "Space"


# Imitates the mix function but without doing any changes to the table, just simulating it so we can see if there are
# available moves.
def movement_checker():
    for row in range(4):
        for col in range(4):
            if grid_2048[row][col] == 0:
                return True
            if row < 4 - 1 and grid_2048[row][col] == grid_2048[row + 1][col]:
                return True
            if col < 4 - 1 and grid_2048[row][col] == grid_2048[row][col + 1]:
                return True
    return False


# This function asks to the "table_state" if there are any available spaces to insert a random number (2 or 4).
def changerandomvalue():
    while True:
        random_pos_row, random_pos_col = random.randint(0, len(grid_2048) - 1), random.randint(0, len(grid_2048[0]) - 1)
        state = table_state()
        if state == "Space":
            if grid_2048[random_pos_row][random_pos_col] == 0:
                grid_2048[random_pos_row][random_pos_col] = random.choice(
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) * 2  # The number "4" has only 10 % of chance to be generated
                obj_refresh()  # Go to "position refresh" function
                break
            else:
                pass
        else:
            break


# Generate 2 numbers everytime it's initialised
def generate_random_value():
    i = 2
    while i != 0:
        i -= 1
        changerandomvalue()


# It refreshes all the cases to display any changes.
def obj_refresh():
    for line in range(len(grid_2048)):
        for col in range(len(grid_2048[line])):
            # creation of each label without placing it
            if grid_2048[line][col] != 0:
                labels[line][col] = tkinter.Label(middle_frame, text=grid_2048[line][col], width=10, height=5,
                                                  borderwidth=1, relief="solid",
                                                  font=("Arial", 12), bg="yellow")
            else:
                labels[line][col] = tkinter.Label(middle_frame, text="", width=10, height=5, borderwidth=1,
                                                  relief="solid",
                                                  font=("Arial", 12), bg="yellow")
            # we set the label in the windows with a virtual grid
            labels[line][col].grid(row=line, column=col)
            try:
                labels[line][col].config(bg=colors_bg[int(grid_2048[line][col])])
            except:
                labels[line][col].config(bg="Yellow")


# This definition clear the grid, clear the movement and the score.
# For the next game the scores and the movements are going to be 0
def reset_game():
    global grid_2048, score, movement
    grid_2048.clear()
    score = 0
    movement = 0
    score_show_textvar.set("Score: " + str(score))
    movement_show_textvar.set("Mouvements: " + str(movement))
    grid_2048 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    generate_random_value()
    obj_refresh()


#########################################
# Grid 2048                             #
#########################################

if __name__ == '__main__':
    display_window()
    # For the window of the game
    window.mainloop()
