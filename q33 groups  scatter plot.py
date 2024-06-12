import matplotlib.pyplot as plt
import numpy as np

# Sample data for three groups: Group 1, Group 2, and Group 3
# Each group contains weights and heights of individuals
group1_weights = np.random.normal(60, 10, 50)
group1_heights = np.random.normal(160, 10, 50)

group2_weights = np.random.normal(65, 8, 50)
group2_heights = np.random.normal(165, 8, 50)

group3_weights = np.random.normal(70, 6, 50)
group3_heights = np.random.normal(170, 6, 50)

# Create scatter plot for each group
plt.figure(figsize=(8, 6))

plt.scatter(group1_weights, group1_heights, color='blue', label='Group 1')
plt.scatter(group2_weights, group2_heights, color='green', label='Group 2')
plt.scatter(group3_weights, group3_heights, color='red', label='Group 3')

# Add labels and title
plt.title('Scatter Plot of Weights vs Heights for Three Groups')
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.legend()
plt.grid(True)  # Show grid
plt.show()
