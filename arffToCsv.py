#########################################
# Project   : ARFF to CSV converter     #
# Created   : 10/01/17 11:08:06         #
# Author    : haloboy777                #
# Update by : rambasnet                 #
# Licence   : MIT                       #
#########################################

# Importing library
import os
import sys


# Function for converting arff list to csv list
def toCsv(content):
    data = False
    header = ""
    newContent = []
    for line in content:
        if not data:
            if "@attribute" in line:
                attri = line.split()
                columnName = attri[attri.index("@attribute")+1]
                header = header + columnName + ","
            elif "@data" in line:
                data = True
                header = header[:-1]
                header += '\n'
                newContent.append(header)
        else:
            newContent.append(line)
    return newContent


def main(dirPath):
    # Main loop for reading and writing files
    # Getting all the arff files from the given directory
    files = [os.path.join(dirPath, arff)
             for arff in os.listdir(dirPath) if arff.endswith(".arff")]
    for file in files:
        with open(file, "r") as inFile:
            content = inFile.readlines()
            name, ext = os.path.splitext(inFile.name)
            new = toCsv(content)
            with open(name+".csv", "w") as outFile:
                outFile.writelines(new)
    print('all done...')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 arffToCsv.py directoryPath')
        sys.exit()

    main(sys.argv[1])
