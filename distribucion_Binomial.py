import random as rand


def distribucion_binomial(n, p):
    x = 0
    for i in range(n):
        if rand.random() < p:
            x += 1

    return x


if __name__ == '__main__':
    resultado = distribucion_binomial(10, 0.5)
    print("Resultado de la distribución binomial:", resultado)