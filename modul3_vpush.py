import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAB",font=("helvetica",24))],
         [sg.Text("BANJARMASIN",font=("Courier",18))]]
window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   element_justification = "center",
                   size=(430,200))

window.read()
window.close()