import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import math

# --- Function to simulate complexity ---
def sample_function(n):
    n = float(n)
    j = 5
    Sum=0
    while j < np.log(n):  # Outer loop
        k = 5
        while k < n:      # Inner loop
            Sum+=j*k
            k = int(k ** 1.5)
        j = int(1.2 * j)

# --- n values ---
n_values = [100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000,
            10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000]

# --- Theoretical values ---
theoretical = [(np.log(np.log(float(n))))**2 for n in n_values]

# --- Experimental times (ns) ---
experimental_times = []
for n in n_values:
    start = time.perf_counter()
    sample_function(n)
    end = time.perf_counter()
    experimental_times.append((end - start) * 1e9)  # convert seconds → nanoseconds

# --- Scaling constant using median ratio ---
ratios = [exp / theo for exp, theo in zip(experimental_times, theoretical)]
scaling_constant = np.median(ratios)

# --- Scaled theoretical ---
scaled_theoretical = [t * scaling_constant for t in theoretical]

# --- Table ---
df = pd.DataFrame({
    "n": n_values,
    "Experimental (ns)": experimental_times,
    "Theoretical": theoretical,
    "Ratio (Exp/Theo)": ratios,
    "Scaling Constant (median)": [scaling_constant]*len(n_values),
    "Scaled Theoretical (ns)": scaled_theoretical
})

print(df.to_string(index=False))

# --- Plot ---
plt.figure(figsize=(7,4))
plt.plot(n_values, experimental_times, 'o-', label="Experimental (ns)", linewidth=2, markersize=6)
plt.plot(n_values, scaled_theoretical, 's--', label=r"Scaled Theoretical $(\log \log n)^2$", linewidth=2, markersize=6)

plt.xscale("log")
plt.yscale("log")
plt.xlabel("n (log scale)")
plt.ylabel("Time (nanoseconds, log scale)")
plt.title("Experimental vs Scaled Theoretical Complexity (Median Scaling)")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.6)
plt.tight_layout()
plt.show()
