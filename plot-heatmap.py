import matplotlib.pyplot as plt
import numpy as np
import glob
from datetime import datetime


def gather_matrix_values(file_list, output_file):
    matrix = np.zeros(shape=(101, 101), dtype=float)

    for file in file_list:
        values = np.genfromtxt(file, skip_header=True, delimiter=';', dtype=float)
        avg_values = np.mean(values, axis=0)
        path = file.split('\\')
        tokens = path[-1].split('_')

        theta_index = round(float(tokens[0]) * 100)
        # print(tokens[0] + ' => ' + str(theta_index))
        tau_index = round(float(tokens[1]) * 100)
        # print(tokens[1] + ' => ' + str(tau_index))

        last_avg_value = avg_values[-1]
        matrix[theta_index, tau_index] = last_avg_value

    matrix = np.delete(matrix, 0, axis=0)
    matrix = np.delete(matrix, 0, axis=1)
    matrix.tofile(output_file, sep=';')
    np.savetxt(output_file, matrix, delimiter=';')

    return matrix


data_name = "tau"
# data_name = "step_gini"

base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\grid_2023_100\\"
# file_list = glob.glob(base_url + '*_*_gini_*.csv')

# fig, axs = plt.subplots(19, 19)
# fig.set_size_inches(60, 60)

steps = np.arange(100)
dt = datetime.now()
ts = datetime.timestamp(dt)
# itervalues = [18]

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
a_value = 1
output_name = base_url + data_name + '\\matrix_' + str(a_value) + '.csv'
try:
    matrix = np.genfromtxt(output_name, skip_header=True, delimiter=';', dtype=float)
except Exception as e:
    print(e)
    print('Matrix not found, gathering it from scratch...')
    file_name = '*_*_' + str(a_value) + '_' + data_name + '_*.csv'
    file_list = glob.glob(base_url + file_name)
    matrix = gather_matrix_values(file_list, output_file=output_name)

# matrix = np.zeros(shape=(101, 101), dtype=float)
#
# for file in file_list:
#     values = np.genfromtxt(file, skip_header=True, delimiter=';', dtype=float)
#     avg_values = np.mean(values, axis=0)
#     path = file.split('\\')
#     tokens = path[-1].split('_')
#
#     theta_index = round(float(tokens[0]) * 100)
#     # print(tokens[0] + ' => ' + str(theta_index))
#     tau_index = round(float(tokens[1]) * 100)
#     # print(tokens[1] + ' => ' + str(tau_index))
#
#     last_avg_value = avg_values[-1]
#     matrix[theta_index, tau_index] = last_avg_value
#
# matrix = np.delete(matrix, 0, axis=0)
# matrix = np.delete(matrix, 0, axis=1)

plt.imshow(matrix, cmap='twilight_shifted', interpolation='nearest')
plt.colorbar()
plt.title("Values of " + data_name + " at the end of the simulation")
plt.ylabel("Theta")
plt.xlabel("Initial Tau")
plt.savefig(base_url + data_name + '\\heatmap_' + str(a_value) + '.png')
