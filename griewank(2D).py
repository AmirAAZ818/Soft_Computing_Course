from math import cos, sqrt

def fGriewank(x, y):
    return (x**2 + y**2) / 4000 - cos(x / sqrt(2)) * cos(y / sqrt(3)) + 1
# The two Demensional Griewank function
