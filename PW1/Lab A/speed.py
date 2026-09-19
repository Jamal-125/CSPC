import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.1

print("Slow (simulate_loop)...")
start_loop = time.perf_counter()
simulate_loop(N0, lam)
end_loop = time.perf_counter()
time_loop = end_loop - start_loop

print("Fast (simulate c NumPy)...")
start_np = time.perf_counter()
simulate(N0, lam)
end_np = time.perf_counter()
time_numpy = end_np - start_np

speed_up = time_loop / time_numpy

print("\n=== Compare ===")
print(f"loop : {time_loop:.4f} s")
print(f"numpy : {time_numpy:.4f} s")
print(f"speed-up: {speed_up:.1f} x faster")