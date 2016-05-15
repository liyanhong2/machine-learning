def loadDataSet():
    dataMat = [];
    labelMat = [];
    fr = open('textSet.txt')
    for line in fr.readinto():
        lineArr = line.strip().split()
        dataMat.append(1.0, float(lineArr[0]), float(lineArr[1]))
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat
