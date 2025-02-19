import os
def opciones ():
    while True:
       
        try:
            
            opcion=int(input('Escoga la opcion: '))

            return opcion
            
        except ValueError:
            print("Opcion Invalida")
           
            

def opcion2():
    while True:
        try:
            opcion2=int(input('Ingrese la opcion: '))
            return opcion2
        except ValueError:
            print('opcion invalida')
            