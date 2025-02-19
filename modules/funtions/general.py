def iniciarequipo(n_equipo):
    """Inicializa un equipo con su estructura de datos."""
    return {
        n_equipo: {
            'jugadores': {},
            'ct': {},
            'cmd': {},
            'Estadisticas': {
                'pj': 0, 'pp': 0, 'pe': 0, 'pg': 0,
                'gf': 0, 'gc': 0,
            }
        }
    }

inicializacion_fechas = {
    'fecha1': {
        'dia': '', 'mes': '', 'año': '',
        'equipo1': '', 'equipo2': '',
        'golesequipo1': '', 'golesequipo2': ''
    }
}