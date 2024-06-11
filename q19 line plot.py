import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.plot(x, y, label='Prime Numbers')

# Labeling the x-axis
plt.xlabel('X Axis Label')

# Labeling the y-axis
plt.ylabel('Y Axis Label')

# Adding a title
plt.title('Line Plot of Prime Numbers')

# Adding a legend
plt.legend()

# Display the plot
plt.show()
