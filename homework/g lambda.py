import matplotlib.pyplot as plt
import numpy as np

# Define the Lagrange dual function g(λ)
def lagrange_dual_function(lambda_val):
    if lambda_val > -1:
        return -9 * lambda_val**2 / (1 + lambda_val) + 1 + 8 * lambda_val
    else:
        return -np.inf  # Negative infinity for λ < -1

# Range of λ values
lambda_values = np.linspace(-2, 10, 400)  # Adjusted range for λ

# Calculate g(λ) for each λ
g_lambda = [lagrange_dual_function(lambda_val) for lambda_val in lambda_values]

plt.plot(lambda_values, g_lambda)
plt.xlabel('λ')
plt.ylabel('g(λ)')
plt.title('Lagrange Dual Function g(λ) vs. λ')
plt.ylim(-10, 8)
plt.xlim(-2,4)
plt.axvline(x=-1, color='black', linestyle='--')
plt.show()
