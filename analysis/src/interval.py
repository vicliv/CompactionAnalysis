import matplotlib.pyplot as plt
xlabel = 'Time in seconds (s)'
ylabel = 'Number of operations in interval'

def plot(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    name = filename.split('.')[0]
    name = name.split('/')[3]
    name = name.split('Report')[0]

    x= []
    y= []
    lines.pop(0)
    for line in lines:
        data = line.split(',')
        x.append(int(data[0]))
        y.append(int(data[1].split('\n')[0]))
    
    plt.plot(x,y)
    title = "Number of operations per timed intervals\n of a " + name + " compaction test"
    plt.title(title)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    outputFilename = "analysis/plots/long/intervals/" + name + ".png"
    plt.savefig(outputFilename)
    plt.clf()

def main():
    plot("analysis/dbbenchResults/long/ReadHeavyLeveledReport.csv")
    plot("analysis/dbbenchResults/long/ReadHeavyTieredReport.csv")
    plot("analysis/dbbenchResults/long/WriteHeavyLeveledReport13.csv")
    plot("analysis/dbbenchResults/long/WriteHeavyTieredReport13.csv")


if __name__ == "__main__":
	main()