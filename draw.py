import numpy as np
import pygraphviz as pgv

url = "/home/ignacio/proyectos/mo-calibration/results/results-by-instance/25TP/WOMM/data/"
methods = ["SPEA2", "NSGAII", "MOEAD"]
# methods = ["NSGAII"]
problemname = "/MWomABMProblem"


def computecolors(funarray):

    items = np.size(funarray, 0)
    objectives = np.size(funarray, 1)

    maxvalue = np.arange(objectives, dtype=np.float128)
    maxvalue.fill(0)
    minvalue = np.arange(objectives, dtype=np.float128)
    minvalue.fill(1000)

    for i in range(0, items):
        for j in range(0, objectives):
            if funarray[i][j] < minvalue[j]:
                minvalue[j] = funarray[i][j]
            if funarray[i][j] > maxvalue[j]:
                maxvalue[j] = funarray[i][j]

    # colors = np.chararray(funarray.shape)
    colors = np.empty(funarray.shape, dtype=object)

    for i in range(0, items):
        # for j in range(0, objectives):
        # n.attr['fillcolor']="red;0.5:orange"
        # "0.000 1.000 1.000"   'blah, blah %4.3f' %variable

        value0 = (funarray[i][0] - minvalue[0])/(maxvalue[0] - minvalue[0])
        value1 = (funarray[i][1] - minvalue[1]) / (maxvalue[1] - minvalue[1])

        colors[i][0] = '0.066 %1.3f 1.000' % (1-value0)
        colors[i][1] = '0.600 %1.3f 1.000' % (1-value1)

        # colors[i][0] = '0.066 %1.3f 1.000' % (1 - value0)
        # colors[i][1] = '0.772 %27.7f 0.765' % (1 - value1)

    return colors


def drawcolors(minvalue, maxvalue, funarray):

    items = np.size(funarray, 0)
    # objectives = np.size(funarray, 1)
    #
    # maxvalue = np.arange(objectives, dtype=np.float128)
    # maxvalue.fill(0)
    # minvalue = np.arange(objectives, dtype=np.float128)
    # minvalue.fill(1000)

    # for i in range(0, items):
    #     for j in range(0, objectives):
    #         if funarray[i][j] < minvalue[j]:
    #             minvalue[j] = funarray[i][j]
    #         if funarray[i][j] > maxvalue[j]:
    #             maxvalue[j] = funarray[i][j]

    # colors = np.chararray(funarray.shape)
    colors = np.empty(funarray.shape, dtype=object)

    for i in range(0, items):
        # for j in range(0, objectives):
        # n.attr['fillcolor']="red;0.5:orange"
        # "0.000 1.000 1.000"   'blah, blah %4.3f' %variable

        value0 = (funarray[i][0] - minvalue[0])/(maxvalue[0] - minvalue[0])
        value1 = (funarray[i][1] - minvalue[1]) / (maxvalue[1] - minvalue[1])

        colors[i][0] = '0.046 %1.3f 1.000' % (1-value0)
        colors[i][1] = '0.600 %1.3f 1.000' % (1-value1)

        # colors[i][0] = '0.046 %1.3f 1.000' % (1 - value0)
        # colors[i][1] = '0.772 %0.277f 1.000' % (1 - value1)

    return colors


def computeminmax(funarray):

    items = np.size(funarray, 0)
    objectives = np.size(funarray, 1)

    maxvalue = np.arange(objectives, dtype=np.float128)
    maxvalue.fill(0)
    minvalue = np.arange(objectives, dtype=np.float128)
    minvalue.fill(1000)

    for i in range(0, items):
        for j in range(0, objectives):
            if funarray[i][j] < minvalue[j]:
                minvalue[j] = funarray[i][j]
            if funarray[i][j] > maxvalue[j]:
                maxvalue[j] = funarray[i][j]

    container = {'minvalue': minvalue, 'maxvalue': maxvalue}

    return container


