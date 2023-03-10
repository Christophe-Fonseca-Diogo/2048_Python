#####################################
# Project 2048 V.02                  #
# Date : 26.01.2023                 #
# Made by Christophe Fonseca Diogo  #
#####################################

from tkinter import *
import tkinter.font

#########################################
# Window settings                       #
#########################################

window_width = 375
window_height = 375
window = Tk()
window.geometry(f"{window_width}x{window_height}")
window.title("2048 |Christophe Fonseca Diogo| V0.2")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_left = int(screen_width/2 - window_width/2)
y_top = int(screen_height/2 - window_height/2)
window.geometry("+{}+{}".format(x_left, y_top))

#########################################
# Variables                             #
#########################################

movement = 0


#########################################
# Functions                             #
#########################################

def Mix(list, rev):
    for obj in list:
        if 0 in list:
            list.remove(0)
    for obj in range(len(list) - 1):
        if list[obj] == list[obj + 1]:
            list[obj] += list[obj + 1]
            list[obj + 1] = 0
    for obj in list:
        if 0 in list:
            list.remove(0)
    if rev:
        totalNumbers = 4 -len(list)
        while totalNumbers != 0:
            totalNumbers -= 1
            list.insert(0,0)
    else:
        while len(list) < 4:
            list.append(0)
    return list
#########################################
#########################################

def click_on_letter(event):
    if event.keysym == 'Left' or event.keysym == 'a':
        for line in range(len(grid_2048)):
            grid_2048[line] = Mix(grid_2048[line], False)
        objRefresh()
    elif event.keysym == 'Right' or event.keysym == 'd':
        for line in range(len(grid_2048)):
            grid_2048[line] = Mix(grid_2048[line], True)
        objRefresh()


#########################################
# Table for the grid                    #
#########################################

grid_2048= [[2, 2, 2, 2], [4, 0, 128, 0], [256, 32, 2048, 8], [64, 512, 16, 1024]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None],[None, None, None, None]]

#########################################
# Dictionary                             #
#########################################

colors_bg = {2:"#22FF00", 4:"#2B78E4", 8:"#6FA8DC", 16:"#FF9900", 32:"#DDDDDD", 64:"#8518B3", 128:"#C08ED5", 256:"#FF6666", 512:"#45818E", 1024:"#FF00FF", 2048:"#FF0000"}

#########################################
# Grid 2048                             #
#########################################

if __name__ == '__main__':


    def objRefresh():
        for line in range(len(grid_2048)):
            for col in range(len(grid_2048[line])):
                # creation of each label without placing it
                if grid_2048[line][col] != 0:
                    labels[line][col] = tkinter.Label(text=grid_2048[line][col], width=10, height=5, borderwidth=1, relief="solid",
                                                      font=("Arial", 12), bg="yellow")
                else:
                    labels[line][col] = tkinter.Label(text="", width=10, height=5, borderwidth=1, relief="solid",
                                                      font=("Arial", 12), bg="yellow")
                # we set the label in the windows with a virtual grid
                labels[line][col].grid(row=line, column=col)
                try:labels[line][col].config(bg=colors_bg[int(grid_2048[line][col])])
                except:labels[line][col].config(bg="Yellow")
    objRefresh()
window.bind('<Key>', click_on_letter)

window.mainloop()
