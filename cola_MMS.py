import random as rand
import math
import numpy as np


def distribucion_exponencial(lambd):
    x = -1 / (1 / lambd) * math.log(rand.random())
    return round(60 * x, 4)


def distribucion_poisson(mi):
    L = math.exp(-mi)
    p = 1.0
    k = 0

    while p > L:
        k += 1
        p *= rand.random()

    return k - 1


def addClientes(mi, lambd):
    clientes = distribucion_poisson(mi)
    return [distribucion_exponencial(lambd) for _ in range(clientes)]


if __name__ == '__main__':
    tiempo_adicional = list()
    cajas = list()
    cola = list()
    servidores = 1
    lambd = 0.25
    mi = 50
    horas = 10000
    colados = []
    average = float('+inf')

    while average > 10:
        tiempo_transcurrido = 0
        hora = 0
        tiempo_total = 0
        cajas = [0 for _ in range(servidores)]
        tiempo_adicional = [9999 for _ in range(servidores)]
        while tiempo_total < horas * 60:
            if tiempo_total == 0 or tiempo_total == hora * 60:
                cola[-1:] = addClientes(mi, lambd)

            for i in range(len(cajas)):
                if cajas[i] == 0:
                    if len(cola) > 0:
                        cajas[i] = cola.pop(0)
                        if cajas[i] >= tiempo_adicional[i]:
                            cajas[i] -= tiempo_adicional[i]
                    else: continue

                if cajas[i] < 1:
                   tiempo_adicional[i] = cajas[i]
                   cajas[i] -= tiempo_adicional[i]
                   continue

                cajas[i] -= 1
            tiempo_transcurrido += 1
            tiempo_total += 1
            if tiempo_transcurrido == 60:
                hora += 1
                colados.append(len(cola))
                tiempo_transcurrido = 0


        average = int(np.average(colados))
        print(f'Cajas: {servidores}, gentes: {average}')

        cola.clear()
        cajas.clear()
        tiempo_adicional.clear()
        colados.clear()
        servidores += 1



