import matplotlib.pyplot as plt
import numpy as np

baseurl = "/home/ignacio/proyectos/abm4marketing/ziocommon/cro-extras/cro-35-log/35TP/CRO-SL_LOG/"

plt.figure(figsize=(8, 4))



# print methods
# values = np.loadtxt(baseurl + pair[0]+"vs"+pair[1] + ".csv", dtype=np.float)

values = np.genfromtxt(baseurl+"larva-boxplot.csv", skip_header=True, delimiter=';', dtype=np.float)

values = values * 100

labels = ["BLX-\u03B1", "SBX", "Mutation", "Random Walk"]

fig = plt.subplot(1, 1, 1, label="Percentage")

plt.boxplot(values.transpose(), labels=labels)

fig.set_xlabel('Substrates')
fig.set_ylabel('Percentage')
fig.set_title('Percentage of times that a given substrate provides the best solution in a generation')



# plt.show()
plt.savefig(baseurl + "larva-figure.png")
