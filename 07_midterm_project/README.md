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
As I dont like really much the Github codespace, I created a container to run jupyter notebooks locally, managing all the dependencies.
You can find the docker-compose in the root folder of the repository. Just running that container, you will have all the dependencies isntalled to run the notebook without isntalling anything inside the notebook. 

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

### Web service

- `app.py` script using FastAPI.  

### Create the model from a script
To avoid installing all the dependencies, and managing venvs, I created a container to run the script to generate the model
As I did this in a computer w/o docker and with Podman installed (an open source and free container management tool), the isntructions to run and create the model (the docker ones should be the same):

From the folder 07_midterm_project:
```bash
podman compose -f docker-compose.train.yml up --build
```
as an output the data would be downloaded and the model created in the folder model/

PS. if you clone the repo, you would have the folder script created, otherwise you should create it and putting there the train.py file.

### Run the Endpoint with Docker
As I said, I finished earlier in a different computer with Docker installed the deployment of the model in a container, so once cloned the repo, go to the 07_midterm_project and run the Dockerfile

```bash
docker build -t student-model .
docker run -p 8000:8000 student-model
```