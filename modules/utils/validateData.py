import modules.utils.controlScreen as cc


mError = 'caracter invalid'             #mensaje generico
"""**************************************************************************************************************"""
def validateInt(msg: str)-> int:        #validacion de enteros // usar para edades o cantidades
    while True:
        try:
            return int(input(msg))      # muestra el mensaje y espera al usuario
        except ValueError:
            print(mError)               # impresion del error si falla
            cc.pause_screen()           # pausa de la pantalla

def validatefloat(msg:str) -> float:    #validacion de flotantes // usar para datos decimales
    while True:
        try:
            return float(input(msg))    # muestra el mensaje y espera al usuario
        except ValueError:
            print(mError)               # impresion del error si falla
            cc.pause_screen()           # pausa de la pantalla

def validateAlpha(msg: str) -> str:     #validacion de textos sin numeros // uso para palabras 
    while True:
        x = input(msg).strip()          #elimina espacios entre el primer y ultimo caracter .strip()
        if x.replace(' ', '').isalpha():#verificacion de solo letras y espacios
            return x                    #retorna el texto valido
        else:
            print(mError)               #impresion del error si falla
            cc.pause_screen()           #pausa de la pantalla
            
def validateAlnum(msg: str) -> str:     #valida datos alfanumericos // usar para direcciones sin caracter especial
    while True:
        x = input(msg).strip()          #elimina espacios entre el primer y ultimo caracter .strip()
        if x.replace(' ', '').isalnum():#verificacion de solo letras y espacios
            return x                    #retorna el texto valido
        else:
            print(mError)               #impresion del error si falla
            cc.pause_screen()           #pausa de la pantalla

def validateDigit(msg: str) -> str:     ##valida datos alfanumericos // usar para direcciones sin caracter especial
    while True:
        x=input(msg).strip()            #elimina espacios entre el primer y ultimo caracter .strip()
        if x.replace(' ', '').isdigit():#verificacion de solo numeros y espacios
            return x                    #retorna el texto valido
        else:
            print(mError)               #impresion del error si falla
            cc.pause_screen()           #pausa de la pantalla
            