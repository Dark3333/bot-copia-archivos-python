import os
import shutil

# Ruta de la carpeta origen
src_folder = input("Ingrese ruta de la carpeta origen: ").strip()

# Nombre de la carpeta nueva
new_folder_name = input("Ingrese nombre de la carpeta destino: ")

# Nombre del archivo
file_name = input("Ingrese el nombre del archivo que contiene el listado de archivos a copiar en la carpeta "+new_folder_name+": ").strip()

# Ruta de la carpeta nueva
dst_folder = './' + new_folder_name

# Crea la carpeta nueva
os.mkdir(dst_folder)

# Lista para guardar las líneas del archivo
lines = []

# Lista para guardar las rutas del archivo
ruta  = []

try:
    # Busca los nombres de los archivos a copiar y los almacena en el array lines.
    with open(file_name, 'r') as file:
        # Lee cada línea del archivo
        for line in file:
            lines.append(line.strip())

    # Recorre la carpeta y subcarpetas
    for root, dirs, files in os.walk(src_folder):

        for archivo in files:

            if archivo in lines:
                # Construye la ruta complta del archivo
                src_file = os.path.join(root, archivo)
                dst_file = os.path.join(dst_folder, archivo)
                # Copia el archivo de la carpeta origen a la nueva
                shutil.copy2(src_file, dst_file)
                # Itera sobre los nombres de archivos

                print(archivo + " se copio exitosamente en la carpeta " + new_folder_name)
        
except:
      print("Valide que los datos ingresados estén correctos.")

input("Oprima cualquier tecla para salir")