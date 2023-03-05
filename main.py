import sys
import os
import PySimpleGUI as sg

from data import *

path = ""

def open_img_win(path):
    img = sg.Image(key="-IMG-", size=(60, 20))
    row1 = img
    generate = sg.Button("GENERATE IMAGE")
    row2 = generate
    layout = [[row1], [row2]]
    img_win = sg.Window("Show Image", layout)
    while True:
        event, values = img_win.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "GENERATE IMAGE":
            img_win["-IMG-"].update(path)

def open_text_win():
    text_listbox = sg.Listbox(lb_items2, key="-text_listbox-", size=(60, 20))
    row1 = text_listbox
    layout = [[row1]]
    text_win = sg.Window("Text", layout)
    while True:
        event, values = text_win.read()
        if event == sg.WIN_CLOSED:
            break

lb_items2 = []

#row1
directorys = sg.Text(showdir, key="-direct_key-")
row1 = directorys

#row2
input1 = sg.In(key="-input1-")
row2 = input1 , sg.Button("GO") , sg.Button("BACK"), sg.Button("HOME")

#row3
lb_items = []
for x in os.listdir():
    lb_items.append(x)
listbox = sg.Listbox(lb_items, size=(60, 20),key="-listbox-", enable_events=True)
row3 = listbox

#row4
open_file = sg.Button("OPEN FILE")
radio_text = sg.Radio("TXT", 1, key="-TXT_RADIO-")
radio_img = sg.Radio("IMG", 1, key="-IMG_RADIO-")
row4 = open_file, radio_text, radio_img

#layout
layout = [[row1], [row2], [row3], [row4]]

#functions
def use_window():
    
    window = sg.Window( "OM-Filebrowser 1.0.1" , layout)
    #loop
    while True:
        
        event , values = window.read()
        lb_items = os.listdir()
        window["-listbox-"].update(lb_items)
        
        if event == sg.WIN_CLOSED:
            break
        
        elif event == "GO" and values["-input1-"] != "":
            os.chdir(values["-input1-"])
            window["-direct_key-"].update(os.getcwd())
            window["-input1-"].update("")
            lb_items = os.listdir()
            window["-listbox-"].update(lb_items)
            
        elif event == "BACK":
            os.chdir("..")
            showdir = os.getcwd()
            window["-direct_key-"].update(os.getcwd())
            window["-input1-"].update("")
            lb_items = os.listdir()
            window["-listbox-"].update(lb_items)
            
        elif event == "HOME":
            os.chdir("/home/")
            window["-direct_key-"].update(os.getcwd())    
            lb_items = os.listdir()
            window["-listbox-"].update(lb_items)
            
        elif event == "-listbox-":
            window["-input1-"].update(values["-listbox-"][0])
            
        elif event == "OPEN FILE" and values["-TXT_RADIO-"]:
            f = open(values["-input1-"], "r")
            inhalt = f.readlines()
            for x in inhalt:
                lb_items2.append(x)
            open_text_win()
        elif event == "OPEN FILE" and values["-IMG_RADIO-"]:
            path = values["-input1-"]
            open_img_win(path)

        
def use_terminal():
    
    while True:
    
        in1 = input("->")
        if in1 == "q" or in1 == "quit":            
            print("Bye!")
            break
        
        elif in1.startswith("echo"):
            
            print(in1.replace("echo ", ""))
        elif in1.startswith("cd"):
            
            in1 = in1.replace("cd ", "")
            os.chdir(in1)
        elif in1 == "..":
            
            os.chdir("..")
            print(os.getcwd())
        elif in1 == "home":
            
            os.chdir("/home/")
            print(os.getcwd())
        elif in1 == "pwd":
            
            print(os.getcwd())
        elif in1 == "ls":
            
            print(os.getcwd())
            for x in os.listdir():
                print(x)


if __name__ == "__main__":
    
    #argv decide
    
    if arg1 == "1":
        use_window()
        
    elif arg1 == "0":
        use_terminal()
        
    elif arg1 == "help":
        print("Use 1 or 0 to use OM-Filebrowser")
