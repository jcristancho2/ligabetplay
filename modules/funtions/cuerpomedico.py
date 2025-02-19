import os
import json
import modules.validaciones as vd

def cargar_json(filename="ligabetplay.json"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}  
def guardar_json(data, filename="ligabetplay.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def addcuerpotec(ligabetplay: dict):
    if not ligabetplay:
        print("No hay equipos registrados. Agregue equipos primero.")
        return

    print("\nEquipos disponibles:")
    for key, team in ligabetplay.items():
        print(f"{key}: {team['name']}")

    while True:
        try:
            equipo_id = int(vd.validateInt("Seleccione el ID del equipo al que desea agregar cuerpo técnico: "))
            if equipo_id in ligabetplay:
                break
            else:
                print("ID de equipo no válido. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    equipo = ligabetplay[equipo_id]

    while True:
        name = vd.validateAlpha("Ingrese el nombre del miembro del cuerpo técnico: ")
        edad = vd.validateInt("Ingrese la edad: ")
        rol = vd.validateAlpha("Ingrese el rol (Ej: Director Técnico, Asistente, Preparador Físico, etc.): ")

        cuerpot = {
            'name': name,
            'edad': edad,
            'rol': rol
        }

        equipo["cuerpotec"][name] = cuerpot

        guardar_json(ligabetplay)

        otro = vd.validateAlpha("¿Desea agregar otro miembro al cuerpo técnico? (s/n): ").lower()
        if otro != "s":
            print("Volviendo al menú anterior... 🔙")
            os.system("pause")  
            break

ligabetplay = cargar_json()
addcuerpotec(ligabetplay)

        
       
