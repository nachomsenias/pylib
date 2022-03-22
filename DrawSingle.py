import numpy as np
import pygraphviz as pgv

from draw import drawgraph, drawcolors, computeminmax

# path = "/home/ignacio/Descargas/Data-20210322T091507Z-001/Data/soluciones/NSGAIIOriginal0/WomABMProblem-TP0/"
# path = "/home/ignacio/Descargas/Data-20210322T091507Z-001/Data/soluciones/Omni0/WomABMProblem-TP0/"
# path = "/home/ignacio/Descargas/Data-20210322T091507Z-001/Data/soluciones/Omni0.05/WomABMProblem-TP0/"
path = "/home/ignacio/Descargas/Data-20210322T091507Z-001/Data/soluciones/Omni0.1/WomABMProblem-TP0/"
executionId = 17
graphfile = path + "Graph" + str(executionId) + ".tsv"
objectivesFile = path + "Objectives" + str(executionId) + ".tsv"

grapharray = np.loadtxt(graphfile, dtype=np.float)
objectivearray = np.loadtxt(objectivesFile, dtype=np.float)

localminmax = computeminmax(objectivearray)

output = path + "network" + str(executionId) + ".png"
dotfile = path + "network" + str(executionId) + ".dot"

drawgraph(grapharray, drawcolors(localminmax['minvalue'], localminmax['maxvalue'], objectivearray), output, dotfile)