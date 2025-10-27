import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Instead of reading te json, I create a class for te POST
class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# --- Endpoint to predict ---
@app.post("/predict")
def predict(client: Client):
    record = client.dict()
    probability = model.predict_proba([record])[0, 1]
    return {"subscription_probability": round(float(probability), 3)}
