import math
import matplotlib.pyplot as plt

def distribucion_exponencial(num, nx, lambd):
    for n in num:
        x = -(1 / lambd) * math.log(n)
        nx.append(x)


if __name__ == '__main__':
    with open('tablas/tabla_3.1.txt', 'r') as file:
        elem = file.read().strip().split('\n')
        num = [float(e) for e in elem]

    lambd = 1
    nx = list()
    distribucion_exponencial(num, nx, lambd)

    fig, ax = plt.subplots()
    plt.title('Distribución exponencial')
    ax.hist(nx, bins=8, linewidth=0.5, edgecolor="white")
    plt.show()