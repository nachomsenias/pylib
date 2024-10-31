import matplotlib.pyplot as plt
import numpy as np
import glob

def plot_values(values, label, filename, ylim_min=None, ylim_max=None, fig_size_x=10, fig_size_y=6):
    fig, ax = plt.subplots()
    fig.set_size_inches(fig_size_x, fig_size_y)
    plt.plot(np.transpose(values))
    if ylim_min is not None or ylim_max is not None:
        plt.ylim([ylim_min, ylim_max])
    plt.title(label + ' values for every simulation.')
    plt.savefig(base_url + filename)
    plt.close(fig)

def plot_average(values, fig_label, filename, ylim_min=None, ylim_max=None, xlim_min=None, xlim_max=None, fig_size_x=10, fig_size_y=6):
    avg_values = np.mean(values, axis=0)
    std_values = np.std(values, axis=0)
    fig, ax = plt.subplots()
    fig.set_size_inches(fig_size_x, fig_size_y)
    plt.plot(steps, avg_values, label=fig_label)
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)
    if ylim_min is not None or ylim_max is not None:
        plt.ylim([ylim_min, ylim_max])
    if xlim_min is not None or xlim_max is not None:
        plt.xlim([xlim_min, xlim_max])
    plt.legend()
    plt.title('Average and std ' + fig_label + ' values.')
    plt.savefig(base_url + filename)
    plt.close(fig)

def plot_tau_and_effort_values(tau_values, effort_values):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    plt.plot(np.transpose(tau_values))
    plt.plot(np.transpose(effort_values))
    plt.ylim([0.0, 1.0])
    plt.xlim([1, 99])
    plt.title('Tau values and percentage of working agents for every simulation.')
    plt.savefig(base_url + 'tau_and_effort_values.png')
    plt.close(fig)

def plot_tau_and_effort_values_average_values(tau_values, effort_values):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    # Tau values
    avg_values = np.mean(tau_values, axis=0)
    std_values = np.std(tau_values, axis=0)

    plt.plot(steps, avg_values, label='Tau')
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)

    # Effort values
    avg_values = np.mean(effort_values, axis=0)
    std_values = np.std(effort_values, axis=0)

    plt.plot(steps, avg_values, label='Percentage of working agents')
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)

    plt.ylim([0.0, 1.0])
    plt.xlim([1, 99])
    plt.legend()
    plt.title('Average tau values and percentage of working agents for every simulation.')
    plt.savefig(base_url + 'tau_and_effort_average.png')
    plt.close(fig)

def plot_gine_and_normalized_effort_values_average_values(g_values, effort_values):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    # Gini values
    avg_values = np.mean(g_values, axis=0)
    std_values = np.std(g_values, axis=0)

    plt.plot(steps, avg_values, label='Gini')
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)

    # Effort values
    avg_values = np.mean(effort_values, axis=0)
    std_values = np.std(effort_values, axis=0)

    plt.plot(steps, avg_values, label='Normalized agent\'s effort')
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)

    plt.ylim([0.0, 1.0])
    plt.xlim([1, 99])
    plt.legend()
    plt.title('Average gini values and normalized agent\'s effort for every simulation.')
    plt.savefig(base_url + 'gini_and_normalized_effort_average.png')
    plt.close(fig)

def plot_gine_and_normalized_effort_values_average_values_with_tau(g_values, effort_values, tau_values):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    # Gini values
    avg_values = np.mean(g_values, axis=0)
    std_values = np.std(g_values, axis=0)

    plt.plot(steps, avg_values, label='Gini')
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)

    # Effort values
    avg_values = np.mean(effort_values, axis=0)
    std_values = np.std(effort_values, axis=0)

    plt.plot(steps, avg_values, label='Normalized agent\'s effort')
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)

    # Tau values
    avg_values = np.mean(tau_values, axis=0)
    std_values = np.std(tau_values, axis=0)

    plt.plot(steps, avg_values, label='Tau')
    plt.plot(steps, avg_values + std_values, linewidth=0.5, linestyle='dotted')
    plt.plot(steps, avg_values - std_values, linewidth=0.5, linestyle='dotted')
    ax.fill_between(steps, avg_values + std_values, avg_values - std_values, alpha=0.2)

    plt.ylim([0.0, 1.0])
    plt.xlim([1, 99])
    plt.legend()
    plt.title('Average gini values, normalized agent\'s effort and tau values for every simulation.')
    plt.savefig(base_url + 'gini_and_normalized_effort_average_with_tau.png')
    plt.close(fig)

