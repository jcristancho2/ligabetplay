import os
import modules.validaciones as vd

def addfechaspartidos():
    while True:

        dia=vd.validateInt('Ingrese el dia del partido: ')
        mes=vd.validateInt('Ingrese el mes del partido: ')
        año=vd.validateInt('Ingrese el año del partido: ')
        

        fecha=(f"{dia}/{mes}/{año}")
        
        otrafecha=vd.validateAlpha("Desea agregar otras fechas ? S/N").lower()
        if otrafecha != 's':
            os.system("pause")
            return fecha
            

