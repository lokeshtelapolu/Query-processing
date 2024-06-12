import matplotlib.pyplot as plt
import numpy as np

# Generate random data points
np.random.seed(0)  # for reproducibility
num_points = 100
x = np.random.randn(num_points)
y = np.random.randn(num_points)

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.5)  # alpha controls transparency
plt.title('Random Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)  # Show grid
plt.show()
