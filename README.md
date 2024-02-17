# Simple-Organizador-de-Archivos
  Este programa le ayudara a organizar sus archivos en carpetas y subcarpetas dependiendo el tipo de archivo.

# Requisitos
   * Python 3.x
   
# Clonar repositorio 
  git clone https://github.com/rogelio5678/Simple-Organizador-de-Archivos.git

# Línea de comandos 
  * cd Simple-Organizador-de-Archivos/
  * Para ejecutar el programa simplemente desde linea de comando debe pasar dos parametros uno correspondiente al directorio donde estan los archivos a organizar y otro para el nuevo directorio a donde se moveran los archivos organizados, recuerde pasar la ruta absoluta de la carpeta.
* Ejemplo:
     - python main.py /user/old_directory/ ~/Documentos/new_directory
# Interfaz gráfica
  * cd Simple-Organizador-de-Archivos/
  * Para la interfaz gráfica unicamente ejecute el programa sin argumentos
  * Ejemplo:
    - python main.py
   
# Configuración
  * Puede abrir el archivo de configuración ubicado en "config/config.ini" con cualquier editor de texto.
  *  Ejemplo en cli linux
    - nano config/config.ini
  * Solo lo hay dos opciones la cuales son "subfolder" por defecto es "False" ("True" para habilitar), esta opcion habilita/deshabilita buscar archivos en los subdirectorios del directorio pasado, la otra opción es "replace" por defecto es False ("True" para habilitar), la cual sirve para saber si remplazar archivos con el mismo nombre o renombrarlos con el mismo nombre simple agregando un distintivo para que el nombre no sea igual.

# Imagenes de Ejemplo
  * Carpetas organizadas por tipo de archivo 
![image](https://github.com/rogelio5678/Simple-Organizador-de-Archivos/assets/99551747/a02ae5ca-c005-4c25-af61-8075bbaaa263)
  * Archivos organizados por extensión
    ![image](https://github.com/rogelio5678/Simple-Organizador-de-Archivos/assets/99551747/d045781b-901b-4eb1-b812-4ce868a6575b)


  


