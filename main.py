#!/bin/python
from view import home
import numpy as np
from sys import argv
from library import srmove


# para ejecutar el programa desde linea de comandos se necesita pasar la ubicación antigua
# y la nueva ubicación como parametros
if len(argv) == 3:
    old_folder = argv[1]
    new_folder = argv[2]
    srmove_init = srmove.srmove()
    srmove_init.start(old_folder, new_folder)

# si no se pasan dos paramtros se ejecuta la interfaz grafica
elif __name__ == '__main__':
    home.show()



