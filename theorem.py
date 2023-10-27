from math import cos, sqrt,sin,pi,prod
#-------------------------------------------------------------------------
# The two Demensional Griewank's function

def fGriewank(x, y):
    return (x**2 + y**2) / 4000 - cos(x / sqrt(2)) * cos(y / sqrt(3)) + 1
#-------------------------------------------------------------------------
# The Griewank's function

def griewank(x):
    n = len(x)
    s = sum([xi**2 for xi in x]) / 4000
    p = prod([cos(xi / sqrt(i + 1)) for i, xi in enumerate(x)])
    return 1 + s - p
#------------------------------------------------------------------------------
# The Michalewicz's function

def michalewicz(x):
    m =10
    n = len(x)
    result = 0
    for i in range(n):
        result -= sin(x[i]) * sin((i + 1) * x[i]**2 / pi)**(2 * m)
    return result
#-------------------------------------------------------------------
# The Rastrigin's Function

def rastrigin(x):
    A = 10
    n = len(x)
    sum_term = sum([(xi**2 - A * cos(2 * pi * xi)) for xi in x])
    return A * n + sum_term
#-------------------------------------------------------------------
# The 2 variable Rosenbrock's function

def rosenbrock(x, y):
    a = 1
    b = 100
    return (a - x) ** 2 + b * (y - x ** 2) ** 2
#--------------------------------------------------------
