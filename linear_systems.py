
# Written By: Aditya Gundimeda

import numpy as np

A = np.array([
    [0, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
], dtype=float) # coefficient matrix

b = np.array([1, 1, 3], dtype=float) # original target readings
b_hat = np.array([1, 1, 2], dtype=float) # modified target readings

def evaluate_target(name, target):
    solution = np.linalg.solve(A, target) # solves Ax = b
    residual = A @ solution - target # matrix multiplication and residual

    feasible = np.all(solution >= -1e-12) # checks nonnegative dye amounts (with rounding tolerance)

    print(f"\n{name}")
    print(f"Solution: {solution}")
    print(f"Residual: {residual}")
    print(f"Feasible mixture: {'Yes' if feasible else 'No'}")

    return solution, residual, feasible

print("Q3(b) — Linear Systems")

evaluate_target("Original target b = [1, 1, 3]", b)
evaluate_target("Modified target b = [1, 1, 2]", b_hat)

# Written by: Aditya Gundimeda
