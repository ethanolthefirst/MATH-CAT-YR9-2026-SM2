import random
import matplotlib.pyplot as plt

# Prompt for expression and quadratic coefficient 'a'
eq_str = input("Enter quadratic string (e.g. -2*x**2 + 40*x): ")
a_coeff = float(input("Enter value of coefficient 'a' (must be negative): "))

def f(x):
    return eval(eq_str, {"x": x, "__builtins__": {}})

target_tolerance = 1.0 / (abs(a_coeff) ** 0.5)

# Pick random start within [-1000, 1000]
current_x = random.uniform(-1000, 1000)
step_size = 10.0