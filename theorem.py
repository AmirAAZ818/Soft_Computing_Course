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
#----------------------------------------------------------------------------------
# Booth function

def booth(x):
    return (x[0] + 2 * x[1] - 7)**2 + (2 * x[0] + x[1] - 5)**2
#----------------------------------------------------------------
# Bukin function N.6

def bukin_n6(x):
    return 100 * np.sqrt(np.abs(x[1] - 0.01*x[0]**2)) + 0.01*np.abs(x[0] + 10)
#-------------------------------------------------------------------------------
# Cross-in-Italy function

def cross_in_italy(x):
    return -0.0001 * (np.abs(np.sin(x[0]) * np.sin(x[1]) * np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2)/np.pi))) + 1)
#-----------------------------------------------------------------------------------------------------------------------------
# Holder table function

def holder_table(x):
    num = -np.abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi))
                  * np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi)))
    den = 1 + np.abs(x[0] + x[1]) * np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi))
    return num / den
#----------------------------------------------------------------------------------------------------
# McComick function

def mccormick(x):
    return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1
#-----------------------------------------------------------------------------
# Schaffer function N.1

def schaffer_n1(x):
    return x**2
#------------------------------
# Schaffer function N.2

def schaffer_n2(x):
    return x**2
#------------------------------
# Poloni's two objective function

def polonis_two_objective(x):
    f1 = (1 - np.exp(-(x[0]-1)**2 - (x[1]+1)**2)) / 0.45
    f2 = (2.0 * (x[0]-0.5)**2 + 2.0 * (x[1]-0.5)**2)
    return f1, f2
#-----------------------------------------------------------
