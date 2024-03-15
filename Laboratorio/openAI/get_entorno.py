def get_detalles():
    import os
    import sys
    import psutil

    # Obtener detalles del sistema operativo
    sistema_operativo = os.name
    detalles_sistema = os.uname()

    # Obtener detalles de la versión de Python
    version_python = sys.version
    plataforma_python = sys.platform

    # Obtener el uso de la CPU
    uso_cpu = psutil.cpu_percent(interval=1)

    # Obtener el uso de la memoria
    uso_memoria = psutil.virtual_memory().percent

    # Obtener el directorio actual
    directorio_actual = os.getcwd()

    # Obtener la lista de archivos en el directorio actual
    archivos_en_directorio = os.listdir(directorio_actual)

    detalles = f"""
    Sistema Operativo: {sistema_operativo}
    Detalles del Sistema: {detalles_sistema}
    Versión de Python: {version_python}
    Plataforma Python: {plataforma_python}
    Uso de CPU: {uso_cpu}%
    Uso de Memoria: {uso_memoria}%
    Directorio Actual: {directorio_actual}
    Archivos en el Directorio: {archivos_en_directorio}
    """

    return detalles
