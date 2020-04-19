from lector import leer_archivo
from estadistica import beta_1, beta_0, r_xy, r2, y_k
from lista import largo
import sys

def main(ruta, x_k):
    try:
        ls1, ls2 = leer_archivo(ruta)
        if largo(ls1) != largo(ls2):
            print(f"""ERROR: Las listas no son del mismo tamaño,
tienen {largo(ls1)} y {largo(ls2)} elementos respectivamente.""")
            sys.exit()
        print(f"beta_1: {beta_1(ls1, ls2)}")
        print(f"beta_0: {beta_0(ls1, ls2)}")
        print(f"r_xy: {r_xy(ls1, ls2)}")
        print(f"r2: {r2(ls1, ls2)}")
        print(f"y_k: {y_k(ls1, ls2, float(x_k))}")
    except ValueError:
        print("ERROR: Todos los parámetros deben ser números reales o enteros.")
        sys.exit()
    except FileNotFoundError:
        print("ERROR: El archivo especificado no fue encontrado.")
        sys.exit()

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print("""ERROR: Se requieren dos parámetros, la ruta del archivo CSV
y el valor x_k, por ejemplo: 'test.csv 386'.""")
        sys.exit()
