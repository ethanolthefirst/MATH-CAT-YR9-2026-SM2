import csv
import random
from pathlib import Path
import matplotlib.pyplot as plt

def evaluate_line(m, c, x_vals, y_vals, colors):
    s1 = sum((y >= m*x + c and col == 'red') or (y < m*x + c and col == 'blue') for x, y, col in zip(x_vals, y_vals, colors))
    s2 = sum((y >= m*x + c and col == 'blue') or (y < m*x + c and col == 'red') for x, y, col in zip(x_vals, y_vals, colors))
    return max(s1, s2) / len(x_vals) * 100.0

x_vals, y_vals, colors = [], [], []
with (Path(__file__).resolve().parent / 'linear_1.csv').open('r') as f:
    for row in csv.reader(f):
        if row:
            x_vals.append(float(row[0]))
            y_vals.append(float(row[1]))
            colors.append(row[2].strip().lower())

trials = int(input("Enter number of trials: "))

best_acc = -1
best_m, best_c = 0, 0

for _ in range(trials):
    m_rand = random.uniform(-10, 10)
    c_rand = random.uniform(-100, 100)
    acc = evaluate_line(m_rand, c_rand, x_vals, y_vals, colors)
    if acc > best_acc:
        best_acc = acc
        best_m = m_rand
        best_c = c_rand

print(f"Best Line: y = {best_m:.2f}x + {best_c:.2f} | Accuracy: {best_acc:.2f}%")

for x, y, col in zip(x_vals, y_vals, colors):
    plt.scatter(x, y, color=col)

x_line = [min(x_vals), max(x_vals)]
y_line = [best_m * x + best_c for x in x_line]
plt.plot(x_line, y_line, color='black', label=f'Best Line ({best_acc:.1f}%)')
plt.legend()
plt.show()