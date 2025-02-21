import modules.utils.validateData as vd , modules.utils.controlScreen as cc, modules.utils.emotic as e
import ui.menus as m
import modules.createFiles.json as j 
import os
from main import ERROR,FILE

def m_principal():
    
    cc.XScreen()
    print(m.menu_principal)
    option = int(vd.validateInt(f'{e.opt}  '))
    match option:
        case 1: #administrar equipos
            m_admin_equi()
        case 2: #programar fechas
            pass
        case 3: #registrar marcadores
            actualizar_estadisticas()
        case 4: #mostrar estadisticas
            mostrar_estad()
        case 5: #salir del programa
            exit
        case _:
            print(ERROR)
        
def m_equi():
    cc.XScreen()
    print(m.menu_equipos)
    option = int(vd.validateInt(f'{e.opt}'))
    ligabetpay = j.read_json(FILE)
    match option:
        case 1: #administar jugadores
            players()
        case 2: #administrar cuerpo medico
            equi_med()
        case 3: #arministrar cuerpo tecnico
            equi_tec()
        case 4: # regresar
            return m_principal()
        case _:
            print(ERROR)
            
def m_admin_equi():
    cc.XScreen()
    print(m.menu_admin_equipos)
    option = int(vd.validateInt(f'{e.opt}'))
    ligabetpay = j.read_json(FILE)
    match option:
        case 1: #agregar equipo
            equipos(ligabetpay)
        case 2: #eliminar equipo
            delete_equi()
        case 3: #editar equipo
            edit_equi()
        case 4: #mostrar equipo
            mostrar_equi()
        case 5: # regresar
            return m_principal()
        case _:
            print(ERROR)
            
#/////////////////////////////////////////////////////////////////


def equipos(ligabetpay:dict):# # Función para agregar equipos
    team={
            "name":"",
            "players":{},
            "cuerpomd":{},
            "cuerpotec":{},
            "estadisticas":{
                "pj":0,
                "pp":0,
                "pg":0,
                "pe":0,
                "gf":0,
                "gc":0

            }
           
        }
    j.initialize_json(FILE,team)
    cc.XScreen()
    name = vd.validateAlpha('ingrese el nombre del equipo: ')
    team.update({'name':name})
    ligabetpay.update({len(ligabetpay)+1:team})    
    j.write_json(FILE, ligabetpay)
    option = vd.validateAlpha('desea agregar otro Equipo [s/n]').lower()
    if option in ['s','n']:
        if option == 's':
            return equipos(ligabetpay)
        elif option =='n':
            return m_admin_equi()

def players(): # Función para agregar jugadores

    ligabetpay = j.read_json(FILE)
    
    print("\n🏆 Lista de Equipos Disponibles:")
    for team_id, team_data in ligabetpay.items():
        print(f"ID: {team_id} EQUIPO: {team_data['name'].title()}")

    equipo_id = vd.validateInt("\n Ingresa el ID del equipo para agregar un jugador: ")
    equipo_id = str(equipo_id)
    
    if equipo_id not in ligabetpay:
        print("equipo no registrado")
        return

    p_name = vd.validateAlpha('Ingresa el nombre del jugador: ')
    edad = int(vd.validateInt(f' Ingresa la edad de {p_name}: '))
    dorsal = int(vd.validateInt(f' Ingresa el número DORSAL de {p_name}: '))
    
    print("""
          1: Portero
          2: Defensa
          3: Centrocampista
          4: Delantero
          """)
    option = int(vd.validateInt(f'{e.opt}'))
    ubicacion = {1: 'portero', 2: 'defensa', 3: 'centrocampista', 4: 'delantero'}
    
    posicion = ubicacion.get(option, "Desconocido")

    if posicion == "Desconocido":
        print("Posición inválida. Intente nuevamente.")
        return players()

    nuevo_player = {
        "nombre": p_name,
        "edad": edad,
        "dorsal": dorsal,
        "posicion": posicion
    }

    ligabetpay[equipo_id]["players"][p_name] = nuevo_player
    j.write_json(FILE, ligabetpay)

    option = vd.validateAlpha("¿Desea agregar otro jugador? [s/n]: ").lower()
    if option == "s":
        return players()
    elif option == "n":
        return m_admin_equi()
    
def equi_med(): #funcion para agregar medicos

    ligabetpay = j.read_json(FILE)
    print("\n🏆 Lista de Equipos Disponibles:")
    for team_id, team_data in ligabetpay.items():
        print(f"ID: {team_id} EQUIPO: {team_data['name'].title()}")

    equipo_id = vd.validateInt("\n Ingresa el ID del equipo para agregar un jugador: ")
    equipo_id = str(equipo_id)
    
    if equipo_id not in ligabetpay:
        print("equipo no registrado")
        return
    
    p_name_med = vd.validateAlpha('Ingresa el nombre del staff medico: ')
    edad = int(vd.validateInt(f' Ingresa la edad de {p_name_med}: '))
    print("""
          1: medico
          2: fisoterapeuta
          3: camillero
          4: enfermero
          5: nuticionista
          """)
    option = int(vd.validateInt(f'{e.opt}'))
    ubicacion = {1: 'medico', 2: 'fisioterapeuta', 3: 'camillero', 4: 'enfermero', 5:'nutricionista'}
    
    posicion = ubicacion.get(option, "Desconocido")

    if posicion == "Desconocido":
        print("Posición inválida. Intente nuevamente.")
        return equi_med()

    nuevo_staff_med = {
        "nombre": p_name_med,
        "edad": edad,
        "funcion": posicion
    }

    ligabetpay[equipo_id]["cuerpomd"][p_name_med] = nuevo_staff_med
    j.write_json(FILE, ligabetpay)

    option = vd.validateAlpha("¿Desea agregar otro personal de staff medico? [s/n]: ").lower()
    if option == "s":
        return equi_med()
    elif option == "n":
        return m_admin_equi()
    
