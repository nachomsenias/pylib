import numpy as np
import pygraphviz as pgv

from draw import drawgraph, drawcolors, computeminmax

# url = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/womM_newhistory/WOMM/data/"
# url = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/25TP/WOMM/data/"

# inputfile = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/0TP/WOMM/data/SPEA2/MWomABMProblem/Graph4.tsv"
# inputfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/example/Graph_example.csv"
# inputfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/first_rev/graficas55/Graph2.tsv"
inputfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/first_rev/graficas25/Graph16.tsv"
somefunarray = np.loadtxt(inputfile, dtype=np.float)

# inputfile = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/0TP/WOMM/data/SPEA2/MWomABMProblem/Objectives4.tsv"
# inputfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/example/Objectives_example.txt"
# inputfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/first_rev/graficas55/Objectives2.tsv"
inputfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/first_rev/graficas25/Objectives16.tsv"
objectivearray = np.loadtxt(inputfile, dtype=np.float)

localminmax = computeminmax(objectivearray)

# output = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/0TP/WOMM/data/SPEA2/MWomABMProblem/Graph4.png"
# output = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/example/Graph_example.png"
output = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/first_rev/graficas25/network.png"


# dotfile = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/0TP/WOMM/data/SPEA2/MWomABMProblem/Graph4.dot"
# dotfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/example/Graph_example.dot"
dotfile = "/home/ignacio/Dropbox/papers/mograms calibracion/latex/figures/first_rev/graficas25/network.dot"

# drawgraph(somefunarray, computecolors(objectivesMap[m]), output, dotfile)
drawgraph(somefunarray, drawcolors(localminmax['minvalue'], localminmax['maxvalue'], objectivearray), output, dotfile)
