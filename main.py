# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from sklearn import datasets
from sklearn.model_selection import train_test_split
from scrappy_knn import ScrappyKNN
from typing import List

# Load dataset
iris = datasets.load_iris()
features = iris.data
labels = iris.target

# Split dataset
features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.5
)

# Train your ScrappyKNN model
model = ScrappyKNN()
model.fit(features_train, labels_train)

# Define FastAPI app
app = FastAPI(title="ScrappyKNN Iris Predictor API")

# Define input model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Welcome to the ScrappyKNN Iris Predictor!"}

@app.post("/predict")
def predict_species(data: IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = model.predict(features)
    species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
    return {
        "predicted_class": int(prediction[0]),
        "species": species_map[prediction[0]]
    }
