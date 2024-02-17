from tkinter import Tk, Label, Button, filedialog, messagebox, Frame
import numpy as np
from library import srmove
import subprocess
import platform

# funciones que sirven para crear label y botones de manera más eficiente,
# asi como crear las funcionalidades que tienen los botones al ser presionados

class create_component(Frame):
    def __init__(self, root):
        super(create_component, self).__init__(root)
        self.root = root
        self.label = []
        self.btn = []
        self.direct = ["", ""]
        self.position_row = 1

    def sum_position(self):
        self.position_row += 1

    def dirs(self, directory_position):
        directory_selected = filedialog.askdirectory(initialdir="~/")
        if directory_selected != ():
            self.direct[directory_position] = directory_selected
            self.label[directory_position + 2].config(text = self.direct[directory_position])

    def create_label(self, text, column):
        if column == 0:
            self.sum_position()

        label = Label(self.root, text=text, font="Arial, 16", pady=8, padx=8, width=38)
        label.grid(row=self.position_row, column=column, sticky="nsew")
        self.label.append(label)

    def config_label(self, label_, font):
        self.label[label_].config(font = font)

    def create_button(self, text, column):
        if column == 0:
            self.sum_position()

        btn = Button(self.root, text=text, width=38)
        btn.grid(row=self.position_row, column=column, pady=8, padx=8)
        self.btn.append(btn)

    def add_directory(self, directory_position, button_press):
        self.btn[button_press].bind("<Button-1>", lambda event: self.dirs(directory_position))

    def execute(self, button_press):
        self.btn[button_press].bind("<Button-1>", lambda event: self.comprobate())

    def open_config(self, button_press):
        self.btn[button_press].bind("<Button-1>", lambda event: self.open_file('config/config.ini'))

    def open_file(self, file):
        opener = "open" if platform.system () == "Darwin" else "xdg-open"

        # Abre el archivo con el programa predeterminado
        subprocess.Popen ([opener, file])
    def comprobate(self):
        if self.direct[0] == "" or self.direct[1] == "":
            messagebox.showwarning("Warning", "Missing Directories Selection")
        else:
            if messagebox.askyesno("Confirmation", "Move " + self.direct[0] + " to " + self.direct[1]):
                srmove_init = srmove.srmove ()
                if srmove_init.start(self.direct[0], self.direct[1]):
                    messagebox.showinfo("Success", "Files Moved Successfully")
                else:
                    messagebox.showwarning("Error", "There Were Errors During Execution")

