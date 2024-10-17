import os
from PIL import Image
import numpy as np

def cargar_y_procesar_imagenes(directorio, nuevo_ancho=224, nuevo_alto=224):
    imagenes_procesadas = []

    
    for archivo in os.listdir(directorio):
        if archivo.endswith(".jpg"):  
            ruta_imagen = os.path.join(directorio, archivo)

            
            imagen = Image.open(ruta_imagen)

            
            imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

            
            imagen_array = np.array(imagen_redimensionada)

            
            imagen_array = imagen_array / 255.0

            
            imagenes_procesadas.append(imagen_array)

            
            imagen_redimensionada.save(f"procesadas/{archivo}")  

    return imagenes_procesadas

def main():
    directorio_imagenes = r'C:\Users\terra\OneDrive\Escritorio\ProyectoLoldle\IA-Loldle-'  
    imagenes_preprocesadas = cargar_y_procesar_imagenes(directorio_imagenes)

    print(f"Se procesaron {len(imagenes_preprocesadas)} imágenes")

main()