def read_values(f_name):
    file_list = glob.glob(base_url + f_name)
    # Asumiré que solo hay uno.
    file = file_list[0]
    values = np.genfromtxt(file, skip_header=False, delimiter=';', dtype=str)
    replace_values = np.core.defchararray.replace(values, ',', '.')
    return replace_values.astype(float)

def min_list(list_values):
    min_value = float('inf')
    for item in list_values:
        min_item = min(item)
        min_value = min(min_item, min_value)

    return min_value

def max_list(list_values):
    max_value = float('-inf')
    for item in list_values:
        max_item = max(item)
        max_value = max(max_item, max_value)

    return max_value

def normalize(arr_list, t_min, t_max):

    diff = t_max - t_min
    min_arr = min_list(arr_list)
    # min_arr = 0
    diff_arr = max_list(arr_list) - min_arr

    norm_matrix = []
    # Ojo que arr es un array de dos dimensiones.
    for arr_mc in arr_list:
        norm_arr = []

        for i in arr_mc:
            temp = (((i - min_arr)*diff)/diff_arr) + t_min
            norm_arr.append(temp)

        norm_matrix.append(norm_arr)

    return norm_matrix

base_url = "C:\\Users\\IgnacioMoyaSeñas\\git\\redistribution-model\\experiments\\dummy\\"

steps = np.arange(100)

# Se lee tau
file_name = 'tau_*.csv'
t_values = read_values(file_name)

# Se lee gini
file_name = 'stepgini_*.csv'
gini_values = read_values(file_name)

# Se leen los effort_history
iterations = np.arange(50)
effort_list = []
effort_sum = []
for it in iterations:
    file_name = 'effortHistory_*_' + str(it) + '.csv'
    e_values = read_values(file_name)
    e_size = len(e_values)
    # Cuenta los agentes que se esfuerzan (posiciones que no son 0) y lo divide por el tamaño.
    positive_effort = np.count_nonzero(e_values, axis=0) / e_size
    positive_effort[0] = 1.0

    effort_list.append(positive_effort)
    # Normalizo los valores de esfuerzo por cada step
    effort_by_step = np.sum(e_values, axis=0)
    effort_by_step[0] = effort_by_step[1]
    effort_sum.append(effort_by_step)
    # normalized_effort_by_step = normalize(effort_by_step, 0, 1)
    # effort_normalized.append(normalized_effort_by_step)

effort_normalized = normalize(effort_sum, 0, 1)

# Plotea los valores en bruto (una linea por cada simulación).
plot_values(t_values, 'Tau', 'tau_values.png', ylim_min=0.2, ylim_max=0.6)
plot_average(t_values, 'tau', 'tau_average.png', ylim_min=0.2, ylim_max=0.6, xlim_min=1, xlim_max=99)

plot_values(gini_values, 'Gini', 'gini_values.png')
plot_average(gini_values, 'Gini', 'gini_average.png')

plot_tau_and_effort_values(t_values, effort_list)
plot_tau_and_effort_values_average_values(t_values, effort_list)

plot_gine_and_normalized_effort_values_average_values(gini_values, effort_normalized)
plot_gine_and_normalized_effort_values_average_values_with_tau(gini_values, effort_normalized, t_values)


plot_values(effort_normalized, 'Normalized effort', 'normalized_effort_values.png', ylim_min=0.0, ylim_max=1.0)
plot_average(effort_normalized, 'normalized effort', 'normalized_effort_average.png', ylim_min=0.0, ylim_max=1.0, xlim_min=1, xlim_max=99)

plot_values(effort_sum, 'Total effort', 'effort_values.png')
plot_average(effort_sum, 'total effort', 'effort_average.png', xlim_min=1, xlim_max=99)
