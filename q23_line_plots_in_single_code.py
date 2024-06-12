import matplotlib.pyplot as plt

# Sample data for multiple plots
data1 = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11],
    'color': 'blue',
    'label': 'Prime Numbers'
}

data2 = {
    'x': [1, 2, 3, 4, 5],
    'y': [1, 4, 9, 16, 25],
    'color': 'green',
    'label': 'Squares'
}

data3 = {
    'x': [1, 2, 3, 4, 5],
    'y': [1, 8, 27, 64, 125],
    'color': 'red',
    'label': 'Cubes'
}


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(data1['x'], data1['y'], color=data1['color'], label=data1['label'])
plt.title('Prime Numbers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
    
    # Create second subplot
plt.subplot(1, 3, 2)
plt.plot(data2['x'], data2['y'], color=data2['color'], label=data2['label'])
plt.title('Squares')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
    
    # Create third subplot
plt.subplot(1, 3, 3)
plt.plot(data3['x'], data3['y'], color=data3['color'], label=data3['label'])
plt.title('Cubes')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
    
    # Adjust layout to prevent overlap
plt.tight_layout()
    
    # Show the plot
plt.show()    
