import random
import time
import matplotlib.pyplot as plt

print("--- Automated Hill Climbing Optimisation ---")
eq_str = input("Enter quadratic expression (e.g. -2*x**2 + 40*x): ")

def f(x):
    return eval(eq_str, {"x": x, "__builtins__": {}})

# Automatically determine coefficient 'a' via curve sampling
y0 = f(0.0)
y1 = f(1.0)
ymin1 = f(-1.0)
a_coeff = (y1 + ymin1 - 2 * y0) / 2.0

print(f"Detected quadratic coefficient a = {a_coeff:.4f}")
target_tolerance = 1.0 / (abs(a_coeff) ** 0.5)

# Initialize random start location within [-1000, 1000][cite: 17]
current_x = random.uniform(-500, 500)
step_size = 15.0

path_x = [current_x]
path_y = [f(current_x)]

# Pre-generate curve data for plotting background
x_range = [i * 0.5 for i in range(-400, 400)]
y_range = [f(x) for x in x_range]

# Set up live interactive plot window for animation
plt.ion()
fig, ax = plt.subplots(figsize=(9, 6))

# Hill climbing loop with live visual frame updates
while step_size > (target_tolerance / 10.0):
    left_y = f(current_x - step_size)
    right_y = f(current_x + step_size)
    current_y = f(current_x)
    
    if right_y > current_y:
        current_x += step_size
    elif left_y > current_y:
        current_x -= step_size
    else:
        step_size /= 2.0  # Refine step size when peak is bracketed[cite: 16]
        
    path_x.append(current_x)
    path_y.append(f(current_x))
    
    # Redraw frame for live animation effect
    ax.clear()
    ax.plot(x_range, y_range, color='gray', linewidth=2, label="Quadratic Curve")
    ax.plot(path_x, path_y, 'ro-', linewidth=2, markersize=6, label="Climber Search Path")
    ax.set_title(f"Hill Climbing in Progress (Step Size: {step_size:.3f})")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend(loc='lower center')
    plt.pause(0.04) # Controls animation speed

plt.ioff()
best_x = current_x
best_y = f(best_x)

print(f"\nOptimisation Complete!")
print(f"Approximate Peak x: {best_x:.4f}")
print(f"Approximate Peak y (Area/Max): {best_y:.4f}")

# Final static display showing the final peak marker
plt.figure(figsize=(9, 6))
plt.plot(x_range, y_range, color='gray', linewidth=2, label="Quadratic Curve")
plt.plot(path_x, path_y, 'ro-', label="Climber Path")
plt.plot(best_x, best_y, 'g*', markersize=18, label=f"Final Peak ({best_x:.2f}, {best_y:.2f})")
plt.title("Hill Climbing Optimisation Final Result")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='lower center')
plt.grid(True)
plt.show()