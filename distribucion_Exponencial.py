import math
import random as rand
import matplotlib.pyplot as plt


def exponencial(M):
    u = rand.random()
    print(u)
    x = -(1 / M) * math.log(1-u)
    return x

def distribucion_exponencial(num, nx, lambd):
    for n in num:
        x = -(1 / lambd) * math.log(n)
        nx.append(x)


if __name__ == '__main__':
    resultado = exponencial(4)
    print(resultado)
    '''
    with open('tablas/tabla_3.1.txt', 'r') as file:
        elem = file.read().strip().split('\n')
        num = [float(e) for e in elem]

    lambd = 0.25
    nx = list()
    distribucion_exponencial(num, nx, lambd)

    print(nx)
    fig, ax = plt.subplots()
    plt.title('Distribución exponencial')
    ax.hist(nx, bins=8, linewidth=0.5, edgecolor="white")
    plt.show()
    '''