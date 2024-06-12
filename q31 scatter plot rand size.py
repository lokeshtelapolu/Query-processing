import matplotlib.pyplot as plt
import numpy as np

# Generate random data points
np.random.seed(0)  # for reproducibility
num_points = 100
x = np.random.randn(num_points)
y = np.random.randn(num_points)
sizes = np.random.randint(10, 200, num_points)  # Random sizes for the balls

# Create scatter plot with balls of different sizes
plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=sizes, color='blue', alpha=0.5)
plt.title('Scatter Plot with Balls of Different Sizes')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)  # Show grid
plt.show()
