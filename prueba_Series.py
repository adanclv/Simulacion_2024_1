from scipy.stats import chi2

def calcular_frecuencia_Observada(parejas, frecuenciaO, fE, n):
    fO = 0
    for pareja in parejas:
        x = calcular_indice(pareja[0], n)
        y = calcular_indice(pareja[1], n)
        frecuenciaO[x][y] += 1

    for i in range(n):
        for j in range(n):
            fO += (frecuenciaO[i][j] - fE)**2 / fE

    return fO


def calcular_indice(e, n):
    for i in range(n):
        if e < (i + 1) / n:
            return i
    return n - 1


def test_chi_cuadrado(estadistico, grados_libertad, nivel_significancia):
    valor_critico = chi2.ppf(1 - nivel_significancia, grados_libertad)
    if estadistico > valor_critico:
        print("Se rechaza la hipótesis, los números presentados no pasan la prueba de uniformidad.")
    else:
        print("No se puede rechazar la hipótesis, los números presentados pasan la prueba de uniformidad.")


if __name__ == '__main__':
    file = open('tabla_3.1.txt', 'r')
    elem = file.read().strip().split('\n')
    file.close()
    num = [float(e) for e in elem]
    n = 5
    N = len(num)
    parejas = [[num[i], num[i+1]] for i in range(N-1)]
    frecuenciaO = [[0 for x in range(n)] for y in range(n)]
    fE = (N-1) /(n)**2
    alpha = 0.05

    fO = calcular_frecuencia_Observada(parejas, frecuenciaO, fE, n)
    print('Frecuencia esperada:', fE)
    print('Frecuencia observada:', fO)
    test_chi_cuadrado(fO, n**2, alpha)
