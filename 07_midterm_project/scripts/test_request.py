import requests

url = "http://127.0.0.1:8000/predict"

# Students to evaluate


record_1 = {'marital_status': 'single',
  'application_mode': '1st_phase_general_contingent',
  'application_order': 5,
  'course': 'communication_design',
  'daytime_evening_attendance': 'daytime',
  'previous_qualification': 'secondary_education',
  'previous_qualification_grade': 122.0,
  'nacionality': 'portuguese',
  'mother_s_qualification': 'basic_education_1st_cycle_4th_5th_year_or_equiv',
  'father_s_qualification': 'basic_education_1st_cycle_4th_5th_year_or_equiv',
  'mother_s_occupation': 'unskilled_workers',
  'father_s_occupation': 'unskilled_workers',
  'admission_grade': 124.8,
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
  'curricular_units_1st_sem_evaluations': 0,
  'curricular_units_1st_sem_approved': 0,
  'curricular_units_1st_sem_grade': 0.0,
  'curricular_units_1st_sem_without_evaluations': 0,
  'curricular_units_2nd_sem_credited': 0,
  'curricular_units_2nd_sem_enrolled': 6,
  'curricular_units_2nd_sem_evaluations': 0,
  'curricular_units_2nd_sem_approved': 0,
  'curricular_units_2nd_sem_grade': 0.0,
  'curricular_units_2nd_sem_without_evaluations': 0,
  'unemployment_rate': 10.8,
  'inflation_rate': 1.4,
  'gdp': 1.74}
#   'target' = 1


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

# print("STATUS 1:", r.status_code)
# print("TEXT 1:", repr(r.text)) 

if r.headers.get("content-type", "").startswith("application/json"):
    response_1 = r.json()
    print('response student 1, expected prediction=1', response_1)
else:
    print("Response 1 is not JSON")

r2 = requests.post(url, json=record_2)

# print("STATUS 2:", r2.status_code)
# print("TEXT 2:", repr(r2.text))

if r2.headers.get("content-type", "").startswith("application/json"):
    response_2 = r2.json()
    print('response student 2, expected prediction=0', response_2)
else:
    print("Response 2 is not JSON")