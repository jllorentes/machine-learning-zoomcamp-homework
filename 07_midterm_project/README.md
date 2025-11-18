🎯 Midterm Project — Predicting Student Dropout and Academic Success
1. 🧩 Problem Description
Contexto

El abandono universitario es uno de los principales desafíos en educación superior. Predecir de manera temprana qué estudiantes tienen mayor riesgo de abandonar puede ayudar a las instituciones a tomar medidas preventivas, ofreciendo apoyo académico o financiero.

Objetivo

Desarrollar un modelo de Machine Learning capaz de predecir si un estudiante terminará graduándose, continuará matriculado o abandonará los estudios, utilizando datos académicos, demográficos y socioeconómicos.

Dataset

Fuente: UCI Machine Learning Repository – Predict Students Dropout and Academic Success

Tamaño: 4 424 registros

Features: 35 variables (edad, género, notas, becas, tipo de curso, situación económica, etc.)

Target: Target (categorías: Dropout, Enrolled, Graduate)

2. 📊 Exploratory Data Analysis (EDA)
Objetivos del EDA

Analizar la distribución de la variable objetivo (balance de clases).

Identificar correlaciones entre rendimiento académico y abandono.

Explorar el impacto de variables socioeconómicas (por ejemplo, becas, edad, empleo).

Detectar valores faltantes o atípicos.

Ejemplos de gráficos útiles

countplot del target (distribución Dropout / Enrolled / Graduate)

boxplot de notas finales vs target

heatmap de correlaciones

barplot de tasa de abandono por género o tipo de curso

3. ⚙️ Data Preparation
Posibles pasos

Limpieza de datos:

Manejar NaN o valores extremos.

Convertir variables categóricas (e.g., “gender”, “course”) a numéricas con OneHotEncoder o DictVectorizer.

Feature engineering:

Crear variables derivadas como:

Promedio de notas de primer año.

Ratio de asignaturas aprobadas/reprobadas.

Variables binarias de apoyo económico.

Normalización / estandarización:

Escalar variables numéricas si usas modelos sensibles (p. ej. regresión logística, SVM).

4. 🤖 Model Training and Evaluation
Modelos a probar

Regresión Logística Multiclase (baseline)

Random Forest Classifier

XGBoost / LightGBM

(Opcional) Support Vector Machine si los datos están bien escalados

Métricas recomendadas

Accuracy (para comparar modelos)

F1-score macro (para evitar sesgos por clases desbalanceadas)

Confusion Matrix

ROC-AUC por clase (si usas binarización)

Validación

train_test_split (70/30 o 80/20)

Validación cruzada (cross_val_score) o GridSearchCV para tuning de hiperparámetros.

5. 🧪 Model Selection and Interpretation

Escoge el mejor modelo en base a F1-macro o balanced accuracy.

Interpreta feature importances o SHAP values:

¿Qué variables influyen más en el abandono?

¿Factores financieros o académicos?

Discute las implicaciones educativas:

Cómo podría usarse este modelo en una universidad para detectar riesgo.

6. 📦 Export and Deployment
Exportar modelo

Usa joblib o pickle para guardar el modelo final (model.pkl).

Guarda también el preprocesador (dv.pkl si usas DictVectorizer).

Crear servicio web

Escribe un script predict.py o app.py con Flask o FastAPI:











Para ejecutar el Docker
docker build -t student-model .
docker run -p 8000:8000 student-model
