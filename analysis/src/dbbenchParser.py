def parseStats(filename):
    f = open(filename, 'r')
    lines = f.readlines()

    def init(line):
        keyValues = lines[line].split(':')
        val = keyValues[1].lstrip()
        if (val[-2].isdigit()):
            return [keyValues[0], val.split('\n')[0]]
        else:
            return [keyValues[0], val.split(' ')[0]]
    
    values = {}
    for i in range(2,15):
        keyValues = init(i)
        if keyValues[1][0].isdigit():
            if keyValues[1].find('.') == -1:
                values[keyValues[0]] = int(keyValues[1])
            else:
                values[keyValues[0]] = float(keyValues[1])
        else:
            values[keyValues[0]] = keyValues[1].replace('\n', '')
    f.close()
    
    return histo(23)

# parse the time values of read or write given
# if isRead = True we parse for read, otherwise for write
def parseHistoStats(lines, line):
    stats = []
    line -= 3

    for i in range(0, 3):
        s = lines[line].split(':')
        k = 1
        if i == 2:
            k = 2
        while (not s[k][-1] == '\n'):
            stats.append(float(s[k].strip().split(' ')[0]))
            k += 1
        stats.append(float(s[k].strip().replace('\n', '')))
        line += 1
    line += 1

    return stats



def parseHistogram(line, lines):
    line += 1
    data = []
    values = []
    percents = []

    i = 0
    while(lines[line] != '\n'):
        rangeNumbers = lines[line].split(',')
        if rangeNumbers[0][0] == '[':
            lowerBound = int(rangeNumbers[0].replace('[', ' ').lstrip())
        else:
            lowerBound = int(rangeNumbers[0].replace('(', ' ').lstrip())
        value = int(rangeNumbers[1].split(']')[1].lstrip().split(' ')[0])
        percentLeftString = lines[line].split('%')[0]
        percent = float(percentLeftString[percentLeftString.rfind(' '):-1:1])

        data.append(lowerBound)
        values.append(value)
        percents.append(percent)
        i += 1
        line += 1
    data.append(int(lines[line-1].split(',')[1].split(']')[0].replace(']', ' ').strip()))
    return [data, values, percents]


def findHistogram(lines):
    pos = []
    for i in range(0, len(lines)):
        if lines[i][0::8] == '-------':
            pos.append(i)
    return pos

def getRead99(lines):
    pos = findReadHistogram(lines)
    x = []
    for i in range(0, len(pos)):
        x.append(float(lines[pos[i]-1].split(':')[4].split('P')[0]))
    return x

def getWrite99(lines):
    pos = findWriteHistogram(lines)
    x = []
    for i in range(0, len(pos)):
        x.append(float(lines[pos[i]+3].split(':')[4].split('P')[0]))
    return x

def getCompactionWrite(lines):
    pos = findCompactionWrite(lines)
    x = []
    y = []
    for i in range(0, len(pos)):
        x.append(int(lines[pos[i]].split(':')[1])/(1024*1024))
    # y.append(x[0])
    # for i in range(1, len(x)):
    #     y.append(x[i]-x[i-1])
    return x

def findCompactionWrite(lines):
    pos = []
    for i in range(0, len(lines)):
        if "rocksdb.compact.write.bytes" in lines[i]:
            pos.append(i)
    return pos

def findReadHistogram(lines):
    pos = []
    for i in range(0, len(lines)):
        if lines[i] == 'Microseconds per read:\n':
            pos.append(i)
    return pos

def findWriteHistogram(lines):
    pos = []
    for i in range(0, len(lines)):
        if lines[i] == 'Microseconds per write:\n':
            pos.append(i)
    return pos
    