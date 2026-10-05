import numpy as np
import matplotlib.pyplot as plt

# TODO 1: Read titration.csv
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# TODO 2: Compute slope and find equivalence point
slope = np.gradient(pH, V)
eq_index = np.argmax(slope)
eq_volume = V[eq_index]

print(f"Equivalence point volume: {eq_volume:.2f} mL")

# TODO 3: Plot titration curve and slope
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, color='purple', linewidth=2)
ax1.axvline(eq_volume, color='red', linestyle='--', label=f'Eq Point ({eq_volume:.1f} mL)')
ax1.set_xlabel('Volume of Base (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titration Curve')
ax1.grid(True)
ax1.legend()

ax2.plot(V, slope, color='green', linewidth=2)
ax2.axvline(eq_volume, color='red', linestyle='--', label=f'Peak ({eq_volume:.1f} mL)')
ax2.set_xlabel('Volume of Base (mL)')
ax2.set_ylabel('dpH / dV')
ax2.set_title('First Derivative (Slope)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("titration.png", dpi=300)
print("Plot saved as titration.png")