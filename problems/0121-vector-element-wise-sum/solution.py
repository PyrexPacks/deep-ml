import numpy as np

def vector_sum(a: list[int | float], b: list[int | float]) -> list[int | float]:
    lista = []
    n = 0

    a = np.array(a)
    b = np.array(b)

    if a.size != b.size:
        return -1

    while n < a.size:
        lista.append(a[n] + b[n])
        n += 1

    return lista