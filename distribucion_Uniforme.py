import matplotlib.pyplot as plt

def distribucion_uniforme(num, a, b, nx):
    for n in num:
        x = a + (b - a) * n
        nx.append(x)


if __name__ == '__main__':
    with open('tablas/tabla_3.1.txt', 'r') as file:
        elem = file.read().strip().split('\n')
        num = [float(e) for e in elem]

    nx = list()
    b = 10
    a = 5
    distribucion_uniforme(num, a, b, nx)

    fig, ax = plt.subplots()
    plt.title('Distribución uniforme')
    ax.hist(nx, bins=5, linewidth=0.5, edgecolor="white")
    plt.show()

