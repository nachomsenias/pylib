import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import glob
from datetime import datetime


# def gather_matrix_values(file_list, output_file):
#     matrix = np.zeros(shape=(101, 101), dtype=float)
#
#     for file in file_list:
#         values = np.genfromtxt(file, skip_header=True, delimiter=';', dtype=float)
#         avg_values = np.mean(values, axis=0)
#         path = file.split('\\')
#         tokens = path[-1].split('_')
#
#         theta_index = round(float(tokens[0]) * 100)
#         # print(tokens[0] + ' => ' + str(theta_index))
#         tau_index = round(float(tokens[1]) * 100)
#         # print(tokens[1] + ' => ' + str(tau_index))
#
#         last_avg_value = avg_values[-1]
#         matrix[theta_index, tau_index] = last_avg_value
#
#     matrix = np.delete(matrix, 0, axis=0)
#     matrix = np.delete(matrix, 0, axis=1)
#     matrix.tofile(output_file, sep=';')
#     np.savetxt(output_file, matrix, delimiter=';')
#
#     return matrix


# data_names = ["tau", "stepgini", "wealth"]
data_names = ["wealth"]

base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\pairs\\"

for data_name in data_names:
    print('Running ' + data_name + '...')
    # Ejemplo de fichero: "step_gini_0.949999988079071_0.4699999988079071_1696979380594.csv"
    file_name = data_name + '_*_*_*.csv'
    file_list = glob.glob(base_url + file_name)
    df = pd.DataFrame(columns=['Name', 'Step', 'Value'])
    for file in file_list:
        values = np.genfromtxt(file, skip_header=True, delimiter=';', dtype=float)
        if ',' in file:
            file = file.replace(',', '.')
        tokens = file.split('_')
        thetha = "%.2f" % float(tokens[1])
        tau = "%.2f" % float(tokens[2])
        name = "Theta: " + thetha + " Tau: " + tau
        for value in values:
            for i in range(len(value)):
                float_value = value[i]
                df_i = pd.DataFrame({'Name': [name], 'Step': [i], 'Value': [float(value[i])]})
                df = pd.concat([df, df_i], axis=0)

    filtered = df[df['Step'] > 0]

    sns.set_theme(style="darkgrid")
    sns.set(rc={'figure.figsize': (11.7, 8.27)})
    sns.lineplot(x="Step", y="Value", hue="Name", data=filtered)
    plt.savefig(base_url + data_name + '_lines.png')
    plt.clf()


# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
# a_value = 1
# output_name = base_url + data_name + '\\matrix_' + str(a_value) + '.csv'
# try:
#     matrix = np.genfromtxt(output_name, skip_header=True, delimiter=';', dtype=float)
# except Exception as e:
#     print(e)
#     print('Matrix not found, gathering it from scratch...')
#     file_name = '*_*_' + str(a_value) + '_' + data_name + '_*.csv'
#     file_list = glob.glob(base_url + file_name)
#     matrix = gather_matrix_values(file_list, output_file=output_name)
#
# # print_heat_map(matrix)
#
# ## Ahora queremos saber como se distribuyen estos puntos.
# df = pd.DataFrame(columns=['Theta', 'Tau', 'Result'])
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         df_i_j = pd.DataFrame({'Theta': [i], 'Tau': [j], 'Result': [float("%.2f" % matrix[i, j])]})
#         df = pd.concat([df, df_i_j], axis=0)
#
# # Filtrar las filas que tienen un 'Result' mayor de 0.8
# filtered = df[df['Result'] < 0.51]
# sorted_df = filtered.sort_values(by=['Result'], ascending=False)
# sorted_df.to_csv(base_url + data_name + '\\matrix_' + str(a_value) + '_filtered_sorted.csv', sep=';', index=False)
#
# sns.set_theme()
# sns.set(rc={'figure.figsize': (11.7, 8.27)})
# sns.histplot(data=sorted_df, x="Result")
# plt.savefig(base_url + data_name + '\\hisplot.png')
