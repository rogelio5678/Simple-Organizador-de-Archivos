import sys
import os
from sos.options import str_to_bool
from library import formats
import datetime
import configparser

# aqui esta el script que se encarga de mover los archivos y organizarlos
# en su nueva ubicación dependediendo su extensión
class srmove:
    def __init__(self):
        self.all_ok = True
        self.sub_folder = False
        self.replace = False
        self.read_config()
        self.create_folder('logs')
        self.file_log = open ("logs/" + str (datetime.datetime.now ()) + ".log", "w")

    def read_config(self):
        config = configparser.ConfigParser ()
        with open ('config/config.ini', 'r') as config_file:
            config.read_file (config_file)

        self.subfolder = str_to_bool(config.get ('CONFIG', 'subfolder'))
        self.replace = str_to_bool(config.get ('CONFIG', 'replace'))


    def move_file(self, file_new_route, file_route, extension):
        counter = 1
        try:
            while True:
                if not self.replace:
                    if not os.path.exists (file_new_route):
                        os.rename (file_route, file_new_route)
                        counter = 1
                        break
                    else:
                        if extension != "":
                            file_new_new_route = file_new_route.replace (extension,
                                                                         f"({counter}){extension}")
                        else:
                            file_new_new_route = f"{file_new_route}({counter})"

                        if not os.path.exists (file_new_new_route):
                            file_new_route = file_new_new_route
                        counter += 1

                else:
                    os.rename (file_route, file_new_route)
                    break
            self.capture_logs (f"Success move file to {file_new_route}")

        except KeyboardInterrupt:
            print("Canceled")

        except:
            self.capture_logs (f"Error move file to {file_new_route}")
            self.all_ok = False

    def capture_logs(self, message):
        print (message)
        self.file_log.write (f"{message}\n")

    def create_folder(self, new_route):
        if os.makedirs (new_route, exist_ok=True):
            self.capture_logs (f"Create Directory {new_route} success")

    def start(self, folder, new_folder):
        if not os.path.isdir(folder):
            print('ubicacion invalida')
            return False

        count = 0

        for root, dirs, files in os.walk (folder):
            if len (os.listdir (root)) != 0:
                if not self.sub_folder:
                    if folder != root:
                        continue

                for file in files:
                    count += 1
                    file_route = f"{root}/{file}"
                    extension = os.path.splitext (file)[1]
                    extension_check = os.path.splitext (file)[1].replace (".", "").upper ()
                    group_folder = ""

                    for name_folder, list_extension in formats.folders_names.items ():
                        if extension_check in list_extension:
                            group_folder = name_folder

                    if group_folder == "":
                        group_folder = "OtherFormats"

                    new_route = f"{new_folder}/{group_folder}/{extension_check}"
                    file_new_route = f"{new_route}/{file}"

                    if extension != "":
                        self.capture_logs (f"Move file {file} to {new_route}")
                        self.create_folder (new_route)
                        self.move_file (file_new_route, file_route, extension)

                    else:
                        new_route = f"{new_folder}/empty_extension"
                        file_new_route = f"{new_route}/{file}"

                        self.capture_logs (f"Move file {file} to {new_route}")
                        self.create_folder (new_route)
                        self.move_file (file_new_route, file_route, extension)

        self.file_log.close ()
        return self.all_ok
