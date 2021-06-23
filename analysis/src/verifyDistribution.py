import matplotlib.pyplot as plt

# File to run to verify the key distribution of the database given each selected key

# First sorts the keys in decreasing order of apperances
# Then plot them on a 100% scale.
def check(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    d = {}

    for key in lines:
        s = key.split('\n')[0]
        if s == '':
            continue
        if int(s) in d:
            d[int(s)] += 1
        else:
            d[int(s)] = 1
    
    f = open("analysis/SortedKeys.txt", 'w')
    for w in sorted(d, key=d.get, reverse=True):
        s = str(w) + " : " + str(d[w]) + '\n'
        f.write(s)
    f.close()

    x = []
    for i in range(0, len(d)):
        x.append(i/len(d)*100)

    sortedDict = dict(sorted(d.items(), key=lambda item: item[1]))
    plt.plot(x, [*sortedDict.values()])
    plt.title("Key distribution of the last benchmark test run")
    plt.yscale("log")
    plt.xticks([0,10,20,30,40,50,60,70,80,90,95,100])
    plt.savefig("analysis/keyDistribution.png")
    
if __name__ == "__main__":
    check("analysis/keys.txt")
