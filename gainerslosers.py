import matplotlib.pyplot as plt
import numpy as np

# plt.figure(figsize=(11, 3))


e0_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/out/PSOE_distances.csv', delimiter=';')
# e0_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.0/out_20/PSOE_distances.csv', delimiter=';')

# print(e0_psoe)

baseline_psoe = e0_psoe[:, -1]

e1_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.1/PSOE_distances.csv', delimiter=';')
# e1_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.1_rally/out_20/PSOE_distances.csv', delimiter=';')

diff_e1_psoe = np.subtract(e1_psoe[:, -1], baseline_psoe)

e3_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.3/PSOE_distances.csv', delimiter=';')
# e3_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.3_leadership_eventos/out_20/PSOE_distances.csv', delimiter=';')

diff_e3_psoe = np.subtract(e3_psoe[:, -1], baseline_psoe)

e4_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.4/PSOE_distances.csv', delimiter=';')
# e4_psoe = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.4_priming/out_20/PSOE_distances.csv', delimiter=';')

diff_e4_psoe = np.subtract(e4_psoe[:, -1], baseline_psoe)


e0_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/out/PP_distances.csv', delimiter=';')
# e0_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.0/out_20/PP_distances.csv', delimiter=';')

baseline_pp = e0_pp[:, -1]

e1_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.1/PP_distances.csv', delimiter=';')
# e1_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.1_rally/out_20/PP_distances.csv', delimiter=';')

diff_e1_pp = np.subtract(e1_pp[:, -1], baseline_pp)

e3_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.3/PP_distances.csv', delimiter=';')
# e3_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.3_leadership_eventos/out_20/PP_distances.csv', delimiter=';')

diff_e3_pp = np.subtract(e3_pp[:, -1], baseline_pp)

# e4_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.4_priming/out_20/PP_distances.csv', delimiter=';')
e4_pp = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.4/PP_distances.csv', delimiter=';')

diff_e4_pp = np.subtract(e4_pp[:, -1], baseline_pp)


# e0_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.0/out_20/IU_distances.csv', delimiter=';')
e0_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/out/IU_distances.csv', delimiter=';')
baseline_iu = e0_iu[:, -1]

# e1_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.1_rally/out_20/IU_distances.csv', delimiter=';')
e1_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.1/IU_distances.csv', delimiter=';')

diff_e1_iu = np.subtract(e1_iu[:, -1], baseline_iu)

# e3_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.3_leadership_eventos/out_20/IU_distances.csv', delimiter=';')
e3_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.3/IU_distances.csv', delimiter=';')

diff_e3_iu = np.subtract(e3_iu[:, -1], baseline_iu)

# e4_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/E.4_priming/out_20/IU_distances.csv', delimiter=';')
e4_iu = np.genfromtxt('/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/e.4/IU_distances.csv', delimiter=';')


diff_e4_iu = np.subtract(e4_iu[:, -1], baseline_iu)

labels = ["IU", "PSOE", "PP"]

# fig, ax = plt.subplots(figsize=(8, 5))
plt.figure(figsize=(10, 5))

plt.ylim(bottom=-0.5, top=0.5)

# First PLOT :: E1
e1_plot = plt.subplot(1, 3, 1, label="Rally")
e1_values = np.stack((diff_e1_iu, diff_e1_psoe, diff_e1_pp))

x=[0.55, 1, 2, 3, 3.45]
y=[0, 0, 0, 0, 0]

plt.plot(x, y, '--')

plt.boxplot(np.transpose(e1_values), labels=labels, widths=0.7)

e1_plot.set_title('Rally')
e1_plot.set_ylabel('Distance variation')
e1_plot.set_ylim([-0.55, 0.55])
e1_plot.set_yticks(np.arange(-0.5, 0.6, 0.1))

# Second PLOT :: E3
e3_plot = plt.subplot(1, 3, 2, label="Leadership")
e3_values = np.stack((diff_e3_iu, diff_e3_psoe, diff_e3_pp))

plt.plot(x, y, '--')

plt.boxplot(np.transpose(e3_values), labels=labels, widths=0.7)

