from lector import leer_archivo
from ttr import very_small, small, medium, large, very_large
from lista import largo
import sys

def main(ruta):
    try:
        ls1, ls2 = leer_archivo(ruta)
        if largo(ls1) != largo(ls2):
            print(f"""ERROR: Las listas no son del mismo tamaño,
tienen {largo(ls1)} y {largo(ls2)} elementos respectivamente.""")
            sys.exit()
        print(f"very_small: {very_small(ls1, ls2)}")
        print(f"small: {small(ls1, ls2)}")
        print(f"medium: {medium(ls1, ls2)}")
        print(f"large: {large(ls1, ls2)}")
        print(f"very_large: {very_large(ls1, ls2)}")
    except ValueError:
        print("ERROR: Todos los parámetros deben ser números reales o enteros.")
        sys.exit()
    except FileNotFoundError:
        print("ERROR: El archivo especificado no fue encontrado.")
        sys.exit()

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print("""ERROR: Se requiere la ruta del archivo CSV,
por ejemplo: 'test1.csv'.""")
        sys.exit()
