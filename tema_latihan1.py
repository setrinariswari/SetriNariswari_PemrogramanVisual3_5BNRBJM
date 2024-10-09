import PySimpleGUI as sg
sg.theme_text_color('blue')
window = sg.Window(title="Profile",
layout=[
    [sg.Text("NPM       : 2310010684")],
    [sg.Text("Nama      : Setri Nariswari")],
    [sg.Text("Kelas     : 5B Non Reguler Banjarmasin")],
    [sg.Text("Matkul    : Pemrograman Visual 3")]
],
size=(400,200), 
background_color='red')
window()
window.close()