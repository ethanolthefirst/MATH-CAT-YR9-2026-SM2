import csv
import matplotlib.pyplot as plt
from statistics_library import minimum, maximum

x_vals, y_vals, colors = [], [], []

with open('linear_1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            x_vals.append(float(row[0]))
            y_vals.append(float(row[1]))
            colors.append(row[2].strip().lower())

# Automatic axis limits using custom statistics library functions
x_min, x_max = minimum(x_vals), maximum(x_vals)
y_min, y_max = minimum(y_vals), maximum(y_vals)

plt.figure()
for x, y, c in zip(x_vals, y_vals, colors):
    plt.scatter(x, y, color=c)

plt.xlim(x_min - 5, x_max + 5)
plt.ylim(y_min - 5, y_max + 5)
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.title("Linear Data Display")
plt.show()