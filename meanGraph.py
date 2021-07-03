import pandas as panda
import csv
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go
import random

df = panda.read_csv("temp.csv")
data = df["temp"].tolist()

#making a function to get the mean of the random data samples
def randSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randIndex = random.randint(0,len(data))
        value = data[randIndex]
        dataset.append(randIndex)
    meanOfData = statistics.mean(dataset)
    return meanOfData

#plotting the mean on the graph
def showGraph(meanList):
    df = meanList
    fig = ff.create_distplot([df],["temp"], show_hist=False)
    fig.show()

#making a function to get the mean of hundred data points a thousand times and to plot a graph
def loopData():
    mean_List = []
    for i in range(0,1000):
        setOfMeans = randSetOfMean(100)
        mean_List.append(setOfMeans)
    showGraph(mean_List)

loopData()

'''numbers = []
with open("temp.csv", newline='') as f:
    read = csv.reader(f)
    newData = list(read)
    newData.pop(0)
    length = len(newData)
    for total in range(0,length):
        for heat in newData:
            numbers.append(float(heat[0]))

mean = statistics.mean(newData)
print(mean)

std = statistics.stdev(newData)
print(std)

fig = ff.create_distplot([newData], ["Temperature"], show_hist=False)
#the mode LINES indicate that it will trace using a line
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name = "Mean"))
fig.show()

'''