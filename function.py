import re


def openFile(nameFile):
    a = []
    b = []
    file = open(nameFile, 'r')
    lines = file.read()

    for line in lines.split('\n'):
        x, y = (re.split('\s+', line))
        a.append(float(x))
        b.append(float(y))
    return a, b


def funLagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z