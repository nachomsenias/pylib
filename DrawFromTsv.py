import numpy as np
import pygraphviz as pgv
import sys

from draw import drawgraph, drawcolors, computeminmax

# This argument should contain the full tsv path (i.e., "Graph17.tsv")
graphfile = sys.argv[1]

body = graphfile.split("Graph")
head = body[0]
executionId = body[1].split(".tsv")[0]

objectivesFile = head + "Objectives" + executionId + ".tsv"

grapharray = np.loadtxt(graphfile, dtype=np.float)
objectivearray = np.loadtxt(objectivesFile, dtype=np.float)

localminmax = computeminmax(objectivearray)

output = head + "network" + str(executionId) + ".png"
dotfile = head + "network" + str(executionId) + ".dot"

drawgraph(grapharray, drawcolors(localminmax['minvalue'], localminmax['maxvalue'], objectivearray), output, dotfile)
