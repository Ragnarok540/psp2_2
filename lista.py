def construir(x, y=None):
    return (float(x), y)

def lista(*x):
    return construir(x[0], lista(*x[1:])) if x else None

def primero(x):
    return x[0]

def resto(x):
    return x[1]

def vacia(x):
    return x is None

def largo(x):
    return 1 + largo(resto(x)) if not vacia(x) else 0

def sumar(x):
    return primero(x) + sumar(resto(x)) if x else 0

def mapear(f, x):
    return construir(f(primero(x)), mapear(f, resto(x))) if x else None

def zipear(f, x, y):
    return construir(f(primero(x), primero(y)),
                     zipear(f, resto(x), resto(y))) if x and y else None
