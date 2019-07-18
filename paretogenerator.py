import numpy as np
import matplotlib.pyplot as plt


def pareto_frontier(Xs, Ys, maxX = True, maxY = True):
    myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
    p_front = [myList[0]]
    for pair in myList[1:]:
        if maxY:
            if pair[1] >= p_front[-1][1]:
                p_front.append(pair)
        else:
            if pair[1] <= p_front[-1][1]:
                p_front.append(pair)
    p_frontX = [pair[0] for pair in p_front]
    # print p_frontX
    p_frontY = [pair[1] for pair in p_front]
    # print p_frontY
    return p_frontX, p_frontY


def printFrontier(urlIn,urlOut, plot = False):
    myArray = np.loadtxt(urlIn, dtype=np.float32)
    myArrayFrontier = pareto_frontier(myArray[:, 0], myArray[:, 1], maxX=False, maxY=False)
    arrayfrontier = np.asarray(myArrayFrontier)
    trasposed = np.transpose(arrayfrontier)
    np.savetxt(urlOut, trasposed, fmt='%10.5f,%10.5f')
    if plot:
        plt.plot(myArrayFrontier[0], myArrayFrontier[1], 'ro')


def loadFiles(urlIn):
    myArray = np.loadtxt(urlIn, dtype=np.float32)
    return myArray


url = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/womM_newhistory/WOMM/data/"
# url = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/womM/WOMM/data/"
methods = ["SPEA2", "NSGAII", "MOEAD"]
iterations = 15

for m in methods:
    funarray = np.empty([1, 2])
    vararray = np.empty([1, 2])
    for i in range(0, iterations):
        inputfile = url + m + "/MWomABMProblem/FUN" + str(i) + ".tsv"
        somefunarray = np.loadtxt(inputfile, dtype=np.float32)

        inputfile = url + m + "/MWomABMProblem/VAR" + str(i) + ".tsv"
        somevararray = np.loadtxt(inputfile, dtype=np.float32)

        funarray = np.append(funarray, somefunarray, axis=0)
        vararray = np.append(vararray, somevararray, axis=0)

        print funarray
        print vararray

    urlout = url + m + "/MWomABMProblem/FUN_agg.tsv"
    np.savetxt(urlout, funarray, fmt='%10.5f,%10.5f')
