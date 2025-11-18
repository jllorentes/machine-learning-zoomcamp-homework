FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

# Copiar dependencias
COPY requirements_deployemnt.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements_deployemnt.txt

# Copiar modelo y app
COPY model/xboost_model.bin .
COPY scripts/app.py .

# Exponer puerto FastAPI
EXPOSE 8000

# Ejecutar uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]