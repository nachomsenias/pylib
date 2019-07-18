import matplotlib.pyplot as plt
import numpy as np

baseurl = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/25TP/WOMM/data/PARAMS_"
# baseurl = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/womM/WOMM/data/PARAMS_"

plt.figure(figsize=(115, 30))

# plt.gca().axes().get_xaxis().set_visible(False)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

methods = ["NSGAII", "SPEA2", "MOEAD"]

headers = ["M", "AWARENESS IMPACT (0)", "AWARENESS IMPACT (1)", "AWARENESS IMPACT (2)",
           "AWARENESS IMPACT (3)", "AWARENESS IMPACT (4)", "AWARENESS IMPACT (5)",
           "AWARENESS IMPACT (6)", "DISCUSSION HEAT IMPACT (0)", "DISCUSSION HEAT IMPACT (1)",
           "DISCUSSION HEAT IMPACT (2)", "DISCUSSION HEAT IMPACT (3)", "DISCUSSION HEAT IMPACT (4)",
           "DISCUSSION HEAT IMPACT (5)", "DISCUSSION HEAT IMPACT (6)", "DISCUSSION HEAT DECAY (0)",
           "DISCUSSION HEAT DECAY (1)", "DISCUSSION HEAT DECAY (2)", "DISCUSSION HEAT DECAY (3)",
           "DISCUSSION HEAT DECAY (4)", "DISCUSSION HEAT DECAY (5)", "DISCUSSION HEAT DECAY (6)",
           "TALKING", "WOM IMPACT", "AWAWRENESS DECAY"]

index = 1

for m in methods:

    # print methods
    values = np.loadtxt(baseurl + m + ".tsv", dtype=np.float)

    param = values.transpose()

    for j in range(0, 25):
        # plt.figure(methods.index(m))
        plt.subplot(3, 25, index)
        index += 1
        # print i,j

        # plt.boxplot(trasposed_nsga2)
        # plt.boxplot(nsga2,0,'')
        plt.title(m + " " + headers[j])

        # axarr[methods.index(m), j].axis('off')

        plt.boxplot(param[j])

# plt.show()
plt.savefig(baseurl + "FIGURE.png")