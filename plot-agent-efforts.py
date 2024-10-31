import matplotlib.pyplot as plt
import numpy as np
import glob
from datetime import datetime

def plot_values(f_values, f_steps, tokens, label, f_url):
    for thevalues in f_values:
        plt.plot(f_steps, thevalues)
    print('Plotting:' + path[-1])
    plt.title(label + ' Effort history by agent for run ' + tokens[2])
    # plt.savefig(f_url + tokens[0] + '_' + tokens[1] + '_' + tokens[2] + '_plot_' + label + '.png')
    it = tokens[2].split('.')[0]
    plt.savefig(f_url + label + '_' + it + '_.png')


# base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\dummy\\"
base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\dummy\\Belgium\\"

kpi = 'salaryHistory'
export_url = base_url + kpi + '\\'

steps = np.arange(100)
dt = datetime.now()
ts = datetime.timestamp(dt)

file_name = kpi + '_*_*.csv'
file_list = glob.glob(base_url + file_name)

fig = plt.figure()
fig.set_size_inches(13, 8)

for file in file_list:
    values = np.genfromtxt(file, skip_header=False, delimiter=';', dtype=str)
    replace_values = np.core.defchararray.replace(values, ',', '.')
    float_values = replace_values.astype(float)

    # Calcula el valor medio para cada fila y lo guarda junto al índice.
    mean_values = np.mean(float_values, axis=1)
    q1 = np.quantile(mean_values, 0.75)
    d1 = np.quantile(mean_values, 0.9)
    # dict_q1_values = {}
    # dict_d1_values = {}
    q1_list = []
    d1_list = []
    for i in range(len(mean_values)):
        value = mean_values[i]
        if value >= q1:
            q1_list.append(i)
        if value >= d1:
            d1_list.append(i)

    float_q1_values = float_values[np.array(q1_list)]
    float_d1_values = float_values[np.array(d1_list)]


    # for row_values in float_values:
    #     avg_value =

    # avg_values = np.mean(values, axis=0)
    # std_values = np.std(values, axis=0)
    # fig, ax = plt.subplots()
    # fig.set_size_inches(10, 6)
    # plt.plot(steps, avg_values)
    # plt.plot(steps, avg_values + std_values)
    # plt.plot(steps, avg_values - std_values)
    # ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)
    # Ejes fijos
    # plt.ylim([0.0, 1.0])
    path = file.split('\\')
    tokens = path[-1].split('_')

    plot_values(float_q1_values, steps, tokens, 'Q1', export_url)
    plt.clf()
    plot_values(float_d1_values, steps, tokens, 'D1', export_url)
    plt.clf()

    # Exportar los valores
    np.savetxt(export_url + 'Q1_' + tokens[2], float_q1_values, delimiter=",")
    np.savetxt(export_url + 'D1_' + tokens[2], float_d1_values, delimiter=",")
