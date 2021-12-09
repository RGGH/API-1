
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression

app = FastAPI()


class request_body(BaseModel):
    cigs: int


## Data (#Cigarettes, #Cancer)
X = np.array([[0, "No"],
             [10, "No"],
             [60, "Yes"],
             [90, "Yes"],
              ])

## One-liner
model = LogisticRegression().fit(X[:, 0].reshape(-1, 1), X[:, 1])


output = {}

@app.post("/tabs")
def tabs(data: request_body):

    chance = model.predict([[data.cigs]])
    chance = "".join(chance)
    output["risk"] = chance

    return (output)
