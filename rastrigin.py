from math import pi,cos,sqrt

def rastrigin(x, A=10):
    n = len(x)
    sum_term = sum([(xi**2 - A * cos(2 * pi * xi)) for xi in x])
    return A * n + sum_term
