import requests

url = "http://127.0.0.1:8000/predict"

# Registro a evaluar
record_1 = {'marital_status': 'single',
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
  'gdp': 1.74}
# target = 1

record_2 = {'marital_status': 'single',
  'application_mode': 'international_student_bachelor',
  'application_order': 1,
  'course': 'tourism',
  'daytime_evening_attendance': 'daytime',
  'previous_qualification': 'secondary_education',
  'previous_qualification_grade': 160.0,
  'nacionality': 'portuguese',
  'mother_s_qualification': 'secondary_education_12th_year_of_schooling_or_eq',
  'father_s_qualification': 'higher_education_degree',
  'mother_s_occupation': 'intermediate_level_technicians_and_professions',
  'father_s_occupation': 'intermediate_level_technicians_and_professions',
  'admission_grade': 142.5,
  'displaced': 'yes',
  'educational_special_needs': 'no',
  'debtor': 'no',
  'tuition_fees_up_to_date': 'no',
  'gender': 'male',
  'scholarship_holder': 'no',
  'age_at_enrollment': 19,
  'international': 'no',
  'curricular_units_1st_sem_credited': 0,
  'curricular_units_1st_sem_enrolled': 6,
  'curricular_units_1st_sem_evaluations': 6,
  'curricular_units_1st_sem_approved': 6,
  'curricular_units_1st_sem_grade': 14.0,
  'curricular_units_1st_sem_without_evaluations': 0,
  'curricular_units_2nd_sem_credited': 0,
  'curricular_units_2nd_sem_enrolled': 6,
  'curricular_units_2nd_sem_evaluations': 6,
  'curricular_units_2nd_sem_approved': 6,
  'curricular_units_2nd_sem_grade': 13.666666666666666,
  'curricular_units_2nd_sem_without_evaluations': 0,
  'unemployment_rate': 13.9,
  'inflation_rate': -0.3,
  'gdp': 0.79}
  # 'target': 0

r = requests.post(url, json=record_1)
print("STATUS:", r.status_code)
print("TEXT:", r.text)

response_1 = r.json()
print(response_1)

response_2 = requests.post(url, json=record_2).json()
print(response_2)