from fastapi import FastAPI
import joblib
import xgboost as xgb  # importa xgboost

app = FastAPI()

dv, model = joblib.load("xboost_model.bin")

feature_names = dv.get_feature_names_out().tolist()


@app.post("/predict")
def predict(student: dict):
    X = dv.transform([student])

    dmatrix = xgb.DMatrix(X, feature_names=feature_names)

    proba_1 = float(model.predict(dmatrix)[0])

    pred = int(proba_1 >= 0.5)

    return {
        "prediction": pred,
        "probability": proba_1
    }