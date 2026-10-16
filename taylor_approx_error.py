# Written By: Aditya Gundimeda

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(__file__).resolve().parent / "figures" # folder for figures
OUTPUT_DIR.mkdir(exist_ok=True)


t = np.arange(601, dtype=float) * 0.001 #generate 601 points between 0 and 0.6 of step size 0.001

f = np.exp(-t) # f(x) example function
p2 = 1.0 - t + (t ** 2) / 2.0 # Taylor polynomial

error = np.abs(f - p2) # abs error calculation from each sample point
B = (0.6 ** 3) / 6.0 # example theoretical maximum error

max_index = np.argmax(error) # returns index of largest element, use index to get error and error's t value

print("Q1(b) — Quadratic Taylor approximation")
print(f"Maximum sampled absolute error: {error[max_index]:.10f}")
print(f"Location of maximum error: t = {t[max_index]:.3f}")
print(f"Theoretical error bound: B = {B:.6f}")

fig, ax = plt.subplots(figsize=(8, 5)) # plot error (x = t, y = error)
ax.plot(t, error, linewidth=2,
        label=r"Absolute error $|f(t)-P_2(t)|$")
ax.axhline(B, color="tab:red", linestyle="--",
           linewidth=2, label=f"Taylor remainder bound B = {B:.3f}")

ax.set(xlabel="t", ylabel="Absolute error",
       title="Q1(b): Error in the Quadratic Taylor Approximation")
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
plot_path = OUTPUT_DIR / "q1b_error.png"
fig.savefig(plot_path, dpi=200)
plt.close(fig)

print(f"Plot saved to: {plot_path}")

# Written by: Aditya Gundimeda