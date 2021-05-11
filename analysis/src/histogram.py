import matplotlib.pyplot as plt
import numpy as np
import dbbenchParser as parser
import copy

def histogramPlot(filename, type):
    data = parser.parseReadWrite(filename, True)
    x = copy.copy(data[1])
    x.pop(len(data[2]))

    plt.hist(x, bins=data[1], weights=data[2], log=True)

    title = "Histogram of a " + workload + " database with a " + compactionPolicy + " compaction policy\nof time of " + type + " in microseconds"
    plt.title(title)

    xlabel = "Time distribution in microseconds per " + type
    plt.xlabel(xlabel)
    ylabel = "Log of number of " + type + "s per distribution"
    plt.ylabel(ylabel)

    outputFilename = "plots/" + workload.title() + type.title() + compactionPolicy.title() + ".jpeg"
    plt.savefig(outputFilename)
    plt.show()

def test():
	histogramPlot("dbbenchResults/result.txt", "read", "Write_Heavy", "leveled")

def main():
    histogramPlot("dbbenchResults/ReadHeavyLeveled.txt", read)
    histogramPlot("dbbenchResults/ReadHeavyTiered.txt", read)

if __name__ == "__main__":
	main()
    