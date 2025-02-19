import os
import json
import modules.validaciones as vd
import modules.utils.controlScreen as cc

# Cargar JSON desde archivo
def cargar_json(filename="ligabetplay.json"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}  # Retorna un diccionario vacío si el archivo no existe

# Guardar JSON en archivo
def guardar_json(data, filename="ligabetplay.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Agregar jugadores a un equipo existente
def addplayers(ligabetplay: dict):
    cc.XScreen()

    if not ligabetplay:
        print("⚠️ No hay equipos registrados. Agregue equipos primero.")
        return

    # Mostrar equipos disponibles
    print("\nEquipos disponibles:")
    for key, team in ligabetplay.items():
        print(f"{key}: {team['name']}")

    # Selección del equipo
    while True:
        equipo_id = vd.validateAlnum("Seleccione el ID del equipo al que desea agregar jugadores: ")
        equipo_id = str(equipo_id)  # Convertir a string para asegurar coincidencia en JSON

        if equipo_id in ligabetplay:
            break
        print("❌ ID de equipo no válido. Intente nuevamente.")

    equipo = ligabetplay[equipo_id]

    # Agregar jugadores
    while True:
        nombre = vd.validateAlpha("Escriba el nombre del jugador: ")
        dorsal = vd.validateInt("Ingrese el número de la dorsal: ")

        if str(dorsal) in equipo["players"]:
            print(f"⚠️ La dorsal {dorsal} ya está asignada a {equipo['players'][str(dorsal)]['namePlayer']}. Pruebe otro número.")
            continue

        edad = vd.validateInt("Ingrese la edad: ")

        equipo["players"][str(dorsal)] = {
            'dorsal': dorsal,
            'namePlayer': nombre,
            'edad': edad
        }

        # Guardar cambios en JSON
        guardar_json(ligabetplay)
        print(f"✅ Jugador {nombre} agregado al equipo {equipo['name']}.")

        otroplayer = vd.validateAlpha("¿Desea agregar otro jugador? (s/n): ").lower()
        if otroplayer != "s":
            print("Volviendo al menú anterior... 🔙")
            input("Presione Enter para continuar...")  # Compatible con todos los sistemas
            break

# Ejecutar la función
ligabetplay = cargar_json()
addplayers(ligabetplay)
