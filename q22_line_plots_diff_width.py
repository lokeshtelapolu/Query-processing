import matplotlib.pyplot as plt

# Define the data for the lines
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]   # y = x^2
y2 = [0, 1, 8, 27, 64, 125] # y = x^3
y3 = [0, 1, 16, 36, 256, 625]
# Create the plot
plt.figure(figsize=(10, 6))

# Plot the first line with specific color, width and label
plt.plot(x, y1, color='blue', linewidth=2, label='y = x^2')

# Plot the second line with specific color, width and label
plt.plot(x, y2, color='red', linewidth=3, label='y = x^3')

plt.plot(x, y3, color='pink', linewidth=4, label='y = x^4')
# Add title and labels
plt.title('Plot of Two Lines')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()
