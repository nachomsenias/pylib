import matplotlib.pyplot as plt
import numpy as np
import glob

def plot_values(f_values, f_steps, it, label, f_url):
    for thevalues in f_values:
        plt.plot(f_steps, thevalues)
    print('Plotting:' + label + ' ' + it)
    plt.title(label + ' history by agent for run ' + it)
    plt.savefig(f_url + label + '_' + it + '.png')

def read_values(f_name):
    file_list = glob.glob(base_url + f_name)
    # Asumiré que solo hay uno.
    file = file_list[0]
    values = np.genfromtxt(file, skip_header=False, delimiter=';', dtype=str)
    replace_values = np.core.defchararray.replace(values, ',', '.')
    return replace_values.astype(float)

def plot_n_export(kpi_q1_values, kpi_d1_values, kpi_q4_values, kpi_d10_values, f_steps, index, f_export_url):
    plot_values(kpi_q1_values, f_steps, str(index), 'Q1', f_export_url)
    plt.clf()
    plot_values(kpi_d1_values, f_steps, str(index), 'D1', f_export_url)
    plt.clf()
    plot_values(kpi_q4_values, f_steps, str(index), 'Q4', f_export_url)
    plt.clf()
    plot_values(kpi_d10_values, f_steps, str(index), 'D10', f_export_url)
    plt.clf()

    # Exportar los valores
    np.savetxt(f_export_url + 'Q1_' + str(index) + '.csv', kpi_q1_values, delimiter=";")
    np.savetxt(f_export_url + 'D1_' + str(index) + '.csv', kpi_d1_values, delimiter=";")
    np.savetxt(f_export_url + 'Q4_' + str(index) + '.csv', kpi_q4_values, delimiter=";")
    np.savetxt(f_export_url + 'D10_' + str(index) + '.csv', kpi_d10_values, delimiter=";")

# base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\dummy\\effort_salary_vote\\"
base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\dummy\\Belgium\\"
kpi1 = 'effortHistory'
kpi2 = 'salaryHistory'
kpi3 = 'voteHistory'

# Carga de datos de cada ejecución
for i in range(50):
    file_name1 = kpi1 + '_*_' + str(i) + '.csv'
    kpi1_values = read_values(file_name1)
    file_name2 = kpi2 + '_*_' + str(i) + '.csv'
    kpi2_values = read_values(file_name2)
    file_name3 = kpi3 + '_*_' + str(i) + '.csv'
    kpi3_values = read_values(file_name3)

    # Ahora se filtran los agentes para quedarnos con los que más ganan (kpi2).
    mean_values = np.mean(kpi2_values, axis=1)
    # Q1 y D1
    q1 = np.quantile(mean_values, 0.75)
    d1 = np.quantile(mean_values, 0.9)
    q1_list = []
    d1_list = []
    # Q4 y D10
    q4 = np.quantile(mean_values, 0.25)
    d10 = np.quantile(mean_values, 0.1)
    q4_list = []
    d10_list = []
    for j in range(len(mean_values)):
        value = mean_values[j]
        if value >= q1:
            q1_list.append(j)
        if value >= d1:
            d1_list.append(j)
        if value <= q4:
            q4_list.append(j)
        if value <= d10:
            d10_list.append(j)

    # Se filtra el salario
    kpi2_q1_values = kpi2_values[np.array(q1_list)]
    kpi2_d1_values = kpi2_values[np.array(d1_list)]
    kpi2_q4_values = kpi2_values[np.array(q4_list)]
    kpi2_d10_values = kpi2_values[np.array(d10_list)]

    # Se filtra el esfuerzo
    kpi1_q1_values = kpi1_values[np.array(q1_list)]
    kpi1_d1_values = kpi1_values[np.array(d1_list)]
    kpi1_q4_values = kpi1_values[np.array(q4_list)]
    kpi1_d10_values = kpi1_values[np.array(d10_list)]

    # Se filtra el voto
    kpi3_q1_values = kpi3_values[np.array(q1_list)]
    kpi3_d1_values = kpi3_values[np.array(d1_list)]
    kpi3_q4_values = kpi3_values[np.array(q4_list)]
    kpi3_d10_values = kpi3_values[np.array(d10_list)]

    # Ploteamos y exportamos los valores.
    steps = np.arange(100)
    export_url = base_url + kpi2 + '\\'
    plot_n_export(kpi2_q1_values, kpi2_d1_values, kpi2_q4_values, kpi2_d10_values, steps, i, export_url)

    export_url = base_url + kpi1 + '\\'
    plot_n_export(kpi1_q1_values, kpi1_d1_values, kpi1_q4_values, kpi1_d10_values, steps, i, export_url)

    export_url = base_url + kpi3 + '\\'
    plot_n_export(kpi3_q1_values, kpi3_d1_values, kpi3_q4_values, kpi3_d10_values, steps, i, export_url)
