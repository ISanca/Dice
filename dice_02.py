import PySimpleGUI as sg
import random

MIN = 1
MAX = 6
x = range(1, 21)
dice_buttons = []

for i in x:
    dice_buttons.append(sg.Button(str(i)))

layout = [[sg.Slider(range=(1, 10), orientation='h', size=(34, 20), default_value=1, key='SLIDER')],
          dice_buttons,
          [sg.Button('Exit')],
          [sg.Text("Ide jön majd...", size=(40, 1), key='TEXT')]]

window = sg.Window('Dice roller', layout, resizable=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    button_events = map(str, x)

    if event in button_events:
        rolls = []
        for i in range(1, int(event) + 1):
            rolls.append(random.randint(MIN, MAX))

        success = rolls.count(5) + rolls.count(6)
        target = values['SLIDER']
        print(f'Target: {target} - Success: {success}')
        evaluation = ''
        if target <= success:
            evaluation = 'success'
        else:
            evaluation = 'failure'

        window['TEXT'].update(f'{evaluation} - {rolls}')

window.close()
