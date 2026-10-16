import matplotlib.pyplot as plt

eq_input = input("Enter quadratic equation (e.g. 40*x - 2*x**2): ")
x_min = float(input("Enter min x: "))
x_max = float(input("Enter max x: "))
y_min = float(input("Enter min y: "))
y_max = float(input("Enter max y: "))

x_values = []
y_values = []

x = x_min
while x <= x_max:
    x_values.append(x)
    # Safely evaluate mathematical expression in x
    y = eval(eq_input, {"x": x, "__builtins__": {}})
    y_values.append(y)
    x += 0.05