import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 3
means_frank = (80.70, 5.55, 13.75)
means_guido = (50.34, 5.50, 44.16)
plt.rcParams["font.family"] = "Times New Roman"

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.43
opacity = 0.8
 
plt.bar(index, means_frank, bar_width,
                 alpha=opacity,
                 color='lightsalmon',
                 label='Our Method')
for i, v in enumerate(means_frank):
    ax.text( i + .017,v + 1, "%" + str(v), color='black', fontsize = 20)
 
plt.bar(index + bar_width, means_guido, bar_width,
                 alpha=opacity,
                 color='lightcyan',
                 label='KRREG')
for i, v in enumerate(means_guido):
    ax.text( i + bar_width+ .017,v + 1, "%" + str(v), color='black', fontsize = 20)

plt.yticks(fontsize=24)
plt.ylabel('Percentage of selection', fontsize=24)
plt.title('Finding the referred object',fontweight='bold', fontsize=24)
plt.xticks(index + bar_width, ('Correct target', 'False target', 'Unclear expression'), fontsize=20)
plt.legend()

plt.legend(loc=7, bbox_to_anchor=(1,0.8),prop={'size': 20})
plt.tight_layout()
plt.show()

