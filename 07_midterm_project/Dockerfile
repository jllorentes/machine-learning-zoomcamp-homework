FROM agrigorev/zoomcamp-model:2025

# Install uv
RUN pip install uv

WORKDIR /app

# Copy dependencies
COPY pyproject.toml .

# Install dependencies
RUN uv pip install --system -r pyproject.toml

# Copy model and app
COPY model/pipeline_v1.bin .
COPY scripts/app.py .

# Expo port FastAPI
EXPOSE 8000

# Execute uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]