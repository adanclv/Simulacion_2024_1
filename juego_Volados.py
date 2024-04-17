import random as rand


def juegoVolado(cash):
    lost = 1
    win = 0
    while cash > 0 and win < 3:
        x = rand.randint(0, 1)
        if x == 0:
            if cash < (10 * lost):
                cash -= cash
            else:
                cash -= 10 * lost
                lost *= 2
        else:
            cash += 10 * lost
            lost = 1
            win += 1

    return cash


if __name__ == '__main__':
    won = 0
    n = 1000000
    for i in range(n):
        if juegoVolado(30) > 0:
            won += 1

    print(won / n)
