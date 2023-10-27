from math import cos,sqrt,sin,pi,prod,exp
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
def fitness_function(chromosome):
    
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    fitness = - (x**2 + y**2 + z**2)
    return fitness
#---------------------------------------------------------
def fitness_function(chromosome):
    
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    fitness = math.sin(x) + math.cos(y) + math.tan(z)
    return fitness
#------------------------------------------------------
def fitness_function(chromosome):
    
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    fitness = math.sin(x) + math.cos(y) + math.tan(z)
    return fitness
#-------------------------------------------------------

def fitness_function(chromosome):
    
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    # objective function value
    obj = x * math.sin(y) + y * math.cos(z) + z * math.sin(x)
    # penalty term
    penalty = 0
    # check if any constraint is violated and add a penalty accordingly
    if x + y > 10:
        penalty += (x + y - 10)**2
    if x - z < 0:
        penalty += (x - z)**2
    if x < 0 or y < 0 or z < 0:
        penalty += (x**2 + y**2 + z**2)
    # fitness score is the objective function value minus the penalty term
    fitness = obj - penalty
    return fitness
#----------------------------------------------------------------------------

def f(chro1, chro2):
    value = (1 + cos(2 * pi * chro1 * chro2)) * exp(- (abs(chro1) + abs(chro2)) / 2)
    return value
#--------------------------------------------------------------------------
def f(chromosome):
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    w = chromosome[3]
    obj = x * sin(y) + y * cos(z) + z * sin(w) + w * cos(x)
    penalty = 0
    # check if any constraint is violated and add a penalty accordingly
    if x + y + z + w > 10:
        penalty += (x + y + z + w - 10)**2
    if x - z < 0:
        penalty += (x - z)**2
    if y - w < 0:
        penalty += (y - w)**2
    if x < 0 or y < 0 or z < 0 or w < 0:
        penalty += (x**2 + y**2 + z**2 + w**2)
    # fitness score is the objective function value minus the penalty term
    fitness = obj - penalty
    return fitness
