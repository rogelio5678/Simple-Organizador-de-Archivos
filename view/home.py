from tkinter import Tk

import numpy as np
from library import create_component


#Crear los labels y botones utilizando la clase create_component asi como asignar las funcionalidades a los botones
def show():
    root = Tk()
    root.title("OrganizerPYou")
    cc = create_component.create_component(root)

    #Create labels 0
    cc.create_label("Old folder", 0)
    #Create label 1
    cc.create_label("New Folder", 1)
    #Create label 2
    cc.create_label("No selected directory", 0)
    cc.config_label(2, "Arial 10")
    #Create label 3
    cc.create_label("No selected directory", 1)
    cc.config_label(3, "Arial 10")

    #Create button 0
    cc.create_button("Old Directory", 0)
    cc.add_directory(0, 0)
    #Create button 1
    cc.create_button("New Directory", 1)
    cc.add_directory(1, 1)
    #Create button 2
    cc.create_button("Start", 0)
    cc.execute(2)
    #Create button 3
    cc.create_button("Config", 1)
    cc.open_config(3)


    root.resizable(width=False, height=False)

    root.mainloop()
