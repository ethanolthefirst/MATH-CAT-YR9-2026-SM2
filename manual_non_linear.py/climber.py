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

path_x = [current_x]
path_y = [f(current_x)]

# Hill climbing loop with variable step reduction
while step_size > (target_tolerance / 10.0):
    left_y = f(current_x - step_size)
    right_y = f(current_x + step_size)
    current_y = f(current_x)
    
    if right_y > current_y:
        current_x += step_size
    elif left_y > current_y:
        current_x -= step_size
    else:
        # Peak bounded within current step size -> refine step size
        step_size /= 2.0
    path_x.append(current_x)
    path_y.append(f(current_x))

best_x = current_x
best_y = f(best_x)

print(f"Optimal x approx: {best_x:.4f}")
print(f"Maximum y approx: {best_y:.4f}")