import csv
import plotly.express as px
import numpy as np
def getDataSource(dataPath):
    coffee = []
    hoursSlept = []
    with open(dataPath , newline="") as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            hoursSlept.append(float(row["sleep in hours"]))
    return {"x":coffee,"y": hoursSlept}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("the correlation coefficient is :"+ str(correlation[0,1]))

def main():
    dataPath = "coffee.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
main()
