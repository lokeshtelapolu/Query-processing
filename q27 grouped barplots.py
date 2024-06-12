import matplotlib.pyplot as plt
import numpy as np

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Number of groups
num_groups = len(groups)

# Width of each bar
bar_width = 0.35

# X values for the men's bars
x_values_men = np.arange(num_groups)

# X values for the women's bars (shifted by the bar width)
x_values_women = np.arange(num_groups) + bar_width

# Create the bar plot
plt.bar(x_values_men, means_men, width=bar_width, label='Men')
plt.bar(x_values_women, means_women, width=bar_width, label='Women')

# Add labels, title, and legend
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
#plt.xticks(x_values_men + bar_width / 2, groups)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
