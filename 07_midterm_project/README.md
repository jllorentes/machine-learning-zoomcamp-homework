# 🎯 Midterm Project — Predicting Student Dropout and Academic Success

## 1. 🧩 Problem Description

### Context

University dropout is one of the main challenges in higher education. Being able to predict early on which students are at higher risk of dropping out can help institutions take preventive actions by offering academic or financial support.

### Objective

Develop a Machine Learning model capable of predicting whether a student will eventually graduate or drop out, using academic, demographic, and socioeconomic data.

### Dataset

- **Source:** UCI Machine Learning Repository – Predict Students Dropout and Academic Success  
- **Size:** 4,424 records  
- **Features:** 35 variables (age, gender, grades, scholarships, type of course, economic situation, etc.)  
- **Target:** `Target` (categories: Dropout, Enrolled, Graduate). It will be simplfied to Dropout or not Dropout

---

## 2. 📊 Exploratory Data Analysis (EDA)

### EDA goals

- Analyze the distribution of the target variable (class balance).  
- Identify correlations between numerical features and dropout.  
- Explore the impact of socioeconomic variables (e.g., scholarships, age, employment).  
- Detect missing or outlier values.  

## 3. ⚙️ Data Preparation

#### Data cleaning

- Handle NaNs.  
- Convert categorical variables (e.g., `gender`, `course`) to numeric using `OneHotEncoder` or `DictVectorizer`.  

## 4. 🤖 Model Training and Evaluation

### Models to try

- Logistic Regression
- Random Forest Classifier  
- XGBoost 

### Metrics

- ROC-AUC

### Validation

- `train_validation_test_split` (60/20/20)  

---

## 5. 📦 Export and Deployment

### Export the model

- Using `pickle` to save the final model.  
- Save the preprocessor.  

### Create a web service

- `app.py` script using FastAPI.  

### Run the Endpoint with Docker

```bash
docker build -t student-model .
docker run -p 8000:8000 student-model