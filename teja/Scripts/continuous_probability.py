import numpy as np
import matplotlib.pyplot as plt

# Parameters of the normal distribution
mu = 0  # Mean
sigma = 1  # Standard deviation

# Generate 10000 random numbers from the normal distribution
x = np.random.normal(mu, sigma, 10000)

# Plot the histogram
plt.hist(x, bins=50, density=True, alpha=0.6, color='g')

# Plot the theoretical PDF
x_axis = np.linspace(-4, 4, 100)
plt.plot(x_axis, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x_axis - mu)**2 / (2 * sigma**2) ), linewidth=2, color='b')

plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.show()