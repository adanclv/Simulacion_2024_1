import random as rand


def juegoVolado(cash):
    lost = 1
    while cash > 0 and cash < 50:
        x = rand.uniform(0.0, 1.0)
        if x > 0.5:
            if cash < (10 * lost):
                cash -= cash
            else:
                cash -= 10 * lost
                lost *= 2
        else:
            if cash < (10 * lost):
                cash += cash
            else:
                cash += 10 * lost
            lost = 1

    return cash


if __name__ == '__main__':
    won = 0
    n = 1000000
    for i in range(n):
        if juegoVolado(30) > 0:
            won += 1

    print(won / n)
