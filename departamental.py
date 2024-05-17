import math


def congruencialMultiplicativo(seed, a , m):
    xn = seed
    num = list()

    for i in range(100):
        xn = (a * xn) % m
        num.append(xn)
    return num

def pruebaZ(num):
    promedio = sum(num) / len(num)
    promedio /= 1020

    z = (promedio - 0.5) * math.sqrt(len(num))
    z = z / math.sqrt(1 / 12)
    z = abs(z)

    if z < 1.96:
        print('Si son aleatorios')
    else:
        print('No son aleatorios')


if __name__ == '__main__':
    seed = 64
    a = 7
    m = 1020

    numeros = congruencialMultiplicativo(seed, a, m)
    pruebaZ(numeros)
