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
def parseReadWrite(filename, isRead):
    f = open(filename, 'r')
    lines = f.readlines()

    stats = []
    line = 19
    if (not isRead): # go for write line
        while(not lines[line] == '\n'):
            line += 1

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

    data = []
    data.append(stats)
    data.extend(histo(line, lines))

    return data



def histo(line, lines):
    data = []
    values = []
    percents = []

    i = 0
    while(lines[line] != '\n'):
        rangeNumbers = lines[line].split(',')
        if i==0:
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