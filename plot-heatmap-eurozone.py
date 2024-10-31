import matplotlib.pyplot as plt
import numpy as np
import glob
import os


def gather_matrix_values(file_list, output_file):
    matrix = np.zeros(shape=(10, 10), dtype=float)

    for file in file_list:
        values = np.genfromtxt(file, skip_header=True, delimiter=';', dtype=float)
        avg_value = np.mean(values[:, -1], axis=0)
        path = file.split('\\')
        tokens = path[-1].split('_')

        theta_index = round(float(tokens[0]) / 10)
        # print(tokens[0] + ' => ' + str(theta_index))
        tau_index = round(float(tokens[1]) / 10)
        # print(tokens[1] + ' => ' + str(tau_index))

        last_avg_value = avg_value
        matrix[theta_index, tau_index] = last_avg_value

    # matrix = np.delete(matrix, 0, axis=0)
    # matrix = np.delete(matrix, 0, axis=1)
    matrix.tofile(output_file, sep=';')
    np.savetxt(output_file, matrix, delimiter=';')

    return matrix


def get_matrix(kpi, a_value, url):
    output_name = url + kpi + '\\matrix_' + kpi + '_' + str(a_value) + '.csv'
    try:
        return np.genfromtxt(output_name, delimiter=';', dtype=float)
    except Exception as e:
        print(e)
        print('Matrix not found, gathering it from scratch...')
        os.makedirs(url + kpi, exist_ok=True)
        file_name = '*_*_' + str(a_value) + '_' + kpi + '_*.csv'
        file_list = glob.glob(url + file_name)
        return gather_matrix_values(file_list, output_file=output_name)


def print_heat_map(name, data, a_value, url):
    fig, ax = plt.subplots()
    # if name == "tau":
    #     fig.set_size_inches(75, 75)
    # else:
    #     fig.set_size_inches(16, 16)
    fig.set_size_inches(16, 16)
    # plt.imshow(matrix, cmap='twilight_shifted', interpolation='nearest')
    plt.imshow(data)
    fontsize_value = 20
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=fontsize_value)
    # if name == "tau":
    #     for i in range(len(data)):
    #         for j in range(len(data[i])):
    #             ax.text(j, i, "%.4f" % data[i, j], ha="center", va="center", color="w")
    plt.title("Values of " + name + " at the end of the simulation", fontsize=fontsize_value)
    plt.ylabel("Theta", fontsize=fontsize_value)
    plt.xlabel("Initial Tau", fontsize=fontsize_value)
    plt.xticks(fontsize=fontsize_value)
    plt.yticks(fontsize=fontsize_value)
    ax.set_xticks(np.arange(0, 10, step=5))
    ax.set_yticks(np.arange(0, 10, step=5))
    fig.tight_layout()
    plt.savefig(url + name + '\\heatmap_' + str(a_value) + '.png')


def generate_heatmaps(given_url):
    # steps = np.arange(100)
    # dt = datetime.now()
    # ts = datetime.timestamp(dt)
    # itervalues = [18]

    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    a_value = 1

    names = ["wealth", "tau"]
    for data_name in names:
        print('Running ' + data_name + '...')
        matrix = get_matrix(data_name, a_value, given_url)

        print_heat_map(data_name, matrix, a_value, given_url)
        plt.clf()


# data_name = "tau"
# data_name = "step_gini"

# base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\grid_eurozone\\"
base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\grid_eurozone_5k\\"
# file_list = glob.glob(base_url + '*_*_gini_*.csv')

# fig, axs = plt.subplots(19, 19)
# fig.set_size_inches(60, 60)

for name in os.listdir(base_url):
    if os.path.isdir(os.path.join(base_url, name)):
        sub_url = os.path.join(base_url, name) + '\\'
        print(sub_url)
        generate_heatmaps(sub_url)

# ## Ahora queremos saber como se distribuyen estos puntos.
# df = pd.DataFrame(columns=['Theta', 'Tau', 'Result'])
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         df_i_j = pd.DataFrame({'Theta': [i], 'Tau': [j], 'Result': [float("%.4f" % matrix[i, j])]})
#         df = pd.concat([df, df_i_j], axis=0)
#
# # Filtrar las filas que tienen un 'Result' mayor de 0.8
# filtered = df[df['Result'] < 0.51]
# filtered = filtered[filtered['Result'] > 0.0]
# sorted_df = filtered.sort_values(by=['Result'], ascending=False)
# sorted_df.to_csv(base_url + data_name + '\\matrix_' + str(a_value) + '_filtered_sorted.csv', sep=';', index=False)
#
# sns.set_theme()
# sns.set(rc={'figure.figsize': (11.7, 8.27)})
# sns.histplot(data=sorted_df, x="Result")
# plt.savefig(base_url + data_name + '\\hisplot.png')
