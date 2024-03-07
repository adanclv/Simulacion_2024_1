def calcular_Frecuencia_Observada(fO, num, n):
    for e in num:
        x = calcular_indice(e, n)
        fO[x] += 1


def calcular_indice(e, n):
    for i in range(n):
        if e < (i + 1) / n:
            return i
    return n - 1


if __name__ == '__main__':
    file = open('tablas/tabla_3.1.txt', 'r')
    elem = file.read().strip().split('\n')
    num = [float(e) for e in elem]
    n = 5
    fE = len(num) / 5
    fO = [0 for x in range(n)]
    chi_Cuadrada = 0

    calcular_Frecuencia_Observada(fO, num, n)
    for e in fO:
        chi_Cuadrada += (fE - e)**2 / fE

    alpha = 0.05
    print('Chi-Cuadrada =', chi_Cuadrada)
    if chi_Cuadrada < alpha:
        print(
            "Se rechaza la hipótesis de que los números pseudoaleatorios presentados provienen de una distribución uniforme.")
    else:
        print(
            "No se puede rechazar la hipótesis de que los números pseudoaleatorios presentados provienen de una distribución uniforme.")
