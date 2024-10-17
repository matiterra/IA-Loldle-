import os
import shutil

# Directorio donde tienes todas las imágenes mezcladas
directorio_origen = r"C:\Users\terra\OneDrive\Escritorio\ProyectoLoldle\IA-Loldle-"

# Directorio donde quieres organizar las imágenes por campeón
directorio_destino =r"C:\Users\terra\OneDrive\Escritorio\ProyectoLoldle\IA-Loldle-"

# Asegúrate de que el directorio destino exista, si no, lo creamos
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Recorremos todas las imágenes en el directorio origen
for archivo in os.listdir(directorio_origen):
    if archivo.endswith(".jpg"):  # Asegúrate de que sean archivos de imagen
        # Ejemplo de nombre de archivo: Aatrox_0.jpg
        nombre_campeon = archivo.split('_')[0]  # Extraer el nombre del campeón
        
        # Crear la carpeta del campeón si no existe
        carpeta_campeon = os.path.join(directorio_destino, nombre_campeon)
        if not os.path.exists(carpeta_campeon):
            os.makedirs(carpeta_campeon)
        
        # Mover la imagen a la carpeta del campeón
        shutil.move(os.path.join(directorio_origen, archivo), os.path.join(carpeta_campeon, archivo))

print("¡Dataset organizado con éxito!")