def compareminmax(localvalues, globalvalues):

    if len(globalvalues) == 0:
        return localvalues

    minvalue = np.minimum(globalvalues['minvalue'], localvalues['minvalue'])
    maxvalue = np.maximum(globalvalues['maxvalue'], localvalues['maxvalue'])

    # minvalue = comparemin(localvalues['minvalue'], globalvalues['minvalue'])
    # maxvalue = comparemax(localvalues['maxvalue'], globalvalues['maxvalue'])

    container = {'minvalue': minvalue, 'maxvalue': maxvalue}

    return container


def custommin(inputarray):
    customminvalue = 1000
    for iindex in range(0, np.size(inputarray, 0)):
        for jindex in range(0, np.size(inputarray, 0)):
            if inputarray[iindex][jindex] != -1 and inputarray[iindex][jindex] < customminvalue:
                customminvalue = inputarray[iindex][jindex]
    return customminvalue


def drawgraph(array, colorsarray, outputfile, outputdotfile):
    g = pgv.AGraph()

    g.node_attr['shape'] = 'circle'
    g.node_attr['fixedsize'] = 'true'
    g.node_attr['fontsize'] = 20
    # g.edge_attr['fontsize'] = 10
    g.edge_attr['fontsize'] = 16

    #g.graph_attr['orientation'] = 'landscape'
    #g.graph_attr['center'] = 1
    #g.graph_attr['ratio'] = 'fill'
    #g.graph_attr['mode'] = 'KK'

    #Buen seed para p-25
    #g.graph_attr['start'] = 2
    g.graph_attr['start'] = 2

    # g.graph_attr['epsilon'] = 0.01

    nnodes = array[0].size

    maxvalue = np.amax(array)
    minvalue = custommin(array)

    minmax = maxvalue - minvalue

    # print maxvalue, minvalue, (maxvalue/minvalue)

    maxpensize = 5

    for i in range(0, nnodes):
        relleno = colorsarray[i][0]+';0.5:'+colorsarray[i][1]
        # print relleno
        g.add_node(i, style='wedged', fillcolor=relleno)
    for j in range(0, nnodes):
        for k in range(0, nnodes):
            if array[j][k] != -1:
                # penvalue = (array[j][k]*10)/maxvalue
                penvalue = ((array[j][k]-minvalue)*maxpensize)/minmax
                if penvalue < 1:
                    penvalue = 1
                # print penvalue
                # g.add_edge(j, k, penwidth=penvalue, label='%.3f' % (array[j][k]))
                # g.add_edge(j, k, fontsize=12, penwidth=penvalue, xlabel='%.3f' % (array[j][k]))
                # g.add_edge(j, k, penwidth=penvalue, xlabel='%.3f' % (array[j][k])) len=1.5,
                g.add_edge(j, k, penwidth=penvalue, weight=penvalue, xlabel='%.1f' % (array[j][k]))
    h = g.handle
    c = pgv.AGraph(h, overlap=False, splines='true')
    c.write(outputdotfile)
    # c.layout(prog='neato')
    c.layout(prog='neato')
    c.draw(outputfile)
    # c.draw(outputfile, prog='circo')


globalminmax = {}

# Compute global min/max
for m in methods:
    inputfile = url + m + problemname + "/Objectives.tsv"
    localobjectives = np.loadtxt(inputfile, dtype=np.float)
    localminmax = computeminmax(localobjectives)

    globalminmax = compareminmax(localminmax, globalminmax)


for m in methods:
    inputfile = url + m + problemname + "/Graph.tsv"
    somefunarray = np.loadtxt(inputfile, dtype=np.float)

    inputfile = url + m + problemname + "/Objectives.tsv"
    objectivearray = np.loadtxt(inputfile, dtype=np.float)

    output = url + m + problemname + "/Graph.png"
    dotfile = url + m + problemname + "/Graph.dot"
    # drawgraph(somefunarray, computecolors(objectivesMap[m]), output, dotfile)
    drawgraph(somefunarray,
              drawcolors(globalminmax['minvalue'], globalminmax['maxvalue'], objectivearray), output, dotfile)


