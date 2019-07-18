import matplotlib.pyplot as plt
import numpy as np

baseurl = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/25TP/WOMM/data/p_"

plt.figure(figsize=(5, 3))

# plt.gca().axes().get_xaxis().set_visible(False)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)


methods_pairs = [["SPEA2", "MOEAD"], ["MOEAD", "NSGAII"], ["NSGAII", "SPEA2"]]

# methods = ["NSGAII", "SPEA2", "MOEAD"]

# headers = ["M", "AWARENESS IMPACT (0)", "AWARENESS IMPACT (1)", "AWARENESS IMPACT (2)",
#           "AWARENESS IMPACT (3)", "AWARENESS IMPACT (4)", "AWARENESS IMPACT (5)",
#           "AWARENESS IMPACT (6)", "DISCUSSION HEAT IMPACT (0)", "DISCUSSION HEAT IMPACT (1)",
#           "DISCUSSION HEAT IMPACT (2)", "DISCUSSION HEAT IMPACT (3)", "DISCUSSION HEAT IMPACT (4)",
#           "DISCUSSION HEAT IMPACT (5)", "DISCUSSION HEAT IMPACT (6)", "DISCUSSION HEAT DECAY (0)",
#           "DISCUSSION HEAT DECAY (1)", "DISCUSSION HEAT DECAY (2)", "DISCUSSION HEAT DECAY (3)",
#           "DISCUSSION HEAT DECAY (4)", "DISCUSSION HEAT DECAY (5)", "DISCUSSION HEAT DECAY (6)",
#           "TALKING", "WOM IMPACT", "AWAWRENESS DECAY"]

# index = 1
boxplot_values = []
labels = []

for pair in methods_pairs:

    # print methods
    # values = np.loadtxt(baseurl + pair[0]+"vs"+pair[1] + ".csv", dtype=np.float)

    values = np.genfromtxt(baseurl + pair[0] + "vs" + pair[1] + ".csv", skip_header=True, delimiter=',')

    boxplot_values.append(values)

    label = pair[0][:1] + "-" + pair[1][:1]
    labels.append(label)

    values = np.genfromtxt(baseurl + pair[1] + "vs" + pair[0] + ".csv", skip_header=True, delimiter=',')

    boxplot_values.append(values)

    label = pair[1][:1] + "-" + pair[0][:1]
    labels.append(label)

#    plt.subplot(1, 6, index)
#    index += 1


plt.boxplot(boxplot_values, labels=labels)

# plt.show()
plt.savefig(baseurl + "FIGURE.png")