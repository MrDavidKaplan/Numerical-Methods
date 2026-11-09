
import numpy as np
import matplotlib.pyplot as plt

# Q1(c): Jacobi and Gauss-Seidel
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 3]], dtype=float)
b = np.array([2, 4, 7], dtype=float)

def residual(x):
    return np.linalg.norm(A @ x - b, np.inf) / np.linalg.norm(b, np.inf)

def solve(method):
    x = np.zeros(3)
    errors = [residual(x)]

    for k in range(1, 501):
        old = x.copy()

        if method == "Jacobi":
            x = np.array([
                (2 + old[1]) / 4,
                (4 + old[0] + old[2]) / 4,
                (7 + old[1]) / 3
            ])
        else:
            x[0] = (2 + old[1]) / 4
            x[1] = (4 + x[0] + old[2]) / 4
            x[2] = (7 + x[1]) / 3

        errors.append(residual(x))
        if errors[-1] < 1e-6:
            break

    return x, errors

plt.figure()
for method in ["Jacobi", "Gauss-Seidel"]:
    x, errors = solve(method)
    print(f"{method}: k={len(errors)-1}, x={x}, residual={errors[-1]:.3e}")
    plt.semilogy(range(len(errors)), errors, marker="o", label=method)

plt.axhline(1e-6, color="gray", linestyle="--", label="Tolerance")
plt.xlabel("Iteration k")
plt.ylabel("Relative infinity-norm residual")
plt.title("Q1: Iterative Method Convergence")
plt.legend()
plt.grid(True)
plt.tight_layout()


# Q2(b): Matrix iteration
M = np.array([[3, 1], [1, 3]], dtype=float) / 5
X = np.zeros((26, 2))
X[0] = [2, 0]

for k in range(25):
    X[k + 1] = M @ X[k]

plt.figure()
plt.plot(range(26), X[:, 0], "o-", label="x1")
plt.plot(range(26), X[:, 1], "s-", label="x2")
plt.xlabel("Iteration k")
plt.ylabel("Component value")
plt.title("Q2: Matrix Iteration")
plt.legend()
plt.grid(True)
plt.tight_layout()


# Q3(c): Compare singular values
C = np.array([[1, 2], [-2, -1]])
C_new = np.array([[1, 2], [2, -1]])

print("Original singular values:", np.linalg.svd(C, compute_uv=False))
print("Corrected singular values:", np.linalg.svd(C_new, compute_uv=False))

plt.show()
