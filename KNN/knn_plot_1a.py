import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# load data from csv
X = np.loadtxt(open("houses.csv", "rb"), delimiter=",", skiprows=1)

#set theme
sns.set_theme(style='darkgrid')

figure(figsize= (9, 9))
x = (X[:,0])
y = (X[:,1])

plt.title("sample data for KNN use")
plt.xlabel("sq metres")
plt.ylabel("house pice")

#create scatterplot
plt.scatter(x,y)
plt.show()