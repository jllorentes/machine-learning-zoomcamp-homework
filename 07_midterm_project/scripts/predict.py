import pickle

# Load Pipeline
with open('xboost_model.bin', 'rb') as f:
    model = pickle.load(f)

# Registro a evaluar
record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Calcular probabilidad de conversión
proba = model.predict_proba([record])[0, 1]

print(f"Probability of dropout: {proba:.3f}")

def predict_drop(alumn, dv, model):
    X = dv.transform([alumn])
    y_pred = model.predict(X)
    return y_pred[0]


with open('xboost_model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)




