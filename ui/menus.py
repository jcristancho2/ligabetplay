# Importamos el módulo 'emotic' desde 'modules.utils' para usar emoticonos personalizados
import modules.utils.emotic as e  

# Definimos el menú principal con opciones numeradas y emoticones para mejorar la presentación
menu_principal = f"""
{e.diamantep * 20}
            MENU PRINCIPAL
{e.diamantep * 20}

{e.uno} Administrar equipos
{e.dos} Programar fechas
{e.tres} Registrar marcadores
{e.cuatro} Mostrar estadísticas
{e.cinco} Salir {e.door}
"""

# Menú para la administración de equipos
menu_admin_equipos = f"""
{e.diamantep * 20}
            ADMINISTRAR EQUIPOS
{e.diamantep * 20}

{e.uno} Agregar Equipo
{e.dos} Eliminar Equipo
{e.tres} Editar Equipo
{e.cuatro} Mostrar Equipo
{e.cinco} Regresar {e.bk}
"""

# Menú para la administración de equipos en detalle
menu_equipos = f"""
{e.diamantep * 20}
            MENU EQUIPOS
{e.diamantep * 20}

{e.uno} Administrar jugadores
{e.dos} Administrar staff médico
{e.tres} Administrar staff técnico
{e.cuatro} Regresar {e.bk}
{e.diamantep * 20}
"""

