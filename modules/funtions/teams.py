import modules.validaciones as vd , modules.utils.controlScreen as cc
import os
import json

# Función para guardar los datos en un archivo JSON
def guardar_en_json(ligabetplay, filename="ligabetplay.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(ligabetplay, file, indent=4, ensure_ascii=False)

def addteams(ligabetplay: dict):
    cc.XScreen()
    while True:
        team = {
            "name": "",
            "players": {},
            "cuerpomd": {},
            "cuerpotec": {},
            "estadisticas": {
                "pj": 0,
                "pp": 0,
                "pg": 0,
                "pe": 0,
                "gf": 0,
                "gc": 0
            }
        }
        
        name = vd.validateAlpha("Ingrese el nombre del equipo: ")
        team["name"] = name
        ligabetplay[len(ligabetplay) + 1] = team

        # Guardar en JSON después de cada adición
        guardar_en_json(ligabetplay)

        otroteam = vd.validateAlpha('Desea agregar otro Equipo S/N: ').lower()
        if otroteam != 's':
            print("Volviendo al menú anterior... 🔙")
            os.system('pause')  # Espera antes de regresar al menú
            break

    
    

