import random as rand


def calcular_pi(n):
    inside = 0

    for i in range(n):
        x = rand.uniform(0.0, 1.0)
        y = rand.uniform(0.0, 1.0)
        if x**2 + y**2 <= 1:
            inside += 1
    return (inside / n) * 4


if __name__ == '__main__':
    print(calcular_pi(10000))