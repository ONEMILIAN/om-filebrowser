import PySimpleGUI as sg
# from openpyxl import Workbook
# from openpyxl import load_workbook

createColony_Layout=[]
firstWindow_Layout=[]
colonyList = []
# Software theme

# FIRST WINDOW
# Layouts
menuBar_Layout = [
                    ['&File', ['&Inserisci file ICM     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                    ['&Edit', ['Undo']],
                    ['&Toolbar', ['---', 'Command &1::Command_Key', 'Command &2', '---', 'Command &3', 'Command &4']],
                    ['&Help', ['&About...']]
                 ]

createColony_Layout = [
                        [sg.Text('Insert researcher name', size=20)],
                        [sg.Input(size=15, key='c')],
                        [sg.Button(button_text='Create', button_type=7)]
                      ]

createColonyFrame = sg.Frame('Create new colony', createColony_Layout, size=(200, 100))

firstWindow_Layout = [
                        [sg.MenubarCustom(menuBar_Layout)],
                        [sg.Push(), sg.Text('Colony management',
                        justification=('Center'), font=('Helvetica', 30)), sg.Push()],
                        [createColonyFrame],
                        [sg.Listbox(colonyList, size =(50, 25), key='lista')]
                     ]

# Create window
window = sg.Window('Colony management', firstWindow_Layout, size=(1300, 700),
                   auto_size_text= True, resizable=True, finalize=True)
window.set_min_size((500, 250))
# window.TKroot.minsize(500,250)
#window.TKroot.maxsize(600, 700)

# Program loop
while True:
        event,values = window.read()

        if event == 'Create':
            window['lista'].update((values['c'],))


        if event == sg.WINDOW_CLOSED:
           break

window.close()
