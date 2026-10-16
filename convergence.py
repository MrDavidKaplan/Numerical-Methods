
# Written By: Aditya Gundimeda

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(__file__).resolve().parent / "figures" # folder for figures
OUTPUT_DIR.mkdir(exist_ok=True)

q = 0.99
C = q / (1.0 - q) # error-to-change ratio
tau = 0.01 / C # stopping threshold for target error
MAX_UPDATES = 1000

def run_until_stop(q_value, threshold):
    x = 0.0 # initial value x_0
    history = [x] # stores all values of the sequence

    for k in range(1, MAX_UPDATES + 1):
        new_x = q_value * x + (1.0 - q_value) # recurrence formula
        delta = abs(new_x - x) # change between consecutive values

        x = new_x
        history.append(x)

        if delta < threshold:
            return k, x, abs(x - 1.0), history, True

    return MAX_UPDATES, x, abs(x - 1.0), history, False

rule1 = run_until_stop(q, 0.01) # first stopping rule
rule2 = run_until_stop(q, tau) # second stopping rule

print("Convergence and Stopping Criteria")
print(f"C = {C:.0f}")
print(f"Tau = {tau:.12f}")

for name, result in [("Rule 1", rule1), ("Rule 2", rule2)]:
    k, x, error, history, met = result

    print(f"\n{name}")
    if met:
        print(f"Stopping index: k = {k}")
    else:
        print("criterion not met after 1000 updates")

    print(f"Final value: x = {x:.12f}")
    print(f"Final error: e = {error:.12f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5)) # two graphs in one figure

for q_value in [0.5, -0.5, 0.99, 1.01]:
    sequence = [0.0]

    for k in range(30):
        sequence.append(q_value * sequence[-1] + (1.0 - q_value))

    ax1.plot(range(31), sequence, linewidth=2,
             label=f"q = {q_value}")

ax1.axhline(1.0, color="black", linestyle=":", label="Target x = 1")
ax1.set(xlabel="Iteration k", ylabel="Value x_k",
        title="Convergence for Different q Values")
ax1.grid(True, alpha=0.3)
ax1.legend()

errors = np.abs(np.array(rule2[3]) - 1.0) # errors through the second stopping point

ax2.plot(range(len(errors)), errors, linewidth=2,
         label="Error for q = 0.99")
ax2.axhline(0.01, color="black", linestyle="--",
            label="Target error = 0.01")

for name, result, color in [("Rule 1", rule1, "tab:orange"),
                            ("Rule 2", rule2, "tab:green")]:
    if result[4]:
        ax2.scatter(result[0], result[2], color=color, s=75,
                    zorder=5, label=f"{name} (k = {result[0]})")

ax2.set_yscale("log") # logarithmic error axis
ax2.set(xlabel="Iteration k", ylabel="Absolute error (log scale)",
        title="Error and Stopping Points for q = 0.99")
ax2.grid(True, which="both", alpha=0.3)
ax2.legend()

fig.tight_layout()
plot_path = OUTPUT_DIR / "convergence.png"
fig.savefig(plot_path, dpi=200)
plt.close(fig)

print(f"\nPlot saved to: {plot_path}")

# Written by: Aditya Gundimeda
