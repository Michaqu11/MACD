import csv

def read_data():
    file = open('csv/NFLX.csv')
    csvreader = csv.reader(file)
    data = []
    close = []
    for row in csvreader:
        changeToFloatList = []
        for item in row:
            if changeToFloatList:
                changeToFloatList.append(float(item))
                if len(changeToFloatList) == 4:
                    close.append(float(item))
            else:
                changeToFloatList.append(item)
        data.append(changeToFloatList)
    file.close()
    return (data, close)