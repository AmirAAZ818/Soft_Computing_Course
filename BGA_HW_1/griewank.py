import math


def griewank(x):
    n = len(x)
    s = sum([xi**2 for xi in x]) / 4000
    p = math.prod([math.cos(xi / math.sqrt(i + 1)) for i, xi in enumerate(x)])
    return 1 + s - p
# it is griewank function
