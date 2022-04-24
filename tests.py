import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')],[sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('36')],
          [sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('37')],
          [sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('38')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])


window.close()
