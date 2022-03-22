import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

csvPathFile = '/home/ignacio/proyectos/modelo-redistribucion/experiments/dummy/perception/alway_up/perception_0.6_0.4_1625760254018.csv'

data = np.genfromtxt(csvPathFile, delimiter=';', skip_header=1)

# print(data)

expectedY = 11
expectedX = 10

mapValues = np.arange(11*10, dtype=float).reshape(10, 11)

for row in data:
    x = int(round(row[0]*10))
    y = int(round(row[1]*10))
    v = row[3]
    mapValues[x-1][y] = v

print(mapValues)

# plt.imshow(mapValues, cmap='hot', interpolation='nearest')
# plt.show()

# plt.savefig('/home/ignacio/proyectos/modelo-redistribucion/experiments/dummy/perception/alway_up/Figure_0.4_0.6_1625760254018.png')



ax = sns.heatmap(mapValues, linewidth=0.5)

yvalues = ["0.1", "0.2", "0.3", "0.4", "0.5",
           "0.6", "0.7", "0.8", "0.9", "1.0"]
xvalues = ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5",
           "0.6", "0.7", "0.8", "0.9", "1.0"]

ax.set_xticklabels(xvalues)
ax.set_xlabel('Perception')
ax.set_yticklabels(yvalues)
ax.set_ylabel('Defectors %')

# plt.show()
plt.savefig('/home/ignacio/proyectos/modelo-redistribucion/experiments/dummy/perception/alway_up/Figure_0.6_0.4_1625760254018_sns.png')

