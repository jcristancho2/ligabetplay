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

def modificar_estadisticas(ligabetplay: dict):
    if not ligabetplay:
        print("No hay equipos registrados. Agregue equipos primero.")
        return

    print("\nEquipos disponibles:")
    for key, team in ligabetplay.items():
        print(f"{key}: {team['name']}")

    while True:
        try:
            equipo_id = int(vd.validateInt("Seleccione el ID del equipo para modificar estadísticas: "))
            if equipo_id in ligabetplay:
                break
            else:
                print("ID de equipo no válido. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    equipo = ligabetplay[equipo_id]
    estadisticas = equipo.get("estadisticas", {})

    print("\nIngrese las nuevas estadísticas del equipo:")
    estadisticas["pj"] = vd.validateInt("Partidos jugados: ")
    estadisticas["pg"] = vd.validateInt("Partidos ganados: ")
    estadisticas["pe"] = vd.validateInt("Partidos empatados: ")
    estadisticas["pp"] = vd.validateInt("Partidos perdidos: ")
    estadisticas["gf"] = vd.validateInt("Goles a favor: ")
    estadisticas["gc"] = vd.validateInt("Goles en contra: ")

    guardar_json(ligabetplay)
    print("✅ Estadísticas actualizadas correctamente.")
    os.system("pause")  # Pausa antes de regresar al menú

ligabetplay = cargar_json()
modificar_estadisticas(ligabetplay)


                