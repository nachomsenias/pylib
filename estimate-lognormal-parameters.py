import csv
import numpy as np
from scipy.stats import lognorm, boxcox
import matplotlib.pyplot as plt


def normalize_data(dict_values):
    # Suponiendo que tienes tus datos en una lista de listas: conjunto_datos, donde cada lista contiene los datos de una distribución
    normalized_dict = {}

    # Definir los percentiles (0.1, 0.2, ..., 0.9)
    percentiles = np.arange(0.1, 1, 0.1)

    # Estimar los valores de los percentiles para cada país utilizando interpolación lineal
    for pais, deciles in dict_values.items():
        valores_estimados = np.interp(percentiles, np.linspace(0, 1, 9), deciles)
        normalized_dict[pais] = valores_estimados

    return normalized_dict

def estimate_lognorm_parameters(deciles):
    # Calculate the mean and standard deviation of the log of the deciles
    log_deciles = np.log(deciles)
    log_mean = np.mean(log_deciles)
    log_std = np.std(log_deciles)

    # Use method of moments to estimate mu and sigma
    mu = log_mean
    sigma = log_std

    return mu, sigma

def plot_deciles(dict_values):
    # Definir los valores de los deciles y su posición en el eje x
    # valores_deciles = [10, 20, 30, 40, 50, 40, 30, 20, 10]
    # posiciones_deciles = range(1, len(valores_deciles) + 1)
    posiciones_deciles = list(range(1, 10))

    # Crear la gráfica
    plt.figure(figsize=(16, 12))
    # plt.plot(deciles, valores_deciles, marker='o', linestyle='-')

    # Etiquetas y título
    plt.xlabel('Decil')
    plt.ylabel('Valor de la renta')
    plt.title('Distribución de renta en la eurozona')

    for key_value, value_index in dict_values.items():
        plt.plot(posiciones_deciles, value_index, label=key_value, marker='o', linestyle='-')

    # Mostrar la gráfica
    plt.grid(True)
    plt.legend()
    plt.savefig("./eurozone_lognormal.png")

def export_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for row in data:
            writer.writerow(row)

def show_histogram(mu, sigma):
    # Histograma de los valores generados utilizando los parámetros estimados
    size = 10000  # Tamaño de la muestra

    # Generar muestras de la distribución lognormal
    samples = np.random.lognormal(mu, sigma, size)

    # Crear el histograma
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    # Añadir etiquetas y título
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

def plot_histograms(export_list):
    size = 20000  # Tamaño de la muestra
    # Generar muestras para cada distribución lognormal y crear los histogramas
    plt.figure(figsize=(20, 12))  # Tamaño de la figura

    for row in export_list[1:]:
        pais = row[0]
        mu = float(row[1])
        sigma = float(row[2])
        samples = np.random.lognormal(mu, sigma, size)
        plt.hist(samples, bins=30, density=True, alpha=0.4, label=pais)
        # plt.hist(samples, label=pais)

    # Añadir etiquetas y título
    plt.xlabel('Renta')
    plt.ylabel('Frecuencia')
    plt.title('Histogramas para las distribuciones de renta de la eurozona')
    plt.legend()
    plt.savefig("./eurozone_histogram.png")

