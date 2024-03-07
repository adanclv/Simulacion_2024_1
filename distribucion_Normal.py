import matplotlib.pyplot as plt

def distribucion_normal(num, nx, mi, sigma):
    for i in range(0, len(num) - 12, 12):
        suma = sum(num[i:i + 12])
        x = mi + sigma * (suma - 6)
        nx.append(x)


if __name__ == '__main__':
    with open('tablas/tabla_3.1.txt', 'r') as file:
        elem = file.read().strip().split('\n')
        num = [float(e) for e in elem]

    mi = 0.5
    sigma = 0.25
    nx = list()
    distribucion_normal(num, nx, mi, sigma)

    fig, ax = plt.subplots()
    plt.title('Distribución normal')
    ax.hist(nx, bins=10, linewidth=0.5, edgecolor="white")
    plt.show()
