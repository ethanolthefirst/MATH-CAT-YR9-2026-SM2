import csv
from pathlib import Path
import matplotlib.pyplot as plt

def evaluate_circle(r, x_vals, y_vals, colors):
    # Distance from origin: x^2 + y^2 <= r^2
    s1 = sum((x**2 + y**2 <= r**2 and col == 'red') or (x**2 + y**2 > r**2 and col == 'blue') for x, y, col in zip(x_vals, y_vals, colors))
    s2 = sum((x**2 + y**2 <= r**2 and col == 'blue') or (x**2 + y**2 > r**2 and col == 'red') for x, y, col in zip(x_vals, y_vals, colors))
    return max(s1, s2) / len(x_vals) * 100.0

x_vals, y_vals, colors = [], [], []
with (Path(__file__).resolve().parent / 'non_linear_1.csv').open('r') as f:
    for row in csv.reader(f):
        if row:
            x_vals.append(float(row[0]))
            y_vals.append(float(row[1]))
            colors.append(row[2].strip().lower())

r = float(input("Enter circle radius (r): "))
acc = evaluate_circle(r, x_vals, y_vals, colors)
print(f"Accuracy: {acc:.2f}%")

fig, ax = plt.subplots()
for x, y, col in zip(x_vals, y_vals, colors):
    ax.scatter(x, y, color=col)

circle = plt.Circle((0, 0), r, fill=False, color='black', linewidth=2)
ax.add_patch(circle)
ax.set_aspect('equal')
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()