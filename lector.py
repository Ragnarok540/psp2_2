from os.path import join, dirname, realpath
from csv import reader
from lista import lista as ls, largo

def leer_archivo(ruta):
    ruta = join(dirname(realpath(__file__)), ruta)
    resultado = []
    
    with open(ruta, newline='') as archivo:
        lector = reader(archivo, delimiter=';')
        
        for fila in lector:
            resultado.append(ls(*fila))

    try:

        return resultado[0], resultado[1]

    except IndexError:

        size = largo(resultado[0])
        unos = [1 for x in range(size)]
        return resultado[0], ls(*unos)
