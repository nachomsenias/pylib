import matplotlib.pyplot as plt
import numpy as np
import glob

def read_values(f_list):
    values_dict = {}

    for file in f_list:
        values = np.genfromtxt(file, skip_header=False, delimiter=';', dtype=str)
        # replace_values = np.core.defchararray.replace(values, ',', '.')
        float_values = values.astype(float)

        path = file.split('\\')
        tokens = path[-1].split('_')
        it = tokens[-1].split('.')[0]
        values_dict[it] = float_values

    return values_dict

def get_colors(v_values):
    color_values = np.empty(len(v_values), dtype=str)
    for v_index in range(len(v_values)):
        if v_values[v_index] == 0:
            color_values[v_index] = 'yellow'
        elif v_values[v_index] == 1:
            color_values[v_index] = 'red'
        elif v_values[v_index] == -1:
            color_values[v_index] = 'green'
        else:
            raise ValueError('Valor incorrecto')

    return color_values


# base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\dummy\\effort_salary_vote\\"
base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\dummy\\Belgium\\"
kpi1 = 'effortHistory'
kpi2 = 'salaryHistory'
kpi3 = 'voteHistory'

quartiles = ['D1', 'D10', 'Q1', 'Q4']

for q in quartiles:
    # Run KPI1
    file_name = kpi1 + '\\' + q + '_*.csv'
    file_list = glob.glob(base_url + file_name)
    kpi1_values_dict = read_values(file_list)

    # Run KPI2
    file_name = kpi2 + '\\' + q + '_*.csv'
    file_list = glob.glob(base_url + file_name)
    kpi2_values_dict = read_values(file_list)

    # Run KPI3
    file_name = kpi3 + '\\' + q + '_*.csv'
    file_list = glob.glob(base_url + file_name)
    kpi3_values_dict = read_values(file_list)

    # Inicialización de la figura.
    fig = plt.figure()
    fig.set_size_inches(13, 8)

    final_kpi = 'combined'
    for i in range(len(kpi1_values_dict)):
        kpi1_values = kpi1_values_dict[str(i)]
        kpi2_values = kpi2_values_dict[str(i)]
        kpi3_values = kpi3_values_dict[str(i)]

        # Eliminamos la columna 0
        kpi1_values = kpi1_values[:, 1:]
        kpi2_values = kpi2_values[:, 1:]
        kpi3_values = kpi3_values[:, 1:]

        print('Plotting run:' + str(i))
        for j in range(len(kpi1_values)):
            kpi1_values_j = kpi1_values[j]
            kpi2_values_j = kpi2_values[j]
            kpi3_values_j = kpi3_values[j]

            colors = get_colors(kpi3_values_j)

            plt.scatter(kpi1_values_j, kpi2_values_j, c=colors)

        plt.title('Effort vs Salary for run ' + str(i))
        fig_name = base_url + final_kpi + '\\' + q + '_' + str(i) + '.png'
        plt.xlabel("Effort")
        plt.ylabel("Salary")
        plt.savefig(fig_name)
        plt.clf()
