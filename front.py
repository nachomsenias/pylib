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
    #print p_frontX
    p_frontY = [pair[1] for pair in p_front]
    #print p_frontY
    return p_frontX, p_frontY


url = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/final-mograms/25TP/WOMM/data/"


# url = "/home/ignacio/codingmadafaka/jmetaltest/olimpo/womM/WOMM/data/"


def printfrontier(urlin, urlout, plot=False):
    myarray = np.loadtxt(urlin, dtype=np.float32)
    myarrayfrontier = pareto_frontier(myarray[:, 0], myarray[:, 1], maxX=False, maxY=False)
    arrayfrontier = np.asarray(myarrayfrontier)
    trasposed = np.transpose(arrayfrontier)
    np.savetxt(urlout, trasposed, fmt='%10.5f%10.5f')
    if plot:
        plt.plot(myarrayfrontier[0], myarrayfrontier[1], 'ro')


methods = ["SPEA2","NSGAII","MOEAD"]


for m in methods:
    for i in range(0, 20):
        inputfile = url + m + "/MWomABMProblem/FUN" + str(i) + ".tsv"
        outputfile = url + m + "/MWomABMProblem/FUN" + str(i) + "_front.tsv"

        array = myArray = np.loadtxt(inputfile, dtype=np.float32)

        printfrontier(inputfile, outputfile)
#    printFrontier(url+m+"/MWomABMProblem/FUN_agg.tsv",url+m+"/MWomABMProblem/FUN_agg_front.tsv", plot= True)
#    plt.show()

printfrontier(url + "pareto_random.csv", url + "filtered_pareto_random.csv", plot=True)
plt.show()

