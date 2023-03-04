from data import *
import sys
import os
import PySimpleGUI as sg

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

#layout
layout = [[row1],[row2], [row3]]

#functions
def use_window():
    window = sg.Window( "OM-Filebrowser" , layout )
    #loop
    while True:
        event , values = window.read()
        lb_items = os.listdir()
        window["-listbox-"].update(lb_items)
        if event == "Exit" or event == sg.WIN_CLOSED:
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

            
        #window.close()

def use_terminal():
    while True:
        in1 = input("->")
        if in1 == "q" or in1 == "quit ":
            print("Bye!")
            break
        elif in1.startswith("echo"):
            print(in1.trimm("echo "))
        elif in1 == "cd":
            dir_in = input("cd->")
            os.chdir( dir_in )
            print( os.getcwd() )
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
    else:
        print("Use 1 for gui, or 0 for terminal")
