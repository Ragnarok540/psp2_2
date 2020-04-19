from math import log, exp
from estadistica import promedio, desviacion
from lista import mapear, zipear

def _desv_log(x, y):
    div = zipear(lambda z, w: z / w, x, y)
    ln = mapear(log, div)
    return desviacion(ln)

def _prom_log(x, y):
    div = zipear(lambda z, w: z / w, x, y)
    ln = mapear(log, div)
    return promedio(ln)

def very_small(x, y):
    ln_vs = _prom_log(x, y) - 2 * _desv_log(x, y)
    return exp(ln_vs)

def small(x, y):
    ln_s = _prom_log(x, y) - _desv_log(x, y)
    return exp(ln_s)

def medium(x, y):
    ln_m = _prom_log(x, y)
    return exp(ln_m)

def large(x, y):
    ln_l = _prom_log(x, y) + _desv_log(x, y)
    return exp(ln_l)

def very_large(x, y):
    ln_vl = _prom_log(x, y) + 2 * _desv_log(x, y)
    return exp(ln_vl)
