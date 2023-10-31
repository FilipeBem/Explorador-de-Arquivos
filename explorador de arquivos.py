import os
import PySimpleGUI as sg

sg.theme('DarkTeal9')

layout = [[sg.Text('Folder'), sg.InputText(), sg.FolderBrowse()],
          [sg.Listbox(values=[], size=(60, 20), key='-FILE LIST-')],
          [sg.Button('Open'), sg.Button('Cancel')],
          [sg.Image(key='-IMAGE-', size=(10, 10), enable_events=True, right_click_menu=None, background_color=None, pad=None, metadata=None)]]

window = sg.Window('File Explorer', layout, resizable=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    folder = values[0]
    try:
        file_list = os.listdir(folder)
    except:
        file_list = []
    window['-FILE LIST-'].update(file_list)
    if event == 'Open':
        if values['-FILE LIST-']:
            filename = values['-FILE LIST-'][0]
            os.subprocess(os.path.join(folder, filename))
    elif event == '-FILE LIST-':
        if values['-FILE LIST-']:
            filename = values['-FILE LIST-'][0]
            image = sg.Image(filename=filename, size=(10, 10))
            window['-IMAGE-'].update(data=image.get_data())

window.close()