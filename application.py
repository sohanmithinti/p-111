import csv
import pandas as pd 
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random 

reader = pd.read_csv("marks.csv")
data = reader["Math_score"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

data1 = []
meanlist = []
for j in range(0, 1000):
    for i in range (0, 100):
       index = random.randint(0, len(data)-1)
       value = data[index]
       data1.append(value) 
    mean1 = statistics.mean(data1)
    meanlist.append(mean1) 
    data1 = [] 

mean2 = statistics.mean(meanlist)
std1 = statistics.stdev(meanlist)
std1_start, std1_end = mean2 - std1, mean2 + std1 
std2_start, std2_end = mean2 - (2*std1), mean2 + (2*std1)
std3_start, std3_end = mean2 - (3*std1), mean2 + (3*std1) 
print(mean2)
print(std1)

graph = ff.create_distplot([data], ["Mathscore"], show_hist=False)
graph.add_trace(go.Scatter(x = [mean2, mean2], y = [0, 0.17], mode = "lines", name = "mean")) 
graph.add_trace(go.Scatter(x = [std1_start, std1_start], y = [0, 0.17], mode = "lines", name = "std1_start"))
graph.add_trace(go.Scatter(x = [std1_end, std1_end], y = [0, 0.17], mode = "lines", name = "std1_end"))
graph.add_trace(go.Scatter(x = [std2_start, std2_start], y = [0, 0.17], mode = "lines", name = "std2_start"))
graph.add_trace(go.Scatter(x = [std2_end, std2_end], y = [0, 0.17], mode = "lines", name = "std2_end"))
graph.add_trace(go.Scatter(x = [std3_start, std3_start], y = [0, 0.17], mode = "lines", name = "std3_start"))
graph.add_trace(go.Scatter(x = [std3_end, std3_end], y = [0, 0.17], mode = "lines", name = "std3_end")) 
graph.show()

