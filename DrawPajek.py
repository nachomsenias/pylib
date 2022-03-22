import numpy as np
import pygraphviz as pgv
import sys

from draw import drawwithedges, drawcolors, computeminmax

# This argument should contain the full tsv path (i.e., "Pajek2.tsv_mograms")

graphfile = "/home/ignacio/proyectos/MM-MO/Data/soluciones/mograms/Omni0.1/TP25/Pajek18.tsv_mograms"
# graphfile = sys.argv[1]

body = graphfile.split("Pajek")
head = body[0]
executionId = body[1].split(".tsv_mograms")[0]

objectivesFile = head + "Objectives" + executionId + ".tsv"

# grapharray = np.loadtxt(graphfile, dtype=np.string)
f = open(graphfile, 'r')
line = f.readline()
while line != "*edges\n" and line:
    line = f.readline()

if line != "*edges\n":
    exit(1)

edges = []
line = f.readline()
while line:
    values = line[:-1]
    edges.append(values.split(" "))
    line = f.readline()

f.close()

objectivearray = np.loadtxt(objectivesFile, dtype=np.float)

localminmax = computeminmax(objectivearray)

output = head + "network" + str(executionId) + ".png"
dotfile = head + "network" + str(executionId) + ".dot"

drawwithedges(edges, objectivearray, drawcolors(localminmax['minvalue'], localminmax['maxvalue'],
                                                objectivearray), output, dotfile)