import math
import random as rand


def distribucion_poisson(lambd):
    L = math.exp(-lambd)
    p = 1.0
    k = 0

    while p > L:
        k += 1
        p *= rand.random()

    return k -1


if __name__ == '__main__':
    resultado = distribucion_poisson(2.5)
    print("Resultado de la distribución de Poisson:", resultado)