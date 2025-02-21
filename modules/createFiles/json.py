import json
import os
from typing import Dict, List, Optional

def read_json(archivo: str) -> Dict:
    """
    Lee un archivo JSON y retorna su contenido como un diccionario.

    :param archivo: Ruta del archivo JSON a leer.
    :return: Diccionario con los datos del JSON o un diccionario vacío si el archivo no existe.
    """
    try:
        with open(archivo, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_json(file_path: str, data: Dict) -> None:
    """
    Escribe datos en un archivo JSON.

    :param file_path: Ruta del archivo JSON donde se guardarán los datos.
    :param data: Diccionario con los datos a escribir.
    """
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def update_json(file_path: str, data: Dict, path: Optional[List[str]] = None) -> None:
    """
    Actualiza un archivo JSON con nuevos datos en una ruta específica.

    :param file_path: Ruta del archivo JSON a modificar.
    :param data: Diccionario con los nuevos datos a agregar o actualizar.
    :param path: Lista con la ruta dentro del JSON donde se actualizarán los datos (opcional).
    
    Ejemplo:
        update_json('db.json', {'nuevo': 'dato'}, ['ruta', 'subruta'])
    """
    current_data = read_json(file_path)
    
    if not path:
        current_data.update(data)
    else:
        current = current_data
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)

    write_json(file_path, current_data)

def delete_json(file_path: str, path: List[str]) -> bool:
    """
    Elimina una clave específica dentro de un archivo JSON.

    :param file_path: Ruta del archivo JSON a modificar.
    :param path: Lista con la ruta de claves donde se encuentra el dato a eliminar.
    :return: True si la eliminación fue exitosa, False si la clave no existe.

    Ejemplo:
        delete_json('db.json', ['ruta', 'subruta'])
    """
    data = read_json(file_path)
    current = data

    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]

    if path and path[-1] in current:
        del current[path[-1]]
        write_json(file_path, data)
        return True
    return False

def initialize_json(file_path: str, initial_structure: Dict) -> None:
    """
    Inicializa un archivo JSON con una estructura base si no existe.

    :param file_path: Ruta del archivo JSON.
    :param initial_structure: Diccionario con la estructura inicial del JSON.

    Si el archivo ya existe, se asegura de que contenga al menos las claves definidas en initial_structure.
    """
    if not os.path.isfile(file_path):
        write_json(file_path, initial_structure)
    else:
        current_data = read_json(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        write_json(file_path, current_data)

