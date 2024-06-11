import matplotlib.pyplot as plt

# Function to read data from a text file and return x and y values
def read_data(file_path):
    x = []
    y = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.split()
            x.append(int(values[0]))
            y.append(int(values[1]))
    return x, y

# File path
file_path = 'test.txt'

# Read data from the file
x, y = read_data(file_path)

# Create a plot
plt.plot(x, y, label='Data Line')

# Labeling the x-axis
plt.xlabel('X Axis')

# Labeling the y-axis
plt.ylabel('Y Axis')

# Adding a title
plt.title('Line Plot from Text File Data')

# Adding a legend
plt.legend()

# Display the plot
plt.show()
