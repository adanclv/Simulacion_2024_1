import math
import matplotlib.pyplot as plt

def distribucion_triangular(num, nx, a, b, c):
    for i in range(0, len(num) - 1, 2):
        if num[i] < (b-a / c-a):
            x = a + (b - a) * math.sqrt(num[i + 1])
        else:
            x = c - (c - b) * math.sqrt(num[i + 1])
        nx.append(x)


if __name__ == '__main__':
    with open('tablas/tabla_3.1.txt', 'r') as file:
        elem = file.read().strip().split('\n')
        num = [float(e) for e in elem]

    a = 0.0
    b = 0.5
    c = 1.0
    nx = list()
    distribucion_triangular(num, nx, a, b, c)

    fig, ax = plt.subplots()
    plt.title('Distribución triangular')
    ax.hist(nx, bins=3, linewidth=0.5, edgecolor="white")
    plt.show()