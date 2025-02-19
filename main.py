import ui.menus as msg
import modules.funtions.opcion as op
import modules.funtions.teams as tm
import modules.funtions.players as pl
import modules.funtions.cuerpomedico as cm
import modules.funtions.cuerpotecnico as ct
import modules.funtions.estadisticas as st
import modules.funtions.fechas as fe
import modules.validaciones as vd
import os

ligabetplay={}

ERROR = '❗option invalid ❗'

if __name__ == "__main__":

    while True:
        
        print(msg.title)
        msg.crearmenu1()
        opcion=op.opciones()
        
        match opcion:
            case 1:
                while True:
                    msg.crearmenu2()
                    opcion2=op.opcion2()
                    os.system('cls')

                    match opcion2:
                        case 1:
                            print(msg.title2)
                            for key, value in ligabetplay.items():
                                print(f'{key}.{value.get('name')}')
                            tm.addteams(ligabetplay)
                            os.system('cls')
                            
                        case 2:
                            while True:
                                print(msg.title3)
                                os.system('cls')
                                for key, value in ligabetplay.items():
                                    print(f'{key}. {value.get('name')}')
                                
                                teamselect=vd.validateAlpha("Seleccione el equipo donde desea agregar el jugador: ")
                                
                                if teamselect in ligabetplay:
                                     
                                     pl.addplayers(ligabetplay.get(teamselect).get('players'))  
                                     break  
                                else:
                                     print(ERROR)
                                     

                        case 3:
                            while True:
                                print(msg.title4)
                                for key, value in ligabetplay.items():
                                    print(f'{key}. {value.get('name')}')
                                teamselect=vd.validateAlpha("Seleccion el equipo donde desea agregar el cuerpo medico: ")

                                if teamselect in ligabetplay:
                                    cm.addcuerpomedico(ligabetplay.get(teamselect).get('cuerpomd'))
                                    break
                                else:
                                    print(ERROR)
                        
                
                        case 4:
                            while True:
                                print(msg.title5)

                                for key, value in ligabetplay.items():
                                    print(f'{key}. {value.get('name')}')
                                teamselect=vd.validateAlpha("Seleccione el equipo donde desea agregar el cuerpo tecnico: ")
                                if teamselect in ligabetplay:
                                    ct.addcuerpotec(ligabetplay.get(teamselect).get('cuerpotec'))
                                    break
                                else:
                                    print(ERROR)
                        case 5:
                            while True:
                                print(msg.title6)
                                for key, value in ligabetplay.items():
                                    print(f'{key}.{value.get('name')}')
                                teamselect=vd.validateAlnum("Seleccione el equipo: ")

                                if teamselect in ligabetplay:
                                    st.addestatics(ligabetplay.get(teamselect).get('estadisticas'))
                                    break
                                else:
                                    print(ERROR)

                        case 6:
                            print("Volviendo al menú principal... 🔙")
                            break

                        case _:
                            print(ERROR)
            case 2:
              
                while True:
                    print(msg.title7)
                    
                    for key, value in ligabetplay.items():
                        print(f"{key}. {value.get('name')}")

                    # Pedir equipos sin usar key directamente en el mensaje
                    teamselect1 = vd.validateAlnum("Seleccione el equipo 1: ")
                    teamselect2 = vd.validateAlnum("Seleccione el equipo 2: ")

                    if teamselect1 not in ligabetplay or teamselect2 not in ligabetplay:
                        print(f" Uno o ambos equipos no existen. Intente de nuevo.")
                        continue  # Volver a pedir los equipos si la selección es incorrecta

                    print(f"{ligabetplay.get(teamselect1).get('name')} 🆚 {ligabetplay.get(teamselect2).get('name')}")

                    # Pasar los equipos a la función
                    fecha = fe.addfechaspartidos()
                    

                    print(msg.title7)
                    print(f" {ligabetplay[teamselect1]['name']} vs {ligabetplay[teamselect2]['name']} ")
                    print(f'{fecha}')
                    

                    break  

            case 3:
                print("Saliendo")
                break


            
                
                    
                    

   


