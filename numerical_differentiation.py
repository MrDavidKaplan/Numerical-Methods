
# Written By: Aditya Gundimeda

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(__file__).resolve().parent / "figures" # folder for figures
OUTPUT_DIR.mkdir(exist_ok=True)

t0 = 0.3
true_derivative = -np.exp(-t0) # exact derivative of f(t) at t = 0.3

def f(t):
    return np.exp(-t)

def forward_difference(t, h):
    return (f(t + h) - f(t)) / h

def centered_difference(t, h):
    return (f(t + h) - f(t - h)) / (2.0 * h)

h_values = np.geomspace(0.3, 1e-16, 200) # 200 logarithmically spaced step sizes

forward_estimates = forward_difference(t0, h_values)
centered_estimates = centered_difference(t0, h_values)

forward_errors = np.abs(forward_estimates - true_derivative) # absolute errors
centered_errors = np.abs(centered_estimates - true_derivative)

best_f = np.argmin(forward_errors) # index of smallest forward error
best_c = np.argmin(centered_errors) # index of smallest centered error

recommended_h = 1e-5
recommended_estimate = centered_difference(t0, recommended_h)
recommended_error = abs(recommended_estimate - true_derivative)

print("Q1(d) — Numerical differentiation")
print(f"Exact derivative: {true_derivative:.15f}")

print("\n      h      Forward error     Centered error")
for h in [0.3, 1e-1, 1e-2, 1e-4, 1e-5, 1e-6, 1e-8, 1e-12, 1e-15]:
    f_error = abs(forward_difference(t0, h) - true_derivative)
    c_error = abs(centered_difference(t0, h) - true_derivative)
    print(f"{h:10.1e}    {f_error:14.6e}    {c_error:14.6e}")

print(f"\nBest forward step: h = {h_values[best_f]:.3e}")
print(f"Best forward error: {forward_errors[best_f]:.3e}")
print(f"Best centered step: h = {h_values[best_c]:.3e}")
print(f"Best centered error: {centered_errors[best_c]:.3e}")
print(f"Recommended method: Centered difference")
print(f"Recommended step: h = {recommended_h:g}")
print(f"Recommended estimate: {recommended_estimate:.15f}")
print(f"Recommended error: {recommended_error:.3e}")

fig, ax = plt.subplots(figsize=(8, 5))

ax.loglog(h_values, forward_errors, linewidth=2,
          label="Forward difference")
ax.loglog(h_values, centered_errors, linewidth=2,
          label="Centered difference")

ax.axvline(recommended_h, color="gray", linestyle="--",
           label="Recommended h = 1e-5")

ax.set(xlabel="Step size h (log scale)",
       ylabel="Absolute error (log scale)",
       title="Q1(d): Numerical Differentiation Error")
ax.grid(True, which="both", alpha=0.3)
ax.legend()

fig.tight_layout()
plot_path = OUTPUT_DIR / "q1d_derivative_errors.png"
fig.savefig(plot_path, dpi=200)
plt.close(fig)

print(f"Plot saved to: {plot_path}")

# Written by: Aditya Gundimeda
