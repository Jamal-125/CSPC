import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6

# TODO 1: Write k_imbalance(x)
def k_imbalance(x):
    return ((2*x)**2) / ((1 - x) * (1 - x)) - K

# TODO 2: Method 1 - Newton root-finding
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3: Method 2 - Minimize squared imbalance with SLSQP
res_slsqp = minimize(lambda x: k_imbalance(x)**2, x0=0.5, method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium extent x (Newton): {x_newton:.4f}")
print(f"Equilibrium extent x (SLSQP):  {x_slsqp:.4f}")

# TODO 4: Report amounts and plot
H2_eq = 1 - x_newton
I2_eq = 1 - x_newton
HI_eq = 2 * x_newton

print(f"Equilibrium amounts: H2 = {H2_eq:.4f} mol, I2 = {I2_eq:.4f} mol, HI = {HI_eq:.4f} mol")

x_vals = np.linspace(0, 0.9, 100)
plt.figure(figsize=(8, 6))
plt.plot(x_vals, 1 - x_vals, label='H2 & I2', color='blue')
plt.plot(x_vals, 2 * x_vals, label='HI', color='orange')
plt.axvline(x_newton, color='red', linestyle='--', label=f'Equilibrium x={x_newton:.2f}')
plt.xlabel('Extent of reaction x')
plt.ylabel('Amount (mol)')
plt.title('Chemical Equilibrium H2 + I2 <=> 2 HI')
plt.legend()
plt.grid(True)
plt.savefig("equilibrium.png", dpi=300)
print("Plot saved as equilibrium.png")