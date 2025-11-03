# Entorno de Machine Learning con Docker y UV

## 📋 Estructura del proyecto

```
tu-proyecto/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── notebooks/          # Tus Jupyter notebooks (se crea automáticamente)
└── data/              # Tus datasets (se crea automáticamente)
```

## 🚀 Instalación y uso

### 1. Crear la estructura inicial

```bash
mkdir ml-workspace
cd ml-workspace
mkdir notebooks data
```

### 2. Copiar los archivos

Coloca los archivos `Dockerfile`, `docker-compose.yml` y `pyproject.toml` en la carpeta `ml-workspace`.

### 3. Generar el lock file de UV (primera vez)

Necesitas tener UV instalado localmente para esto. Si no lo tienes:

```bash
# En Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# En Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Luego genera el lock file:

```bash
uv lock
```

### 4. Construir y ejecutar

```bash
docker compose up --build
```

### 4. Acceder a Jupyter

Abre tu navegador en: **http://localhost:8888**

No necesitas token, está configurado para desarrollo local.

## 🔧 Comandos útiles

### Detener el contenedor
```bash
docker compose down
```

### Ver logs
```bash
docker compose logs -f
```

### Reconstruir después de cambiar dependencias
```bash
# 1. Actualiza el lock file
uv lock

# 2. Reconstruye la imagen
docker compose up --build
```

### Añadir nuevas librerías

Edita `pyproject.toml` y añade la dependencia:

```toml
dependencies = [
    # ... existentes ...
    "tensorflow>=2.15.0",  # ejemplo
]
```

Luego ejecuta:
```bash
uv lock
docker compose up --build
```

## 📂 Persistencia de datos

- **notebooks/**: Todos tus notebooks se guardan aquí y persisten después de parar el contenedor
- **data/**: Coloca tus datasets aquí para acceder desde los notebooks

## 🎯 Alternativa: Jupyter Lab

Si prefieres Jupyter Lab en lugar de Jupyter Notebook, modifica el `CMD` en el Dockerfile:

```dockerfile
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
```

## ⚡ Ventajas de este setup

- **UV es rapidísimo**: Instalación de dependencias 10-100x más rápida que pip tradicional
- **Simple y directo**: Solo un archivo `requirements.txt` fácil de mantener
- **Aislado**: No contaminas tu sistema con dependencias
- **Portable**: Llevas todo el entorno en estos archivos