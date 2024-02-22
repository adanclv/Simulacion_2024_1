import numpy as np


def calcular_maximo(num, n):
    maximo = float('-inf')
    for i in range(n):
        dn = np.absolute(num[i] - (i+1)/n)
        if dn > maximo:
            maximo = dn

    return maximo


if __name__ == '__main__':
    file = open('tabla_3.1.txt', 'r')
    elem = file.read().strip().split('\n')

    num = [float(e) for e in elem]
    Dn = calcular_maximo(sorted(num), len(num))

    print('Dn =', Dn)
    if Dn <= 0.134:
        print('Los números presentados pseudoaleatorios provienen de una distribución uniforme.')
    else:
        print('Los números presentados pseudoaleatorios no provienen de una distribución uniforme.')
