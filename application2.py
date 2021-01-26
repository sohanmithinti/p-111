import csv
import pandas as pd 
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random 

reader1 = pd.read_csv("mark2.csv")
data = reader1["Math_score"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

print(mean)
print(std)

std1_start, std1_end = mean - std, mean + std
std2_start, std2_end = mean - (2*std), mean + (2*std)
std3_start, std3_end = mean - (3*std), mean + (3*std) 

graph = ff.create_distplot([data], ["Mathscore"], show_hist=False)
graph.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean")) 
graph.add_trace(go.Scatter(x = [std1_start, std1_start], y = [0, 0.17], mode = "lines", name = "std1_start"))
graph.add_trace(go.Scatter(x = [std1_end, std1_end], y = [0, 0.17], mode = "lines", name = "std1_end"))
graph.add_trace(go.Scatter(x = [std2_start, std2_start], y = [0, 0.17], mode = "lines", name = "std2_start"))
graph.add_trace(go.Scatter(x = [std2_end, std2_end], y = [0, 0.17], mode = "lines", name = "std2_end"))
graph.add_trace(go.Scatter(x = [std3_start, std3_start], y = [0, 0.17], mode = "lines", name = "std3_start"))
graph.add_trace(go.Scatter(x = [std3_end, std3_end], y = [0, 0.17], mode = "lines", name = "std3_end")) 
graph.show()