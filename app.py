from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import numpy as np
import os

app = FastAPI()

# dane treningowe
X = np.array([
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [6.0, 9.0],
    [1.2, 0.8],
    [8.0, 8.0]
])

y = np.array([0, 0, 1, 1, 0, 1])

# trenowanie modelu
model = LogisticRegression()
model.fit(X, y)

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def root():
    return {"message": "API działa poprawnie"}

@app.exception_handler(RequestValidationError)
async def validationExceptionHandler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "nieprawidlowe dane wejsciowe",
            "details": exc.errors()
        }
    )

@app.post("/predict")
def predict(data: InputData):
    inputData = np.array([[data.feature1, data.feature2]])
    prediction = model.predict(inputData)[0]

    return {"prediction": int(prediction)}

@app.get("/info")
def info():
    appEnv = os.getenv("APP_ENV", "local")

    return {
        "modelType": "LogisticRegression",
        "numberOfFeatures": X.shape[1],
        "numberOfClasses": len(model.classes_),
        "classes": model.classes_.tolist(),
        "appEnv": appEnv
    }

@app.get("/health")
def health():
    return {"status": "ok"}