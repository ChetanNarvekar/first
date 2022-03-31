import numpy as np  #required for mathematical calculation
import pandas as pd   #required for vector and array
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset
from google.colab import files
uploaded=files.upload()
temp = pd.read_csv("SalesNProfit.csv")
print(temp)
# 1) CountPlot
sns.countplot( data = temp)
plt.xlabel("X-axis")
plt.show()
#2) Pie Chart
a=temp.loc[:,"Sales"]
month=['1','2','3','4','5','6','7','8','9']
# Creating plot
fig = plt.figure(figsize =(10, 10))
plt.pie(a[1:10],labels = month)
 # show plot
plt.show()
# Numerical Data
#1) Scatter Plot
x = list(temp['Sales'])    #temp is the data name
y = list(temp['Profit'])   #temp is the data name
plt.scatter(x,y)         
plt.show()
#2) Box Plot
plt.boxplot(temp[1:23])
# show plot
plt.show() 
#3) Line plot
a=temp.loc[:,"Sales"]
x = list(a[:25])    
y = range(25)
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend('temp')
plt.title('The sales for first 25 years')
plt.plot(y,x)
plt.show()
   
