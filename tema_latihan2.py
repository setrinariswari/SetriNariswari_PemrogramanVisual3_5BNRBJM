import PySimpleGUI as sg

layout = [
    [sg.Text('NPM       : 2310010684',  text_color='blue', background_color='red')],
    [sg.Text('Nama      : SETRI NARISWARI', text_color='blue', background_color='red')],
    [sg.Text('Kelas     : 5B Non Reguler Banjarmasin', text_color='blue', background_color='red')],
    [sg.Text('Matkul    : Pemrograman Visual 3', text_color='blue', background_color='red')]
]

window = sg.Window('Profile', layout, background_color='red', size=(400,200))
window()
window.close()