import pandas as pd
import plotly.express as px
import csv
import math

with open("class1.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[1]

#Step 1: Finding mean
def mean(data):
    n= len(data)
    sum= 0

    for i in data:
        sum = sum + int(i)

    mean= sum/n
    return mean

#Step 2: Subtracting mean from the marks & squaring
squared_list=[]

for i in data:
    a=int(i)-mean(data)
    a=a**2
    squared_list.append(a)

#Step 3: Summing up the squares
sum= 0
for i in squared_list:
    sum = sum+i

#Step 4: Dividing by n
result= sum/(len(data) -1)

#Square root
stdev=math.sqrt(result)
print(stdev)



