import math

if __name__ == '__main__':
    file = open('apendice_A.txt','r')
    elem = file.read().strip().split('\n')
    num = [float(e) for e in elem]

    promedio = sum(num) / len(num)
    z = (promedio - 0.5) * math.sqrt(len(num))
    z = z / math.sqrt(1/12)

    if z < 1.96:
        print('Si son aleatorios')
    else:
        print('No son aleatorios')