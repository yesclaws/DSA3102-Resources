import matplotlib.pyplot as plt
import numpy as np

# Create a range of x values
x = np.linspace(-10, 10, 400)  # Adjust the range and number of points as needed

# Calculate the corresponding y values for y = x^2 + 1
y = x**2 + 1

# Calculate the corresponding y values for the inequality (x-2)(x-4) <= 0
inequality_y = (x-2)*(x-4)

# Create the plot for y = x^2 + 1
plt.plot(x, y, label='y = x^2 + 1')

# Plot the graph of the inequality (x-2)(x-4) <= 0
plt.plot(x, inequality_y, label='(x-2)(x-4) <= 0')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x^2 + 1 and (x-2)(x-4) <= 0')
plt.legend()
plt.xlim(0,5)
plt.ylim(-5, 30)
plt.axhline(y=0, color='black', label='y = 0')

plt.xlabel('x')

plt.fill_betweenx(y, -np.inf, np.inf, where=(x >= 2) & (x <= 4), color='gray', alpha=0.5)

# Show the plot
plt.show()


