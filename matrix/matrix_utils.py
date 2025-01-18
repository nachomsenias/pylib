import math
import numpy as np
import glob
import os


class MatrixUtils:
    def __init__(self):
        pass

    @staticmethod
    def gather_matrix_values(file_list, theta_a, output_file):
        # We assume that the matrixes are squared.
        matrix_size = int(math.sqrt(len(file_list)))
        if theta_a and matrix_size == 98:
            matrix_size += 1
        matrix = np.zeros(shape=(matrix_size + 1, matrix_size + 1), dtype=float)

        for file in file_list:
            values = np.genfromtxt(file, skip_header=True, delimiter=';', dtype=float)
            avg_value = np.mean(values[:, -1], axis=0)
            path = file.split('\\')
            tokens = path[-1].split('_')

            theta_index = round(float(tokens[0]) * matrix_size)
            tau_index = MatrixUtils.get_index(tokens[1], theta_a, matrix_size)

            last_avg_value = avg_value
            matrix[theta_index, tau_index] = last_avg_value

        # Store the matrix values
        matrix.tofile(output_file, sep=';')
        np.savetxt(output_file, matrix, delimiter=';')

        return matrix

    @staticmethod
    def get_index(token, theta_a, matrix_size):
        if theta_a:
            index_value = int(token)
        else:
            index_value = round(float(token) * matrix_size)

        return index_value

    @staticmethod
    def get_matrix(kpi, base_url, theta_a):
        output_name = base_url + kpi + '\\matrix_' + kpi + '.csv'
        try:
            return np.genfromtxt(output_name, delimiter=';', dtype=float)
        except Exception as e:
            print(e)
            print('Matrix not found, gathering it from scratch...')
            os.makedirs(base_url + kpi, exist_ok=True)
            file_name = '*_*_' + kpi + '_*.csv'
            file_list = glob.glob(base_url + file_name)
            return MatrixUtils.gather_matrix_values(file_list, theta_a, output_file=output_name)
