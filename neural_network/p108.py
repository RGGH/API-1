## Dependencies
from sklearn.neural_network import MLPRegressor
import numpy as np

## questionaire data
data = np.loadtxt(open("questions.csv", "rb"), delimiter=",", skiprows=1)

## one liner
# fit first 4 v 5th(last)
# study per week, years, books, projects, ear, rating

neural_net = MLPRegressor(max_iter=10000).fit(data[:,:-1], data[:,-1])

## result
res = neural_net.predict([[10,2,4,4,2500]])
print (res)