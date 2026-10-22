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

best_r = 0
best_acc = -1

# Systematic sweep across the transition zone where red/blue clusters divide (10 to 70)
r_curr = 10.0
while r_curr <= 70.0:
    acc = evaluate_circle(r_curr, x_vals, y_vals, colors)
    if acc > best_acc:
        best_acc = acc
        best_r = r_curr
    r_curr += 0.25

print(f"Optimal Radius Found: {best_r:.2f} | Maximum Accuracy: {best_acc:.2f}%")

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
plt.title("Automated Non-Linear Circular Classification")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()