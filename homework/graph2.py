import matplotlib.pyplot as plt
import numpy as np

def lagrangian(x, lambda_val):
    return (1 + lambda_val) * x**2 - 6 * lambda_val * x + (1 + 8 * lambda_val)


# Range of x values
x = np.linspace(-5, 5, 400)  # Adjusted range for x

# List of lambda values
lambda_values = [0, 1, 2, 3, 4]

# Plot L(x, lambda) for each lambda
for lambda_val in lambda_values:
    L_x = lagrangian(x, lambda_val)
    plt.plot(x, L_x, label=f'λ = {lambda_val}')

plt.xlabel('x')
plt.ylabel('L(x, λ)')
plt.title('Lagrangian L(x, λ) vs. x for Different λ')
plt.ylim(-5, 30)
plt.xlim(-1,5)
plt.legend()
plt.show()


