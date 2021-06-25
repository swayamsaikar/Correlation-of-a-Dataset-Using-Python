import csv
import plotly.express as px
import numpy as np


def plotGraph(dataPath):
    with open(dataPath) as f:
        df = csv.DictReader(f)
        figure = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        figure.show()


#  We are separating some values in the dataFrame and storing all values into an array and return those arrays
def SeparateData(dataPath):
    coffieData = []
    sleepData = []

    # get The Data Inside the csv
    with open(dataPath) as f:
        # print(dataFrame) #This is an array of objects(each rows)
        dataFrame = csv.DictReader(f)
        for row in dataFrame:
            # Converting the "Coffie in ml" -> value (that is a string) in an integer so that we can performthe operations
            coffieData.append(float(row["Coffee in ml"]))

            # Converting the "sleep in hours" -> value (that is a string) in an integer so that we can perform the operations
            sleepData.append(float(row["sleep in hours"]))

        # Here we are returning the coffieData array and the sleepData array as x and y
        return {
            "x": coffieData,
            "y": sleepData
        }


def corr(data):
    # This data parameter is basically in the objects {x:[coffieData],y:[sleepData]} and data["x"](means we are extracting the coffieData array and similar for y)
    # print(data) basically objects
    corelation = np.corrcoef(data["x"], data["y"])
    return corelation


if __name__ == '__main__':
    dataPath = "coffieData.csv"
    # plotGraph(dataPath)
    DataToBeCorrelated = SeparateData(dataPath)
    correlationResult = corr(DataToBeCorrelated)
    print(correlationResult)  # correlationResult is here
