import csv
import random
from pathlib import Path
import matplotlib.pyplot as plt

def evaluate_line(m, c, x_vals, y_vals, colors):
    s1 = 0
    s2 = 0
    total = len(x_vals)
    for x, y, col in zip(x_vals, y_vals, colors):
        above = y >= (m * x + c)
        if (above and col == 'red') or (not above and col == 'blue'):
            s1 += 1
        if (above and col == 'blue') or (not above and col == 'red'):
            s2 += 1
    return max(s1, s2) / total * 100.0

x_vals, y_vals, colors = [], [], []
data_file = Path(__file__).resolve().parent / 'linear_1.csv'
with data_file.open('r', newline='') as f:
    for row in csv.reader(f):
        if row:
            x_vals.append(float(row[0]))
            y_vals.append(float(row[1]))
            colors.append(row[2].strip().lower())

trials = int(input("Enter number of trials (e.g. 5000): "))

best_acc = -1
best_m, best_c = 0, 0

for _ in range(trials):
    # Focused search ranges ensuring valid line separation across the data gap
    m_rand = random.uniform(0.5, 3.0)
    c_rand = random.uniform(-80.0, 0.0)
    
    acc = evaluate_line(m_rand, c_rand, x_vals, y_vals, colors)
    if acc > best_acc:
        best_acc = acc
        best_m = m_rand
        best_c = c_rand

print(f"Best Line: y = {best_m:.2f}x + {best_c:.2f} | Accuracy: {best_acc:.2f}%")

plt.figure(figsize=(8, 6))
for x, y, col in zip(x_vals, y_vals, colors):
    plt.scatter(x, y, color=col)

x_line = [min(x_vals), max(x_vals)]
y_line = [best_m * x + best_c for x in x_line]
plt.plot(x_line, y_line, color='black', linewidth=2, label=f'Best Line ({best_acc:.1f}%)')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.title("Automated Linear Classification (Random Search)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()