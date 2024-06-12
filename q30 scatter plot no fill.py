import matplotlib.pyplot as plt
import numpy as np

# Generate random data points
np.random.seed(0)  # for reproducibility
num_points = 100
x = np.random.randn(num_points)
y = np.random.randn(num_points)

# Create scatter plot with empty circles
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.5, edgecolors='black', marker='o', facecolors='none')  # 'o' for empty circles
plt.title('Scatter Plot with Empty Circles')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)  # Show grid
plt.show()
