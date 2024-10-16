import json
import requests
import time
import os

def cargo_campeones():
    ruta_archivo = r'C:\Users\terra\OneDrive\Escritorio\ProyectoLoldle\IA-Loldle-\campeones_lol.json'
    with open(ruta_archivo, 'r') as file:
        campeones = json.load(file)
    return campeones

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada exitosamente: {nombre_archivo}")
    else:
        print(f"Error al descargar la imagen: {response.status_code}")

def ver_solicitud(campeones):

    bandera = True
    while bandera:  

        for campeon in campeones:
            for numero in range(30):
                nombre_archivo = f"{campeon}_{numero}.jpg"

            
                if os.path.exists(nombre_archivo):
                    print(f"La imagen {nombre_archivo} ya existe. Saltando descarga.")
                    continue  

                url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{campeon}_{numero}.jpg"
            
            
                response = requests.get(url)
            
                if response.status_code == 200:
                    print(f"Imagen encontrada: {campeon}_{numero}")
                    descargar_imagen(url, nombre_archivo)

                else:
                    print(f"No se encontró la imagen para {campeon}_{numero}. Código: {response.status_code}")
                    bandera = False
def main():
    campeones = cargo_campeones()
    ver_solicitud(campeones)

main()
