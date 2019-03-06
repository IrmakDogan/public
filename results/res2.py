import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams["font.family"] = "Times New Roman"
mpl.rcParams['font.size'] = 22
values = [47.59, 15.18,  25.07,12.16]
colors = ['lightsalmon', 'lightcyan', 'teal', 'orchid']
labels = ['Our method ', 'KRREG', 'Both', 'Neither']
explode = (0, 0, 0, 0)
plt.pie(values, colors=colors, labels=labels,  autopct='%1.2f%%', counterclock=False, shadow=True)
plt.axis("equal")
plt.title('The selected referring expression',fontweight='bold',fontsize = 24,y=1.05)
plt.show()