values = {}
values["Belgium"] = [15.013, 18.278, 21.323, 24.591, 27.314, 30.478, 33.441, 37.812, 44.809]
values["Bulgaria"] = [2.248, 3.035, 3.730, 4.494, 5.378, 6.400, 7.657, 9.313, 12.491]
values["Czechia"] = [7.235, 8.718, 9.852, 10.985, 12.146, 13.404, 15.132, 17.213, 21.009]
values["Denmark"] = [18.548, 23.059, 26.261, 29.895, 33.260, 37.066, 41.092, 46.949, 56.288]
values["Germany"] = [13.232, 16.680, 19.461, 22.096, 25.000, 28.298, 32.178, 37.471, 46.764]
values["Estonia"] = [6.586, 8.312, 10.394, 12.463, 14.827, 17.179, 20.056, 23.776, 30.663]
values["Ireland"] = [15.791, 19.500, 22.467, 25.760, 29.060, 33.241, 36.567, 41.818, 51.104]
values["Greece"] = [4.453, 5.900, 7.080, 8.247, 9.520, 10.787, 12.383, 14.502, 18.100]
values["Spain"] = [7.207, 9.957, 12.303, 14.575, 16.814, 19.477, 22.456, 26.619, 33.425]
values["France"] = [11.898, 15.140, 18.025, 20.490, 23.053, 25.789, 29.080, 33.723, 41.995]
values["Croatia"] = [4.061, 5.546, 6.635, 7.712, 8.760, 9.938, 11.260, 12.974, 15.633]
values["Italy"] = [8.213, 11.135, 13.613, 15.981, 18.592, 21.182, 24.229, 28.317, 35.695]
values["Cyprus"] = [9.772, 11.723, 13.541, 15.574, 17.856, 20.142, 22.965, 26.601, 33.094]
values["Latvia"] = [4.338, 5.781, 7.313, 8.777, 10.258, 11.949, 14.053, 16.722, 21.353]
values["Lithuania"] = [4.646, 6.027, 7.350, 8.653, 10.195, 11.705, 13.931, 16.739, 22.542]
values["Luxembourg"] = [22.973, 28.646, 33.276, 39.111, 45.310, 50.533, 58.612, 66.500, 82.867]
values["Hungary"] = [4.035, 4.959, 5.520, 6.207, 6.975, 7.668, 8.688, 9.870, 12.133]
values["Malta"] = [9.501, 11.723, 13.739, 15.826, 18.155, 20.485, 23.429, 28.028, 35.004]
values["Netherlands"] = [15.910, 19.574, 22.684, 26.272, 29.537, 32.743, 36.114, 40.671, 48.922]
values["Austria"] = [14.320, 18.740, 21.894, 24.859, 27.844, 31.104, 35.061, 39.843, 48.145]
values["Poland"] = [4.819, 6.157, 7.182, 8.067, 8.946, 10.013, 11.192, 12.927, 15.784]
values["Portugal"] = [5.503, 7.191, 8.531, 9.744, 11.014, 12.496, 14.263, 17.164, 22.854]
values["Romania"] = [2.154, 3.168, 4.064, 4.768, 5.512, 6.427, 7.315, 8.655, 10.510]
values["Slovenia"] = [9.381, 11.704, 13.410, 15.057, 16.544, 18.165, 20.163, 22.606, 26.569]
values["Slovakia"] = [4.872, 6.351, 7.272, 8.117, 8.819, 9.665, 10.555, 11.787, 13.269]
values["Finland"] = [15.219, 18.024, 20.792, 23.549, 26.541, 29.270, 32.723, 37.699, 45.344]
values["Sweden"] = [13.620, 17.290, 20.559, 23.896, 26.692, 30.196, 33.887, 38.369, 45.797]

export_values = [["Name", "Mu", "Sigma"]]

values = normalize_data(values)

for kvalues, valores_estimados in values.items():
    # Estimate parameters
    # sigma, loc, scale = lognorm.fit(vvalues, floc=0)
    # mu = np.log(scale)

    # Calcular mu y sigma a partir de los valores estimados
    mu = np.log(np.mean(valores_estimados))
    sigma = np.sqrt(np.log(np.std(valores_estimados)**2 / np.mean(valores_estimados)**2 + 1))

    # show_histogram(mu, sigma)

    print("Estimated values for:", kvalues)
    print("Estimated mu:", mu)
    print("Estimated sigma:", sigma)

    export_values.append([kvalues, mu, sigma])

export_file = "./eurozone_lognormal.csv"
export_to_csv(export_values, export_file)

# Plot deciles
plot_deciles(values)
plot_histograms(export_values)

print("Fin.")
