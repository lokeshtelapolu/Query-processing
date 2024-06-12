import matplotlib.pyplot as plt
import numpy as np

# Sample data for various plots
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.random.normal(size=100)
categories = ['A', 'B', 'C', 'D']
values = [23, 17, 35, 29]
data = np.random.rand(10, 4)

# Function to create multiple types of plots
def create_multiple_plots():
    plt.figure(figsize=(15, 10))
    
    # Scatter plot
    plt.subplot(2, 3, 1)
    plt.scatter(x, y, color='blue', label='sin(x)')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    
    # Line plot
    plt.subplot(2, 3, 2)
    plt.plot(x, y, color='green', label='sin(x)')
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    
    # Histogram
    plt.subplot(2, 3, 3)
    plt.hist(z, bins=20, color='red', alpha=0.7, label='Random Data')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    
    # Bar plot
    plt.subplot(2, 3, 4)
    plt.bar(categories, values, color=['blue', 'green', 'red', 'orange'])
    plt.title('Bar Plot')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.grid(True)
    
    # Box plot
    plt.subplot(2, 3, 5)
    plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='cyan'))
    plt.title('Box Plot')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.grid(True)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Show the plots
    plt.show()


create_multiple_plots()
