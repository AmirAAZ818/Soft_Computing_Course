from math import sin, pi

def michalewicz(x):
    m = 10
    n = len(x)
    result = 0
    for i in range(n):
        result -= sin(x[i]) * sin((i + 1) * x[i]**2 / pi)**(2 * m)
    return result
