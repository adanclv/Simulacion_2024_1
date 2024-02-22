def congruencialMixto(a, seed, c, m):
    xn = seed

    for i in range(m):
        xn = (a * xn + c) % m
        uniform = xn / m
        print(f'{xn} - {uniform}')


if __name__ == '__main__':
    seed = 9
    a = 21
    c = 3
    m = 100

    congruencialMixto(a, seed, c, m)