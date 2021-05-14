import matplotlib.pyplot as plt
import numpy as np
import dbbenchParser as parser
import copy

colors = {0 : 'b', 1 : 'r', 2 : 'g', 3 : 'c', 4: 'm', 5 : 'y', 6 : 'k', 7: 'w'}

def histogramPlot(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    name = filename.split('.')[0].split('/')[2]

    pos =  parser.findHistogram(lines)

    for i in range(0, 2):
        data = parser.parseHistogram(pos[i], lines)

        x = copy.copy(data[0])
        x.pop(len(data[1]))

        if (i==0):
            l = "Reads"
        elif (i==1):
            l = "Writes"

        plt.hist(x, bins=data[0], weights=data[1], log=True, color=colors[i%8], label=l, alpha = 0.5)

    title = "Histogram of a " + name + " database with\n read/writes time in microseconds"
    plt.title(title)
    plt.legend()

    xlabel = "Time distribution in microseconds per operation"
    plt.xlabel(xlabel)
    ylabel = "Log of number of operations per distribution"
    plt.ylabel(ylabel)

    outputFilename = "analysis/plots/" + name + ".jpeg"
    plt.savefig(outputFilename)
    plt.clf()

    for i in range(2, len(pos)):
        data = parser.parseHistogram(pos[i], lines)

        x = copy.copy(data[0])
        x.pop(len(data[1]))

        l = "L" + str(i-2) + " reads"

        plt.hist(x, bins=data[0], weights=data[1], log=True, color=colors[(i-2)%8], label=l, alpha = 0.5, ls = "dashed", edgecolor = "black", linewidth = 0.2)
    
    title = "Histogram of a " + name + " database with\n read/writes per level time in microseconds"
    plt.title(title)
    plt.legend()

    xlabel = "Time distribution in microseconds per operation"
    plt.xlabel(xlabel)
    ylabel = "Log of number of operations per distribution"
    plt.ylabel(ylabel)

    outputFilename = "analysis/plots/" + name + "Levels.jpeg"
    plt.savefig(outputFilename)
    plt.clf()

def main():
    histogramPlot("analysis/dbbenchResults/ReadHeavyLeveled.txt")
    histogramPlot("analysis/dbbenchResults/ReadHeavyTiered.txt")
    histogramPlot("analysis/dbbenchResults/WriteHeavyLeveled.txt")
    histogramPlot("analysis/dbbenchResults/WriteHeavyTiered.txt")
    histogramPlot("analysis/dbbenchResults/1%Leveled.txt")
    histogramPlot("analysis/dbbenchResults/1%Tiered.txt")

if __name__ == "__main__":
	main()
    