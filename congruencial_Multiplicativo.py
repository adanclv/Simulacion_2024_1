def congruencialMultiplicativo(seed, a , m):
    xn = seed

    for i in range(100):
        xn = (a * xn) % m
        print(f'{i+1}. {xn}')


if __name__ == '__main__':
    seed = 47
    a = 53
    m = 1000

    congruencialMultiplicativo(seed, a , m)