import json
import requests
from bs4 import BeautifulSoup

def cargo_campeones():
    with open('campeones_lol.json', 'r') as file:
        campeones = json.load(file)
        print(campeones)


def ver_solicitud():
    #cargo página
    url = "https://www.leagueoflegends.com/es-mx/champions/"
    response = requests.get(url)

    #veo status
    if response.status_code == 200:
        print("La página responde")
        #uso jabón bello para encontrar los splash arts del lolsito
        soup = BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Error en la solicitud: {response.status_code}")

    print(response)
    print(soup.title.string)
    #printeo todo el html
    print(soup.prettify())



def main():
    ver_solicitud()
    cargo_campeones()
main()