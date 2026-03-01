import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81
v0 = 20
theta = np.radians(45)

# Time array
t = np.linspace(0, 3, 100)

# Equations of motion
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

range_estimate = (v0**2 * np.sin(2*theta)) / g
print("Estimated Range:", range_estimate)

# Plot
plt.plot(x, y)
plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.title("Projectile Motion Simulation")
plt.grid(True)
plt.show()