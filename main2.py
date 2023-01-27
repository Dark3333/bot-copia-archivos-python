import os

# Ruta de la carpeta a buscar
root_folder = 'folder'

# Lista para guardar los archivos encontrados
txt_files = []

# Recorre la carpeta y subcarpetas
for root, dirs, files in os.walk(root_folder):

    for file in files:
        if file.endswith(".txt"):
            print(file)

            txt_files.append(os.path.join(root, file))
        

print(txt_files)