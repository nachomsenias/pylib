import matplotlib.pyplot as plt
import numpy as np

baseurl = "/home/ignacio/proyectos/abm-11m/log/calibration_DISTANCE/SSGA_HC_ABM11M_DISTANCE_E0_distance-params/"

fig = plt.figure(figsize=(100, 15))

# plt.gca().axes().get_xaxis().set_visible(False)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)


headers = ["TALKING", "DH DECAY (0)", "DH DECAY (1)", "DH DECAY (2)", "DH DECAY (3)", "DH DECAY (4)", "DH DECAY (5)",
           "DH DECAY (6)", "DH IMPACT (0)", "DH IMPACT (1)", "DH IMPACT (2)", "DH IMPACT (3)", "DH IMPACT (4)",
           "DH IMPACT (5)", "DH IMPACT (6)", "PERCEPTION DECAY (0)", "PERCEPTION DECAY (1)", "PERCEPTION DECAY (2)",
           "PERCEPTION DECAY (3)", "PERCEPTION DECAY (4)", "PERCEPTION DECAY (5)", "PERCEPTION DECAY (6)",
           "PERCEPTION POTENTIAL (0)", "PERCEPTION POTENTIAL (1)", "PERCEPTION POTENTIAL (2)",
           "PERCEPTION POTENTIAL (3)", "PERCEPTION POTENTIAL (4)", "PERCEPTION POTENTIAL (5)",
           "PERCEPTION POTENTIAL (6)", "PERCEPTION SPEED (0)", "PERCEPTION SPEED (1)", "PERCEPTION SPEED (2)",
           "PERCEPTION SPEED (3)", "PERCEPTION SPEED (4)", "PERCEPTION SPEED (5)", "PERCEPTION SPEED (6)", "WOM DECAY",
           "WOM SPEED"]

values = np.genfromtxt(baseurl + "values_num.csv", skip_header=False, delimiter=',', dtype=np.float)


plt.boxplot(np.transpose(values), labels=headers)

plt.savefig(baseurl + "FIGURE.png")

# index = 1
#
# numParams = 38
#
# rows = numParams / 2
#
# plotrow = 1
#
# for j in range(0, numParams):
#     plt.subplot(2, rows, index)
#
#     # print i,j
#
#     # plt.boxplot(trasposed_nsga2)
#     # plt.boxplot(nsga2,0,'')
#     plt.title(headers[index-1])
#
#     # axarr[methods.index(m), j].axis('off')
#
#     plt.boxplot(values[index-1])
#
#     index += 1
#
#
# # plt.show()
# plt.savefig(baseurl + "FIGURE.png")