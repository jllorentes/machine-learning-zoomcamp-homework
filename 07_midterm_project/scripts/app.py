from fastapi import FastAPI
import joblib

app = FastAPI()

dv, model = joblib.load("xboost_model.bin")

@app.post("/predict")
def predict(student: dict):

    X = dv.transform([student])

    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1]

    return {
        "prediction": int(pred),
        "probability": float(proba)
    }
