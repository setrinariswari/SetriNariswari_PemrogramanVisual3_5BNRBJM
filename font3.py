import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25,"italic","bold","underline"))],
[sg.Text("NPM : 2310010684 ")],
[sg.Text("Nama : SETRI NARISWARI ")],
[sg.Text("Kelas : 5B Non Reguler Banjarmasin ")]
],
size=(510,200),
font=("Times", 18))
window()
window.close()