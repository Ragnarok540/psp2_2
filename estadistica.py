from math import sqrt
from lista import sumar, largo, mapear, zipear

def promedio(x):
    return sumar(x) / largo(x) if largo(x) > 0 else 0

def desviacion(x):
    if largo(x) < 2:
        return 0

    prom = promedio(x)
    restas = mapear(lambda y: y - prom, x)
    cuadrados = mapear(lambda y: y * y, restas)
    sumatoria = sumar(cuadrados)

    return sqrt(sumatoria / (largo(x) - 1))

def beta_1(x, y):
    multip = zipear(lambda z, w: z * w, x, y)
    sum_multip = sumar(multip)

    cuadrados = mapear(lambda z: z * z, x)
    sum_cuadrados = sumar(cuadrados)

    numerador = sum_multip - largo(x) * promedio(x) * promedio(y)
    denominador = sum_cuadrados - largo(x) * promedio(x) * promedio(x)

    return numerador / denominador

def beta_0(x, y):
    return promedio(y) - beta_1(x, y) * promedio(x)

def r_xy(x, y):
    multip = zipear(lambda z, w: z * w, x, y)
    sum_multip = sumar(multip)

    sum_x = sumar(x)
    sum_y = sumar(y)

    cuadrados_x = mapear(lambda z: z * z, x)
    sum_cuadrados_x = sumar(cuadrados_x)

    cuadrados_y = mapear(lambda z: z * z, y)
    sum_cuadrados_y = sumar(cuadrados_y)

    numerador = largo(x) * sum_multip - sum_x * sum_y
    denominador_a = largo(x) * sum_cuadrados_x - sum_x * sum_x
    denominador_b = largo(x) * sum_cuadrados_y - sum_y * sum_y

    return numerador / sqrt(denominador_a * denominador_b)

def r2(x, y):
    r = r_xy(x, y)

    return r * r

def y_k(x, y, x_k):
    return beta_0(x, y) + beta_1(x, y) * x_k
