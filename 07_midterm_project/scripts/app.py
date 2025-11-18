from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("xboost_model.bin")
# si usas DictVectorizer o Pipeline, cargarlo también

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/predict")
def predict(student: dict):
    # transformar features
    # X = dv.transform([student])
    # pred = model.predict(X)[0]
    # proba = model.predict_proba(X)[0][1]
    return {
        "prediction": int(pred),
        "probability": float(proba)
    }