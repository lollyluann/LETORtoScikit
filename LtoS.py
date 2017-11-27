# Luann Jung
# 11/26/2017

import sys

fileName = sys.argv[1]
classesFile = sys.argv[2]

def readFile():
    count = 0
    with open(fileName) as fp:
        for line in fp:
            processLine(line, count+1, count)
            count += 1

def processLine(line, lineNumber, count):
    columns = removeComments(line)
    if (lineNumber==1):
        saveAttributes(columns)
    writeFile(columns, lineNumber, count)

def removeComments(line):
    columns = line.split(" ")
    for el in range(len(columns)):
        if columns[el][0] == '#':
            return columns[0:el]

def saveAttributes(columns):
    attributes = []
    for a in columns[2:]:
        attributes.append(a.split(":")[0])
    writeFileName = fileName[:len(fileName) - 4] + "-attr.csv"
    with open(writeFileName, "a+") as f:
        f.write(','.join(str(x) for x in attributes))

def listClasses():
    #reads from a file with the all of the possible class names comma-delimited in the first line
    with open(classesFile) as fp:
        return ",".join(str(x) for x in fp.readline().split(","))

def calcFeaturesLines(columns):
    return len(columns) - 2, sum(1 for line in open(fileName))

def getData(columns):
    values = []
    classLabel = columns[0]
    for a in columns[2:]:
        values.append(a.split(":")[1])
    return values, classLabel

def writeFile(columns, lineNumber, count):
    writeFileName = fileName[:len(fileName) - 4] + "-converted.csv"
    numFeatures, numLines = calcFeaturesLines(columns)
    with open(writeFileName, "a+") as f:
        if lineNumber == 1:
            f.write("{0},{1},".format(numLines, numFeatures) + listClasses() + "\n")
        else:
            val, cls = getData(columns)
            f.write(','.join(str(x) for x in val) + "," + cls + "\n")

readFile()
