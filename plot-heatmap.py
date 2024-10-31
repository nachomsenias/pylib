from matrix.matrix_utils import MatrixUtils
from plot.heatmap_plot import HeatmapPlot
import sys

# Código antiguo para filtrar valores
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

# No usamos main porque este script no se importa en otro módulo
data_name = sys.argv[1]
base_url = sys.argv[2]

print('Running ' + data_name + '...')
matrix = MatrixUtils.get_matrix(data_name, base_url)

HeatmapPlot.print_heat_map(data_name, matrix, base_url)