e3_plot.set_title('Leadership')
# e3_plot.set_ylabel('Distance increment')
e3_plot.set_ylim([-0.55, 0.55])
e3_plot.set_yticks(np.arange(-0.5, 0.6, 0.1))
# e3_plot.set_xmargin(0.5)

# Last PLOT :: E4
e4_plot = plt.subplot(1, 3, 3, label="Priming")
e4_values = np.stack((diff_e4_iu, diff_e4_psoe, diff_e4_pp))

plt.plot(x, y, '--')

plt.boxplot(np.transpose(e4_values), labels=labels, widths=0.7)

e4_plot.set_title('Priming')
# e4_plot.set_ylabel('Distance increment')
e4_plot.set_ylim([-0.55, 0.55])
e4_plot.set_yticks(np.arange(-0.5, 0.6, 0.1))

# plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

# plt.savefig("/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/GainersLosers.png")
plt.savefig("/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/GainersLosers.png")

# full = plt.figure(figsize=(11, 3))
#
# trasposed_full = np.stack((np.transpose(e1_values), np.transpose(e3_values), np.transpose(e4_values)))
#
# # plt.axes.set_ylabel('Distance variation')
#
# full_labels = ["IU_rally", "PP_rally", "PSOE_rally", "IU_leadership", "PP_leadership", "PSOE_leadership",
#                "IU_priming", "PP_priming", "PSOE_priming"]
#
# plt.boxplot(trasposed_full, labels=full_labels)
#
# plt.savefig("/home/ignacio/proyectos/abm-11m/distance-analysis/analysis/escenarios/GainersLosers_full.png")


labels = ['Rally', 'Leadership', 'Priming']
iu_means = [np.average(diff_e1_iu).round(decimals=2), np.average(diff_e3_iu).round(decimals=2), np.average(diff_e4_iu).round(decimals=2)]
pp_means = [np.average(diff_e1_pp).round(decimals=2), np.average(diff_e3_pp).round(decimals=2), np.average(diff_e4_pp).round(decimals=2)]
psoe_means = [np.average(diff_e1_psoe).round(decimals=2), np.average(diff_e3_psoe).round(decimals=2), np.average(diff_e4_psoe).round(decimals=2)]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(8, 5))
# rects1 = ax.bar(x - width/2, iu_means, width, label='IU')
# rects2 = ax.bar(x + width/2, pp_means, width, label='PP')
# rects3 = ax.bar(x + width/2, psoe_means, width, label='PSOE')

# rects1 = ax.bar(x- 2*width/3, iu_means, width/3, label='IU')
# rects2 = ax.bar(x- 2*width/3 + (width/3), pp_means, width/3, label='PP')
# rects3 = ax.bar(x- 2*width/3 + (2*width/3), psoe_means, width/3, label='PSOE')

# ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
# ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
# ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)


rects1 = ax.bar(x, iu_means, width, label='IU', color='#66c2a5')

rects2 = ax.bar(x + width, psoe_means, width, label='PSOE', color='#d53e4f')

rects3 = ax.bar(x + width*2, pp_means, width, label='PP', color='#3288bd')

# rects1 = ax.bar(x- width/2 + width/6, iu_means, width/3, label='IU')
#
# for rect in rects1:
#     rect.set_color('#66c2a5')
#
# rects2 = ax.bar(x- width/2 + (width/3) + width/6, pp_means, width/3, label='PP')
#
# for rect in rects2:
#     rect.set_color('#3288bd')
#
# rects3 = ax.bar(x- width/2 + (2*width/3) + width/6, psoe_means, width/3, label='PSOE')
#
# for rect in rects3:
#     rect.set_color('#d53e4f')


xtics = [width*3/2-width/2, width*3/2 + width*4-width/2, width*3/2 + width*8-width/2]

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Absolute distance variation')
#ax.set_title('Distance variation by party for each scenario')
ax.set_xticks(xtics)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
        else:
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, -14),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

# plt.show()
plt.savefig("/home/ignacio/proyectos/abm-11m/dummy_output/R1_201217-log-alahmbra/log/calibration_DISTANCE_DH_20k_influence/SSGA_HC_flat_distance_baseline_influence_20k_params-dh/GainersLosers_bar.png")
