from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
from sklearn.neighbors import KNeighborsRegressor

app = FastAPI()

output = {}

# load data from csv
X = np.loadtxt(open("houses.csv", "rb"), delimiter=",", skiprows=1).astype("int")
print(X)

## One Liner
KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:, 0].reshape(-1, 1), X[:, 1])
print(KNN)

class knnx(BaseModel):
    sqm: int

@app.post("/foo")
def index(data: knnx):

    res = KNN.predict([[data.sqm]])
    res = round(res[0],2)
    #res = "".join(str(res))
    output["price"] = res

    return output
