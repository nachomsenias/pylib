import matplotlib.pyplot as plt
import numpy as np


def computevalues(e):
    return (e * e) / 2


evalues = np.arange(100)
print(evalues)
computed_e = computevalues(evalues)
print(computed_e)

plt.plot(evalues, computed_e)

plt.show()
