import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#set theme
sns.set_theme(style='darkgrid')

X = np.array(
    [[35, 30000], [45, 45000], [40, 50000], [35, 35000], [25, 32500], [40, 40000]]
)

figure(figsize= (9, 9))
x = (X[:,0])
y = (X[:,1])

plt.title("2-D array")
plt.xlabel("sq metres")
plt.ylabel("house pice")

#create scatterplot
plt.scatter(x,y)
plt.show()