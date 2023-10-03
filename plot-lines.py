import matplotlib.pyplot as plt
import numpy as np
import glob
from datetime import datetime

# import sys
#
# data_name = sys.argv[1]
data_name = "tau"

base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\grid_thetha\\1000_tau10\\"
# file_list = glob.glob(base_url + '*_*_gini_*.csv')

# fig, axs = plt.subplots(19, 19)
# fig.set_size_inches(60, 60)

steps = np.arange(100)
dt = datetime.now()
ts = datetime.timestamp(dt)
# itervalues = [18]

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
for i in range(19):
    for j in range(19):
        file_name = str(i+1)+'_'+str(j+1)+'_' + data_name + '_*.csv'
        file_list = glob.glob(base_url + file_name)
        if len(file_list)>1:
            print("More than one file.")
        # fig = plt.figure()
        # fig.set_size_inches(10, 6)
        values = np.genfromtxt(file_list[0], skip_header=True, delimiter=';', dtype=float)
        # for k in range(values.shape[0]):
        #     plt.plot(steps, values[k])
        # plt.title('Theta='+str(i+1)+' a='+str(j+1))
        # plt.savefig(base_url + data_name + '\\' + str(i+1)+'_'+str(j+1)+'_' + data_name + '.png')
        # plt.close(fig)
            # axs[i, j].plot(steps, values[k])
        # axs[0, 1].set_title('Theta='+str(i+1)+' a='+str(j+1))
        avg_values = np.mean(values, axis=0)
        std_values = np.std(values, axis=0)
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 6)
        plt.plot(steps, avg_values)
        plt.plot(steps, avg_values + std_values)
        plt.plot(steps, avg_values - std_values)
        ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)
        plt.title('Average and std for '+data_name + ' with Theta='+str(i+1)+' a='+str(j+1))
        plt.savefig(base_url + data_name + '\\' + str(i + 1) + '_' + str(j + 1) + '_' + data_name + '_average.png')
        plt.close(fig)


# plt.savefig(base_url + "gini_"+str(ts)+".png")

# values = np.genfromtxt(base_url+"1_1_gini_1653179896755.csv", skip_header=True, delimiter=';', dtype=np.float)
#
# shape = values.shape[0]
#
#
#
# for i in range(values.shape[0]):
#     plt.plot(steps, values[i])
#
# plt.show()
#
# plt.savefig(base_url + "1_1_gini_1653179896755.png")
