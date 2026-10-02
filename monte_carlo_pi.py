import random
import matplotlib.pyplot as plt

# Monte Carlo simulation to estimate pi
inside_circle = 0
total_points = 1_000_000
points_x = []
points_y = []
colors = []

for _ in range(total_points):
    # Generate random points in the range [-1, 1]
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    distance = x**2 + y**2
    points_x.append(x)
    points_y.append(y)

    if distance <= 1:
        inside_circle += 1
        colors.append("blue")
    else:
        colors.append("red")

# Estimate pi
pi_estimate = (inside_circle / total_points) * 4
print(f"Estimated pi: {pi_estimate}")

# Plot points
plt.figure(figsize=(6, 6))
plt.scatter(points_x, points_y, c=colors, s=1)
plt.title(f"Monte Carlo Estimation of pi: {pi_estimate}")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect("equal", adjustable="box")
plt.show()