def equi_tec(): #funcion para agregar tecnicos

    ligabetpay = j.read_json(FILE)
    print("\n🏆 Lista de Equipos Disponibles:")
    for team_id, team_data in ligabetpay.items():
        print(f"ID: {team_id} EQUIPO: {team_data['name'].title()}")

    equipo_id = vd.validateInt("\n Ingresa el ID del equipo para agregar un jugador: ")
    equipo_id = str(equipo_id)
    
    if equipo_id not in ligabetpay:
        print("equipo no registrado")
        return
    p_name_tec = vd.validateAlpha('Ingresa el nombre del staff medico: ')
    edad = int(vd.validateInt(f' Ingresa la edad de {p_name_tec}: '))
    print("""
          1: entrenador
          2: preparador fisico
          3: entrenador de portero
          4: analista de rendimiento
          """)
    option = int(vd.validateInt(f'{e.opt}'))
    ubicacion = {1: 'entrenador', 2: 'preparador fisico', 3: 'entrenador de portero', 4: 'analista de rendimiento'}
    
    posicion = ubicacion.get(option, "Desconocido")

    if posicion == "Desconocido":
        print("Posición inválida. Intente nuevamente.")
        return equi_tec()

    nuevo_staff_tec = {
        "nombre": p_name_tec,
        "edad": edad,
        "funcion": posicion
    }

    ligabetpay[equipo_id]["cuerpotec"][p_name_tec] = nuevo_staff_tec
    j.write_json(FILE, ligabetpay)

    option = vd.validateAlpha("¿Desea agregar otro staff tecnico? [s/n]: ").lower()
    if option == "s":
        return equi_med()
    elif option == "n":
        return m_admin_equi()
    
#/////////////////////////////////////////////////////////////////

def mostrar_equi(): #funcion para visualizacion
    ligabetpay = j.read_json(FILE)
    print("\n🏆 Lista de Equipos Disponibles:")
    for team_id, team_data in ligabetpay.items():
        print(f"ID: {team_id} EQUIPO: {team_data['name'].title()}")

    equipo_id = vd.validateInt("\n Ingresa el ID del equipo para agregar un jugador: ")
    equipo_id = str(equipo_id)
    
    if equipo_id not in ligabetpay:
        print("equipo no registrado")
        return

def edit_equi(): #funcion para editar equipos
    pass

def delete_equi(): #funcion para eliminar equipos
    ligabetpay = j.read_json(FILE)
    print("\n🏆 Lista de Equipos Disponibles:")
    for team_id, team_data in ligabetpay.items():
        print(f"ID: {team_id} EQUIPO: {team_data['name'].title()}")

    equipo_id = vd.validateInt("\n Ingresa el ID del equipo que desea eliminar : ")
    equipo_id = str(equipo_id)
    
    if equipo_id not in ligabetpay:
        print("⚠️ Equipo no registrado.")
    else:
        # Confirmación antes de eliminar
        confirmacion = input(f"¿Estás seguro de eliminar el equipo '{ligabetpay[equipo_id]['name'].title()}'? (S/N): ").strip().lower()
    
    if confirmacion == "s":
        del ligabetpay[equipo_id]  # Eliminar equipo
        print("✅ Equipo eliminado correctamente.")
        
        j.write_json(FILE, ligabetpay)
    else:
        print("⚠️ Operación cancelada.")

#/////////////////////////////////////////////////////////////////
    
def actualizar_estadisticas(): #funcion para actualizar estadisticas
    ligabetpay = j.read_json(FILE)
    print("\n🏆 Lista de Equipos Disponibles:")
    for team_id, team_data in ligabetpay.items():
        print(f"ID: {team_id} - {team_data['name'].title()}")

    equipo_id = vd.validateInt("\n Ingresa el ID del equipo para agregar un jugador: ")
    equipo_id = str(equipo_id)
    
    equipo = ligabetpay[equipo_id]
                
    print(f"\n📊 Estadísticas Actuales de {equipo['name'].title()}:")
    for stat, value in equipo["estadisticas"].items():
        print(f"{stat.upper()}: {value}")

    print("\n🔄 Ingresa los nuevos valores de las estadísticas:")

    # Solicitar y actualizar estadísticas
    for stat in equipo["estadisticas"]:
        while True:
            try:
                nuevo_valor = int(input(f"{stat.upper()} (Valor actual: {equipo['estadisticas'][stat]}): "))
                equipo["estadisticas"][stat] = nuevo_valor
                break
            except ValueError:
                print("⚠️ Ingresa un número válido.")

    j.write_json(FILE, ligabetpay)

    print("\n✅ Estadísticas actualizadas correctamente.")


def mostrar_estad(): #funcion para mostrar estadisticas
    ligabetpay = j.read_json(FILE)
    print("Lista de Equipos Disponibles:")
    for team_id, team_data in ligabetpay.items():
        print(f"ID: {team_id} - {team_data['name'].title()}")


    equipo_id = input("Ingresa el ID del equipo que deseas consultar: ").strip()


    if equipo_id not in ligabetpay:
        print("Equipo no registrado.")
        return

    equipo = ligabetpay[equipo_id] 

    print(f"Estadísticas de {equipo['name'].title()}:")
    for stat, value in equipo["estadisticas"].items():
        print(f"🔹 {stat.upper()}: {value}")