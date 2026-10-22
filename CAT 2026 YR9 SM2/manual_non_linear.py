import csv
from pathlib import Path
import matplotlib.pyplot as plt

def evaluate_circle(r, x_vals, y_vals, colors):
    s1 = 0
    s2 = 0
    total = len(x_vals)
    for x, y, col in zip(x_vals, y_vals, colors):
        inside = (x**2 + y**2) <= (r**2)
        if (inside and col == 'red') or (not inside and col == 'blue'):
            s1 += 1
        if (inside and col == 'blue') or (not inside and col == 'red'):
            s2 += 1
    return max(s1, s2) / total * 100.0

x_vals, y_vals, colors = [], [], []
data_file = Path(__file__).resolve().parent / 'non_linear_1.csv'
with data_file.open('r', newline='') as f:
    for row in csv.reader(f):
        if row:
            x_vals.append(float(row[0]))
            y_vals.append(float(row[1]))
            colors.append(row[2].strip().lower())

r = float(input("Enter circle radius (r): "))
acc = evaluate_circle(r, x_vals, y_vals, colors)
print(f"Classification Accuracy: {acc:.2f}%")

fig, ax = plt.subplots(figsize=(8, 8))
for x, y, col in zip(x_vals, y_vals, colors):
    ax.scatter(x, y, color=col, alpha=0.8)

circle = plt.Circle((0, 0), r, fill=False, color='black', linewidth=2.5, label=f'Radius r = {r} ({acc:.1f}%)')
ax.add_patch(circle)
ax.set_aspect('equal')
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Manual Non-Linear Circular Classification")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()