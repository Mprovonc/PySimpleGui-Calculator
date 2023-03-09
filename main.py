from random import random
from venv import create
import PySimpleGUI as sg

# GUI window with buttons and input window along with customizations and coloring
def createWindow(theme):
    sg.theme(theme)
    sg.set_options(font = 'Helvetica 14', button_element_size = (6, 2))
    buttonSize = (6,2)   
    layout = [
        [sg.Text(
        '',
        font = 'Helvetica 40',
        justification = 'right',
        expand_x = True, pad = (10, 20),
        right_click_menu = themeMenu,
        key = '-TEXT-')
        ],
        [sg.Button('Clear', expand_x = True), sg.Button('Enter', expand_x = True)],
        [sg.Button(7, size = buttonSize), sg.Button(8, size = buttonSize), sg.Button(9, size = buttonSize), sg.Button('*', size = buttonSize)],
        [sg.Button(4, size = buttonSize), sg.Button(5, size = buttonSize), sg.Button(6, size = buttonSize), sg.Button('/', size = buttonSize)],
        [sg.Button(1, size = buttonSize), sg.Button(2, size = buttonSize), sg.Button(3, size = buttonSize), sg.Button('-', size = buttonSize)],
        [sg.Button(0, expand_x = True), sg.Button('.', size = buttonSize), sg.Button('+', size = buttonSize)]
    ]    

    return sg.Window('Calculator', layout)

# Theme/color changing option      
themeMenu = ['menu', ['LightGrey1', 'dark', 'DarkGrey8', 'random']]
window = createWindow('dark')

currentNum = []
fullOperation = []

while True:
    
    # Window open and close
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in themeMenu[1]:
        window.close()
        window = createWindow(event)

    # Number button activation
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        currentNum.append(event)
        numString = ''.join(currentNum)
        window['-TEXT-'].update(numString)

    # Operator button activation
    if event in ['+', '-', '/', '*']:
        fullOperation.append(''.join(currentNum))
        currentNum = []
        fullOperation.append(event)  
        window['-TEXT-'].update('')     
    
    # Enter button activation
    if event == 'Enter':
        fullOperation.append(''.join(currentNum))
        result = eval(' '.join(fullOperation))
        window['-TEXT-'].update(result)
        fullOperation = []

    # Clear button activation
    if event == 'Clear':
        currentNum = []
        fullOperation = []
        window['-TEXT-'].update('')

window.close()