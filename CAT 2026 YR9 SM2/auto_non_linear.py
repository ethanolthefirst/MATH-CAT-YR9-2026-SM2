import csv
from pathlib import Path
import matplotlib.pyplot as plt

def evaluate_circle(r, x_vals, y_vals, colors):
    s1 = sum((x**2 + y**2 <= r**2 and col == 'red') or (x**2 + y**2 > r**2 and col == 'blue') for x, y, col in zip(x_vals, y_vals, colors))
    s2 = sum((x**2 + y**2 <= r**2 and col == 'blue') or (x**2 + y**2 > r**2 and col == 'red') for x, y, col in zip(x_vals, y_vals, colors))
    return max(s1, s2) / len(x_vals) * 100.0

# Load dataset with robust parsing
x_vals, y_vals, colors = [], [], []
with (Path(__file__).resolve().parent / 'non_linear_1.csv').open('r') as f:
    for row in csv.reader(f):
        if row:
            x_vals.append(float(row[0]))
            y_vals.append(float(row[1]))
            colors.append(row[2].strip().lower())

print("Running advanced systematic non-linear search...")
best_r = 0
best_acc = -1

# High-precision sweep algorithm from r = 0 to 142 with 0.1 step increments
r_curr = 0.0
while r_curr <= 142.0:
    acc = evaluate_circle(r_curr, x_vals, y_vals, colors)
    if acc > best_acc:
        best_acc = acc
        best_r = r_curr
    r_curr += 0.1

print(f"Optimal Radius Found: {best_r:.2f} | Maximum Accuracy: {best_acc:.2f}%")

# Plotting results
fig, ax = plt.subplots(figsize=(8, 8))
for x, y, col in zip(x_vals, y_vals, colors):
    ax.scatter(x, y, color=col, alpha=0.8)

circle = plt.Circle((0, 0), best_r, fill=False, color='black', linewidth=2.5, label=f'Optimal r = {best_r:.2f} ({best_acc:.1f}%)')
ax.add_patch(circle)
ax.set_aspect('equal')
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Automated Non-Linear Circular Classification Optimisation")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()