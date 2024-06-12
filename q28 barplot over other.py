import matplotlib.pyplot as plt
import numpy as np

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_dev_men = [4, 3, 4, 1, 5]
std_dev_women = [3, 5, 2, 3, 3]

# Number of groups
num_groups = len(groups)

# Width of each bar
bar_width = 0.35

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create the bars for men
bars_men = ax.bar(np.arange(num_groups), means_men, bar_width, yerr=std_dev_men, label='Men')

# Create the bars for women stacked on top of men
bars_women = ax.bar(np.arange(num_groups), means_women, bar_width, bottom=means_men, yerr=std_dev_women, label='Women')

# Add labels, title, and legend
ax.set_xlabel('Groups')
ax.set_ylabel('Scores')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(np.arange(num_groups))
ax.set_xticklabels(groups)
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
