from os.path import join, dirname, realpath
from csv import reader
from lista import lista as ls

def leer_archivo(ruta):
    ruta = join(dirname(realpath(__file__)), ruta)
    resultado = []
    
    with open(ruta, newline='') as archivo:
        lector = reader(archivo, delimiter=';')
        
        for fila in lector:
            resultado.append(ls(*fila))
            
    return resultado[0], resultado[1]
