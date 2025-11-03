FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Crear directorio de trabajo
WORKDIR /workspace

# Copiar archivos de dependencias
COPY requirements.txt ./

# Instalar dependencias con UV
RUN uv pip install --system -r requirements.txt

# Exponer puerto de Jupyter
EXPOSE 8888

# Comando por defecto: iniciar Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]