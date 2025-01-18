import matplotlib.pyplot as plt
import numpy as np

class HeatmapPlot:
    def __init__(self):
        pass

    @staticmethod
    def print_heat_map(name, data, url, theta_a, min_value=None, max_value=None):
        # Create the plot using pyplot
        # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
        fig, ax = plt.subplots()
        fig.set_size_inches(16, 16)
        # plt.imshow(data, cmap='twilight_shifted', interpolation='nearest')
        if min_value is None or max_value is None:
            plt.imshow(data)
        else:
            plt.imshow(data, vmin=min_value, vmax=max_value)
        fontsize_value = 20
        cbar = plt.colorbar()
        cbar.ax.tick_params(labelsize=fontsize_value)
        # Title and lables
        plt.title("Values of " + name + " at the end of the simulation", fontsize=fontsize_value)
        plt.ylabel("Theta", fontsize=fontsize_value)
        if theta_a:
            plt.xlabel("Effort cost (a)", fontsize=fontsize_value)
        else:
            plt.xlabel("Initial Tau", fontsize=fontsize_value)
        plt.xticks(fontsize=fontsize_value)
        plt.yticks(fontsize=fontsize_value)
        # Plot ticks
        ticks_max = len(data)
        ticks_step = int(ticks_max/10)
        ax.set_xticks(np.arange(0, ticks_max, step=ticks_step))
        ax.set_yticks(np.arange(0, ticks_max, step=ticks_step))
        fig.tight_layout()
        # Save the plot
        plt.savefig(url + name + '\\heatmap_' + name + '.png')
        # Clear the canvas
        plt.clf()
