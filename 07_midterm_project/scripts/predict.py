import pickle

# Load Pipeline
with open('xboost_model.bin', 'rb') as f:
    model = pickle.load(f)



# Calcular probabilidad de conversión
proba = model.predict_proba([record])[0, 1]

print(f"Probability of dropout: {proba:.3f}")

def predict_drop(alumn, dv, model):
    X = dv.transform([alumn])
    y_pred = model.predict(X)
    return y_pred[0]


with open('xboost_model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)




# Registro a evaluar
record = {'marital_status': 'single',
  'application_mode': '2nd_phase_general_contingent',
  'application_order': 5,
  'course': 'animation_and_multimedia_design',
  'daytime_evening_attendance': 'daytime',
  'previous_qualification': 'secondary_education',
  'previous_qualification_grade': 122.0,
  'nacionality': 'portuguese',
  'mother_s_qualification': 'basic_education_3rd_cycle_9th_10th_11th_year_or_equiv',
  'father_s_qualification': 'other_11th_year_of_schooling',
  'mother_s_occupation': 'personal_services_security_and_safety_workers_and_sellers',
  'father_s_occupation': 'unskilled_workers',
  'admission_grade': 127.3,
  'displaced': 'yes',
  'educational_special_needs': 'no',
  'debtor': 'no',
  'tuition_fees_up_to_date': 'yes',
  'gender': 'male',
  'scholarship_holder': 'no',
  'age_at_enrollment': 20,
  'international': 'no',
  'curricular_units_1st_sem_credited': 0,
  'curricular_units_1st_sem_enrolled': 0,
  'curricular_units_1st_sem_evaluations': 0,
  'curricular_units_1st_sem_approved': 0,
  'curricular_units_1st_sem_grade': 0.0,
  'curricular_units_1st_sem_without_evaluations': 0,
  'curricular_units_2nd_sem_credited': 0,
  'curricular_units_2nd_sem_enrolled': 0,
  'curricular_units_2nd_sem_evaluations': 0,
  'curricular_units_2nd_sem_approved': 0,
  'curricular_units_2nd_sem_grade': 0.0,
  'curricular_units_2nd_sem_without_evaluations': 0,
  'unemployment_rate': 10.8,
  'inflation_rate': 1.4,
  'gdp': 1.74,
  'target': 1}