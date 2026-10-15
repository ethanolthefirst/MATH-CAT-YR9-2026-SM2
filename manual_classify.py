import csv
import matplotlib.pyplot as plt

def evaluate_line(m, c, x_vals, y_vals, colors):
    score1_correct = 0
    score2_correct = 0
    
    for x, y, color in zip(x_vals, y_vals, colors):
        above_line = y >= (m * x + c)
        
        # Rule 1: Above line = Red, Below line = Blue
        if (above_line and color == 'red') or (not above_line and color == 'blue'):
            score1_correct += 1
            
        # Rule 2: Above line = Blue, Below line = Red
        if (above_line and color == 'blue') or (not above_line and color == 'red'):
            score2_correct += 1
            
    best_score = max(score1_correct, score2_correct) / len(x_vals) * 100.0
    return best_score

x_vals, y_vals, colors = [], [], []
with open('linear_1.csv', 'r') as f:
    for row in csv.reader(f):
        if row:
            x_vals.append(float(row[0]))
            y_vals.append(float(row[1]))
            colors.append(row[2].strip().lower())

m = float(input("Enter gradient (m): "))
c = float(input("Enter y-intercept (c): "))

acc = evaluate_line(m, c, x_vals, y_vals, colors)
print(f"Classification Accuracy: {acc:.2f}%")

for x, y, col in zip(x_vals, y_vals, colors):
    plt.scatter(x, y, color=col)

# Plot decision line
x_line = [min(x_vals), max(x_vals)]
y_line = [m * x + c for x in x_line]
plt.plot(x_line, y_line, color='black', label=f'y = {m}x + {c}')
plt.legend()
plt.show()