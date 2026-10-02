import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

mean_a = np.mean(a)
std_a = np.std(a)

print(f"Mean acceleration:{mean_a:.2f} m/s^2")
print(f"Standart deviation of acceleration: {std_a:.2f} m/s^2")

v_recovered = cumulative_trapezoid(a, x=t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, x=t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_recovered))
print(f"Max difference in recovered position: {max_diff:.4f} m")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax1.plot(t, y, label="Measured Position", color="blue")
ax1.set_ylabel("Position (m)")
ax1.set_title("Motion Analysis from Tracking Data")
ax1.grid(True)
ax1.legend()

ax2.plot(t, v, label="Calculated Velocity", color="orange")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)
ax2.legend()

ax3.plot(t, a, label="Calculated Acceleration", color="green", alpha=0.7)
ax3.axhline(-9.81, color="red", linestyle="--", label="Target g (-9.81 m/s^2)")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Acceleration (m/s^2)")
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=300)
print("Plot saved as motion.png")