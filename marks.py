import csv
import plotly.express as px
import numpy as np
def getDataSource(dataPath):
    daysPresent = []
    marks = []
    with open(dataPath , newline="") as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            daysPresent.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
    return {"x":daysPresent,"y": marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("the correlation coefficient is :"+ str(correlation[0,1]))

def main():
    dataPath = "marks.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
main()

