from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
from sklearn.neighbors import KNeighborsRegressor

app = FastAPI()

output = {}

X = np.array(
    [[35, 30000], [45, 45000], [40, 50000], [35, 35000], [25, 32500], [40, 40000]]
)

## One Liner
KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:, 0].reshape(-1, 1), X[:, 1])


class knnx(BaseModel):
    sqm: int


@app.post("/foo")
def index(data: knnx):

    res = KNN.predict([[data.sqm]])
    res = res[0]
    res = "".join(str(res))
    output["price"] = res

    return output
