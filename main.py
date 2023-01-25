import os
import shutil

# Ruta de la carpeta origen
src_folder = input("Ingrese ruta de la carpeta origen: ")

# Nombre de la carpeta nueva
new_folder_name = input("Ingrese nombre de la carpeta destino: ")

# Ruta de la carpeta nueva
dst_folder = './' + new_folder_name

# Crea la carpeta nueva
os.mkdir(dst_folder)

# Nombre del archivo
file_name = 'list.txt'

# Lista para guardar las líneas del archivo
lines = []

# Busca los nombres de los archivos a copiar y los almacena en el array lines.
with open(file_name, 'r') as file:
    # Lee cada línea del archivo
    for line in file:
        lines.append(line.strip())


#file_names = ['text1.txt', 'text2.txt', 'text3.txt']

# Itera sobre los nombres de archivos
for file_name in lines:
    # Construye la ruta completa del archivo
    src_file = os.path.join(src_folder, file_name)
    dst_file = os.path.join(dst_folder, file_name)
    # Copia el archivo de la carpeta origen a la nueva
    shutil.copy2(src_file, dst_file)

print("Los archivos han sido copiados exitosamente en la carpeta " + new_folder_name)