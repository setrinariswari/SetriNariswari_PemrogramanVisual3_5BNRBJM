import PySimpleGUI as sg

window = sg.Window(title="Profile", layout=[[sg.Text('NPM    :'), sg.Text('2310010684')],
    [sg.Text('Nama   :'), sg.Text('Setri Nariswari')],
    [sg.Text('Kelas   :'), sg.Text('5B Non Reguler Banjarmasin')],
    [sg.Text('Matkul  :'), sg.Text('Pemrograman Visual 3')],], size=(400, 200))
window()
window.close()