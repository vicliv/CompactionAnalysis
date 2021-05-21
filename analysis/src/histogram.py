import matplotlib.pyplot as plt
import numpy as np
import dbbenchParser as parser
import copy

colors = {0 : 'b', 1 : 'r', 2 : 'g', 3 : 'c', 4: 'm', 5 : 'y', 6 : 'k', 7: 'w'}
xlabel = "Time distribution in microseconds per operation"
ylabel = "Log of number of operations per distribution"

def plotType(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    name = filename.split('.')[0].split('/')[2]

    pos =  parser.findHistogram(lines)

    plotRead(pos, lines, name, colors[0], "")
    outputFilename = "analysis/plots/" + name + "Reads.png"
    plt.savefig(outputFilename)
    plt.clf()

    plotWrite(pos, lines, name, colors[0], "")
    outputFilename = "analysis/plots/" + name + "Writes.png"
    plt.savefig(outputFilename)
    plt.clf()

    plotLevels(pos, lines, name)
    outputFilename = "analysis/plots/" + name + "Levelspng"
    plt.savefig(outputFilename)
    plt.clf()

def plotWorkload(filename1, filename2, workload):
    f1 = open(filename1, 'r')
    lines1 = f1.readlines()
    f1.close()

    f2 = open(filename2, 'r')
    lines2 = f2.readlines()
    f2.close()

    pos1 =  parser.findHistogram(lines1)
    pos2 =  parser.findHistogram(lines2)

    plotRead(pos1, lines1, workload, colors[0], "Leveled")
    plotRead(pos2, lines2, workload, colors[1], "Tiered")
    outputFilename = "analysis/plots/long/" + workload + "ReadsComparison.png"
    plt.savefig(outputFilename)
    plt.clf()

    plotWrite(pos1, lines1, workload, colors[0], "Leveled")
    plotWrite(pos2, lines2, workload, colors[1], "Tiered")
    outputFilename = "analysis/plots/long/" + workload + "WritesComparison.png"
    plt.savefig(outputFilename)
    plt.clf()

def plotLevels(pos, lines, name):
    for i in range(2, len(pos)):
        data = parser.parseHistogram(pos[i], lines)

        x = copy.copy(data[0])
        x.pop(len(data[1]))

        l = "L" + str(i-2) + " reads"

        plt.hist(x, bins=data[0], weights=data[1], log=True, color=colors[(i-2)%8], label=l, alpha = 0.5, ls = "dashed", edgecolor = "black", linewidth = 0.2)
    
    title = "Histogram of a " + name + " database with\n read/writes per level time in microseconds"
    plt.title(title)
    plt.legend()

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def plotRead(pos, lines, name, color, l):
    data = parser.parseHistogram(pos[0], lines)

    x = copy.copy(data[0])
    x.pop(len(data[1]))

    plt.hist(x, bins=data[0], weights=data[1], label=l, log=True, color=color, alpha = 0.5)

    title = "Histogram of a " + name + " database with\n reads time in microseconds"
    plt.title(title)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if (l != ""):
        plt.legend()

def plotWrite(pos, lines, name, color, l):
    data = parser.parseHistogram(pos[1], lines)

    x = copy.copy(data[0])
    x.pop(len(data[1]))

    plt.hist(x, bins=data[0], weights=data[1], label=l, log=True, color=color, alpha = 0.5)
 
    title = "Histogram of a " + name + " database with\n writes time in microseconds"
    plt.title(title)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if (l != ""):
        plt.legend()

def main():
    plotWorkload("analysis/dbbenchResults/long/ReadHeavyLeveled.txt", "analysis/dbbenchResults/long/ReadHeavyTiered.txt", "ReadHeavy")
    plotWorkload("analysis/dbbenchResults/long/WriteHeavyLeveled13.txt", "analysis/dbbenchResults/long/WriteHeavyTiered13.txt", "WriteHeavy")


if __name__ == "__main__":
	main()
    
