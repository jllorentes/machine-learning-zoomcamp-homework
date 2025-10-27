import pickle

# Cargar el pipeline
with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

# Registro a evaluar
record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Calcular probabilidad de conversión
proba = model.predict_proba([record])[0, 1]

print(f"Probability of conversion: {proba:.3f}")
