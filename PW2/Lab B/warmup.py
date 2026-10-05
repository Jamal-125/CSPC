import numpy as np
from scipy.optimize import newton, minimize

# --- 2A: Easy convex function ---
def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def d2f(x):
    return 2.0

# 1. Gradient descent by hand
x_gd = 0.0
lr = 0.1
for _ in range(100):
    x_gd = x_gd - lr * df(x_gd)

# 2. Newton's method
x_newton = newton(df, x0=0.0, fprime=d2f)

# 3. SLSQP minimize
res_slsqp = minimize(f, x0=0.0, method="SLSQP")

print("--- Part 2A ---")
print(f"Gradient Descent: x = {x_gd:.4f}")
print(f"Newton: x = {x_newton:.4f}")
print(f"SLSQP: x = {res_slsqp.x[0]:.4f}")

# --- 2B: Harder landscape ---
def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

print("\n--- Part 2B ---")
for x0 in [0.0, 2.0]:
    # Newton
    x_n = newton(dg, x0=x0, fprime=d2g)
    curv = d2g(x_n)
    pt_type = "minimum" if curv > 0 else "maximum"
    
    # SLSQP
    res_s = minimize(g, x0=x0, method="SLSQP")
    
    print(f"\nStart x0 = {x0}:")
    print(f"  Newton: x = {x_n:.4f} ({pt_type}, d2g = {curv:.2f})")
    print(f"  SLSQP:  x = {res_s.x[0]:.4f}")