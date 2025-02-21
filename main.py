# Importamos el módulo de funciones desde la carpeta 'modules/functions'
import modules.funtions.funtions as f
import os

# Definimos un mensaje de error para opciones inválidas
ERROR = '❗option invalid ❗'

# Construimos la ruta del archivo 'equipos.json' dentro de la carpeta 'data'
FILE = os.path.join('data/', 'equipos.json')

# Punto de entrada del script
if __name__ == '__main__':
    # Llamamos a la función principal del módulo importado
    f.m_principal()
