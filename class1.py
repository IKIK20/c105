import pandas as pd
import plotly.express as px
import csv

with open("class1.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#Removing headers from csv
file_data.pop(0)

sum = 0
n = len(file_data)

for marks in file_data:
    sum = sum + float(marks[1])

mean = sum/n
print("Mean is: " + str(mean))


df = pd.read_csv("class1.csv")

fig = px.scatter(df, x="Student Number", y = "Marks")


fig.update_layout(shapes = [dict(
    type = 'line',
    y0 = mean, y1 = mean,
    x0 = 0, x1 = n
)])

fig.show()