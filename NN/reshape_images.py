from PIL import Image
import os


# Elige el directorio principal donde se encuentran las carpetas
root_dir = 'data/'

# Define el tamaño deseado de la imagen
new_size = (256, 256)

# Recorre las carpetas
for folder in os.listdir(root_dir):
    if folder.isdigit():  # Solo procesa carpetas numéricas
        folder_path = os.path.join(root_dir, folder)
        
        # Recorre las imágenes en cada carpeta
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Abre la imagen
            with Image.open(file_path) as im:
                
                # Recorta la imagen a un cuadrado
                width, height = im.size
                square_size = min(width, height)
                left = (width - square_size) / 2
                top = (height - square_size) / 2
                right = (width + square_size) / 2
                bottom = (height + square_size) / 2
                im = im.crop((left, top, right, bottom))
                
                # Redimensiona la imagen
                im = im.resize(new_size)
                
                # Guarda la imagen procesada
                new_filename = os.path.splitext(filename)[0] + '.jpg'  # Cambia la extensión del archivo a .jpg
                new_file_path = os.path.join(folder_path, new_filename)
                im.save(new_file_path)
