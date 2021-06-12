import matplotlib.pyplot as plt
import dbbenchParser as parser

duration = 3600
res = 1000

# Method to plot the number of operations using a time interval file
def plotOperations(filename, color, leg):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    name = filename.split('.')[0]
    name = name.split('/')[3]
    name = name.split('Report')[0]

    xlabel = 'Time in seconds (s)'
    ylabel = 'Number of operations in interval'

    x= []
    y= []
    lines.pop(0)
    for line in lines:
        data = line.split(',')
        x.append(int(data[0]))
        y.append(int(data[1].split('\n')[0]))
    
    plt.plot(x,y, color = color,  linewidth=1, label=leg)
    plt.legend()

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    outputFilename = "analysis/plots/Operations" + name + ".png"
    plt.savefig(outputFilename, dpi= res)

# Method to plot the write 99th percentile per interval of a run from the ouput file
def plotWrite99(filename1, filename2):
    name = filename1.split('.')[0]
    name = name.split('/')[3]
    name = name.split('Interval')[1]

    f = open(filename1, 'r')
    lines = f.readlines()
    f.close()
    x = []
    y = parser.getWrite99(lines)
    mult = duration/len(y)
    k = 0
    for i in range(0, len(y)):
        x.append(k+mult)
        k += mult

    plt.plot(x, y, color= 'b', label='Leveled',  linewidth=1)

    f = open(filename2, 'r')
    lines = f.readlines()
    f.close()
    x = []
    y = parser.getWrite99(lines)
    mult = duration/len(y)
    k = 0
    for i in range(0, len(y)):
        x.append(k+mult)
        k += mult
    xlabel = 'Time in seconds (s)'
    ylabel = '99th write percentile time during interval (ms)'

    plt.plot(x, y, color ='r', label = 'Tiered',  linewidth=1)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    outputFilename = "analysis/plots/99Write" + name + ".png"
    plt.savefig(outputFilename, dpi= res)
    plt.clf()

# Method to plot the read 99th percentile per interval of a run from the ouput file
def plotRead99(filename1, filename2):
    name = filename1.split('.')[0]
    name = name.split('/')[3]
    name = name.split('Interval')[1]

    f = open(filename1, 'r')
    lines = f.readlines()
    f.close()
    x = []
    y = parser.getWrite99(lines)
    mult = duration/len(y)
    k = 0
    for i in range(0, len(y)):
        x.append(k+mult)
        k += mult

    plt.plot(x, y, color= 'b', label='Leveled', linewidth=1)

    f = open(filename2, 'r')
    lines = f.readlines()
    f.close()
    x = []
    y = parser.getWrite99(lines)
    mult = duration/len(y)
    k = 0
    for i in range(0, len(y)):
        x.append(k+mult)
        k += mult

    xlabel = 'Time in seconds (s)'
    ylabel = '99th read percentile time during interval (ms)'

    plt.plot(x, y, color ='r', label = 'Tiered',  linewidth=1)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    outputFilename = "analysis/plots/99Read" + name + ".png"
    plt.savefig(outputFilename, dpi= res)
    plt.clf()

# Method to plot the number of bytes compacted per interval of a run from the ouput file
def plotCompactionWritten(filename1, filename2):
    name = filename1.split('.')[0]
    name = name.split('/')[3]
    name = name.split('Interval')[1]

    f = open(filename1, 'r')
    lines = f.readlines()
    f.close()
    x = []
    y = parser.getCompactionWrite(lines)
    mult = duration/len(y)
    k = 0
    for i in range(0, len(y)):
        x.append(k+mult)
        k += mult

    plt.plot(x, y, color= 'b', label='Leveled',  linewidth=1)

    f = open(filename2, 'r')
    lines = f.readlines()
    f.close()
    x = []
    y = parser.getCompactionWrite(lines)
    mult = duration/len(y)
    k = 0
    for i in range(0, len(y)):
        x.append(k+mult)
        k += mult

    xlabel = 'Time in seconds (s)'
    ylabel = 'Number of megabytes written in timed interval (MB)'

    plt.plot(x, y, color ='r', label = 'Tiered',  linewidth=1)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    outputFilename = "analysis/plots/CompactionWritten" + name + ".png"
    plt.savefig(outputFilename, dpi= res)
    plt.clf()


def main():
    plotOperations("analysis/dbbenchResults/final/ReadHeavyLeveledReport.csv", 'r', 'Leveled')
    plotOperations("analysis/dbbenchResults/final/ReadHeavyTieredReport.csv", 'b', 'Tiered')
    plt.clf()
    plotOperations("analysis/dbbenchResults/final/WriteHeavyLeveledReport.csv", 'r', 'Leveled')
    plotOperations("analysis/dbbenchResults/final/WriteHeavyTieredReport.csv", 'b', 'Tiered')
    plt.clf()
    plotOperations("analysis/dbbenchResults/final/ZipfianWriteHeavyLeveledReport.csv", 'r', 'Leveled')
    plotOperations("analysis/dbbenchResults/final/ZipfianWriteHeavyTieredReport.csv", 'b', 'Tiered')
    plt.clf()
    plotOperations("analysis/dbbenchResults/final/ZipfianReadHeavyLeveledReport.csv", 'r', 'Leveled')
    plotOperations("analysis/dbbenchResults/final/ZipfianReadHeavyTieredReport.csv", 'b', 'Tiered')
    plt.clf()

    plotWrite99("analysis/dbbenchResults/final/IntervalWriteHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalWriteHeavyTiered.txt")
    plotRead99("analysis/dbbenchResults/final/IntervalWriteHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalWriteHeavyTiered.txt")
    plotCompactionWritten("analysis/dbbenchResults/final/IntervalWriteHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalWriteHeavyTiered.txt")

    plotWrite99("analysis/dbbenchResults/final/IntervalReadHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalReadHeavyTiered.txt")
    plotRead99("analysis/dbbenchResults/final/IntervalReadHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalReadHeavyTiered.txt")
    plotCompactionWritten("analysis/dbbenchResults/final/IntervalReadHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalReadHeavyTiered.txt")

    plotWrite99("analysis/dbbenchResults/final/IntervalZipfianWriteHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalZipfianWriteHeavyTiered.txt")
    plotRead99("analysis/dbbenchResults/final/IntervalZipfianWriteHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalZipfianWriteHeavyTiered.txt")
    plotCompactionWritten("analysis/dbbenchResults/final/IntervalZipfianWriteHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalZipfianWriteHeavyTiered.txt")

    plotWrite99("analysis/dbbenchResults/final/IntervalZipfianReadHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalZipfianReadHeavyTiered.txt")
    plotRead99("analysis/dbbenchResults/final/IntervalZipfianReadHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalZipfianReadHeavyTiered.txt")
    plotCompactionWritten("analysis/dbbenchResults/final/IntervalZipfianReadHeavyLeveled.txt", "analysis/dbbenchResults/final/IntervalZipfianReadHeavyTiered.txt")

if __name__ == "__main__":
	main()