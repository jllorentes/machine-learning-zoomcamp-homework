# ============================================================
# 1. IMPORTS
# ============================================================

import pandas as pd
import numpy as np

import re
from unidecode import unidecode

import os
import wget
import zipfile

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
import xgboost as xgb
from tqdm.auto import tqdm
import pickle

# ============================================================
# 2. DOWNLOAD DATA
# ============================================================

url = "https://archive.ics.uci.edu/static/public/697/predict+students+dropout+and+academic+success.zip"
folder = "07_midterm_project/data/"

# Carpeta de datos relativa al directorio donde se ejecuta el script (raíz del proyecto en el contenedor)
folder = "data"
os.makedirs(folder, exist_ok=True)

file = os.path.join(folder, "predict+students+dropout+and+academic+success.zip")

# Crear la carpeta si no existe (opcional)
# os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

if os.path.exists(file):
    print("File already downloaded.")
else:
    try:
        print("Downloading file...")
        wget.download(url, file)
        print("Download done.")
    except:
        print("Error downloading file.")

# ============================================================
# 3. UNZIP DATA
# ============================================================

folder_destiny = 'data'
file_destiny = os.path.join(folder_destiny, "data.csv")

if os.path.exists(file_destiny):
    print("File already unzipped.")
else:
    try:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(folder_destiny)

        print(f"File unzip in: {folder_destiny}")
    except:
        print("Error unzipping.")

# ============================================================
# 4. LOAD DATA
# ============================================================

file = 'data/data.csv'

df = pd.read_csv(file, delimiter=';')

# Preview
print("Shape:", df.shape)
df.head()

# ============================================================
# 3. INITIAL CLEANING
# ============================================================
def to_snake_case(name):
    # Special characters
    name = unidecode(name)
    # Lowercase
    name = name.lower()
    # Replace non alphanumeric by _
    name = re.sub(r'[^a-z0-9]+', '_', name)
    # Delete initial and ending _
    name = name.strip('_')
    return name

def standardize_columns(df):
    df = df.copy()
    df.columns = [to_snake_case(col) for col in df.columns]
    return df

df = standardize_columns(df)

# Mapping values (from the dataset page: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)
marital_status = {
    1: 'single',
    2: 'married',
    3: 'widower',
    4: 'divorced',
    5: 'facto_union',
    6: 'legally_separated'
}
for values in marital_status:
    marital_status[values] = to_snake_case(marital_status[values])

application_mode = {
    1: '1st_phase_general_contingent',
    2: 'Ordinance No. 612/93',
    5: '1st_phase_special_contingent_azores',
    7: 'holders_of_other_higher_courses',
    10: 'international_student',
    15: 'International student (bachelor)',
    16: '1st_phase_special_contingent_madeira',
    17: '2nd_phase_general_contingent',
    18: '3rd_phase_general_contingent',
    26: 'different_plan',
    27: 'other_institution',
    39: 'over_23_years_old',
    42: 'transfer',
    43: 'change_of_course',
    44: 'technological_specialization_diploma_holders ',
    51: 'change_of_institution_course',
    53: 'short_cycle_diploma_holders',
    57: 'change_of_institution_course_international'
}
for values in application_mode:
    application_mode[values] = to_snake_case(application_mode[values])

course = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene ',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance'
}
for values in course:
    course[values] = to_snake_case(course[values])

daytime_evening_attendance = {
    1: 'daytime',
    0: 'evening'
}
for values in daytime_evening_attendance:
    daytime_evening_attendance[values] = to_snake_case(daytime_evening_attendance[values])


previous_qualification = {
    1: 'Secondary education',
    2: 'Higher education - bachelors degree',
    3: 'Higher education - degree',
    4: 'Higher education - masters' ,
    5: 'Higher education - doctorate',
    6: 'Frequency of higher education ',
    9: '12th year of schooling - not completed ',
    10: '11th year of schooling - not completed ',
    12: 'Other - 11th year of schooling ',
    14: '10th year of schooling ',
    15: '10th year of schooling - not completed ',
    19: 'Basic education 3rd cycle (9th/10th/11th year) or equiv. ',
    38: 'Basic education 2nd cycle (6th/7th/8th year) or equiv. ',
    39: 'Technological specialization course ',
    40: 'Higher education - degree (1st cycle) ',
    42: 'Professional higher technical course ',
    43: 'Higher education - master (2nd cycle)'
}
for values in previous_qualification:
    previous_qualification[values] = to_snake_case(previous_qualification[values])

nacionality = {
    1: 'Portuguese',
    2: 'German',
    6: 'Spanish',
    11: 'Italian', 
    13: 'Dutch', 
    14: 'English', 
    17: 'Lithuanian',
    21: 'Angolan', 
    22: 'Cape Verdean', 
    24: 'Guinean', 
    25: 'Mozambican', 
    26: 'Santomean', 
    32: 'Turkish', 
    41: 'Brazilian', 
    62: 'Romanian', 
    100: 'Moldova (Republic of)', 
    101: 'Mexican', 
    103: 'Ukrainian', 
    105: 'Russian', 
    108: 'Cuban', 
    109: 'Colombian'
}
for values in nacionality:
    nacionality[values] = to_snake_case(nacionality[values])

mother_s_qualification = {
    1: 'Secondary Education 12th Year of Schooling or Eq. ',
    2: 'Higher Education Bachelors Degree ',
    3: 'Higher Education Degree ',
    4: 'Higher Education Masters ',
    5: 'Higher Education Doctorate ',
    6: 'Frequency of Higher Education ',
    9: '12th Year of Schooling Not Completed ',
    10: '11th Year of Schooling Not Completed ',
    11: '7th Year (Old) ',
    12: 'Other 11th Year of Schooling ',
    14: '10th Year of Schooling ',
    18: 'General commerce course ',
    19: 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. ',
    22: 'Technical-professional course ',
    26: '7th year of schooling ',
    27: '2nd cycle of the general high school course ',
    29: '9th Year of Schooling Not Completed ',
    30: '8th year of schooling ',
    34: 'Unknown ',
    35: 'Cant read or write ',
    36: 'Can read without having a 4th year of schooling ',
    37: 'Basic education 1st cycle (4th/5th year) or equiv. ',
    38: 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. ',
    39: 'Technological specialization course ',
    40: 'Higher education degree (1st cycle) ',
    41: 'Specialized higher studies course ',
    42: 'Professional higher technical course ',
    43: 'Higher Education Master (2nd cycle) ',
    44: 'Higher Education Doctorate (3rd cycle)'
}
for values in mother_s_qualification:
    mother_s_qualification[values] = to_snake_case(mother_s_qualification[values])

father_s_qualification = {
    1: 'Secondary Education 12th Year of Schooling or Eq. ',
    2: 'Higher Education Bachelors Degree ',
    3: 'Higher Education Degree ',
    4: 'Higher Education Masters ',
    5: 'Higher Education Doctorate ',
    6: 'Frequency of Higher Education ',
    9: '12th Year of Schooling Not Completed ',
    10: '11th Year of Schooling Not Completed ',
    11: '7th Year (Old) ',
    12: 'Other 11th Year of Schooling ',
    13: '2nd year complementary high school course ',
    14: '10th Year of Schooling ',
    18: 'General commerce course ',
    19: 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. ',
    20: 'Complementary High School Course ',
    22: 'Technical-professional course ',
    25: 'Complementary High School Course not concluded ',
    26: '7th year of schooling ',
    27: '2nd cycle of the general high school course ',
    29: '9th Year of Schooling Not Completed ',
    30: '8th year of schooling ',
    31: 'General Course of Administration and Commerce ',
    33: 'Supplementary Accounting and Administration ',
    34: 'Unknown ',
    35: 'Cant read or write ',
    36: 'Can read without having a 4th year of schooling ',
    37: 'Basic education 1st cycle (4th/5th year) or equiv. ',
    38: 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. ',
    39: 'Technological specialization course ',
    40: 'Higher education degree (1st cycle) ',
    41: 'Specialized higher studies course ',
    42: 'Professional higher technical course ',
    43: 'Higher Education Master (2nd cycle) ',
    44: 'Higher Education Doctorate (3rd cycle)',
}
for values in father_s_qualification:
    father_s_qualification[values] = to_snake_case(father_s_qualification[values])

mother_s_occupation = {
    0: 'Student ',
    1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers ',
    2: 'Specialists in Intellectual and Scientific Activities ',
    3: 'Intermediate Level Technicians and Professions ',
    4: 'Administrative staff ',
    5: 'Personal Services, Security and Safety Workers and Sellers ',
    6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry ',
    7: 'Skilled Workers in Industry, Construction and Craftsmen ',
    8: 'Installation and Machine Operators and Assembly Workers ',
    9: 'Unskilled Workers ',
    10: 'Armed Forces Professions ',
    90: 'Other Situation ',
    99: '(blank) ',
    122: 'Health professionals ',
    123: 'teachers ',
    125: 'Specialists in information and communication technologies (ICT) ',
    131: 'Intermediate level science and engineering technicians and professions ',
    132: 'Technicians and professionals, of intermediate level of health ',
    134: 'Intermediate level technicians from legal, social, sports, cultural and similar services ',
    141: 'Office workers, secretaries in general and data processing operators ',
    143: 'Data, accounting, statistical, financial services and registry-related operators ',
    144: 'Other administrative support staff ',
    151: 'personal service workers ',
    152: 'sellers ',
    153: 'Personal care workers and the like ',
    171: 'Skilled construction workers and the like, except electricians ',
    173: 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like ',
    175: 'Workers in food processing, woodworking, clothing and other industries and crafts ',
    191: 'cleaning workers ',
    192: 'Unskilled workers in agriculture, animal production, fisheries and forestry ',
    193: 'Unskilled workers in extractive industry, construction, manufacturing and transport ',
    194: 'Meal preparation assistants'
}
for values in mother_s_occupation:
    mother_s_occupation[values] = to_snake_case(mother_s_occupation[values])

father_s_occupation = {
    0: 'Student ',
    1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers ',
    2: 'Specialists in Intellectual and Scientific Activities ',
    3: 'Intermediate Level Technicians and Professions ',
    4: 'Administrative staff ',
    5: 'Personal Services, Security and Safety Workers and Sellers ',
    6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry ',
    7: 'Skilled Workers in Industry, Construction and Craftsmen ',
    8: 'Installation and Machine Operators and Assembly Workers ',
    9: 'Unskilled Workers ',
    10: 'Armed Forces Professions ',
    90: 'Other Situation ',
    99: '(blank) ',
    101: 'Armed Forces Officers ',
    102: 'Armed Forces Sergeants ',
    103: 'Other Armed Forces personnel ',
    112: 'Directors of administrative and commercial services ',
    114: 'Hotel, catering, trade and other services directors ',
    121: 'Specialists in the physical sciences, mathematics, engineering and related techniques ',
    122: 'Health professionals ',
    123: 'teachers ',
    124: 'Specialists in finance, accounting, administrative organization, public and commercial relations ',
    131: 'Intermediate level science and engineering technicians and professions ',
    132: 'Technicians and professionals, of intermediate level of health ',
    134: 'Intermediate level technicians from legal, social, sports, cultural and similar services ',
    135: 'Information and communication technology technicians ',
    141: 'Office workers, secretaries in general and data processing operators ',
    143: 'Data, accounting, statistical, financial services and registry-related operators ',
    144: 'Other administrative support staff ',
    151: 'personal service workers ',
    152: 'sellers ',
    153: 'Personal care workers and the like ',
    154: 'Protection and security services personnel ',
    161: 'Market-oriented farmers and skilled agricultural and animal production workers ',
    163: 'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence ',
    171: 'Skilled construction workers and the like, except electricians ',
    172: 'Skilled workers in metallurgy, metalworking and similar ',
    174: 'Skilled workers in electricity and electronics ',
    175: 'Workers in food processing, woodworking, clothing and other industries and crafts ',
    181: 'Fixed plant and machine operators ',
    182: 'assembly workers ',
    183: 'Vehicle drivers and mobile equipment operators ',
    192: 'Unskilled workers in agriculture, animal production, fisheries and forestry ',
    193: 'Unskilled workers in extractive industry, construction, manufacturing and transport ',
    194: 'Meal preparation assistants ',
    195: 'Street vendors (except food) and street service providers'
}
for values in father_s_occupation:
    father_s_occupation[values] = to_snake_case(father_s_occupation[values])

yes_no = {
    1: 'yes',
    0: 'no'
}

gender = {
    1: 'male',
    0: 'female'
}

df.marital_status = df.marital_status.map(marital_status)
df.application_mode = df.application_mode.map(application_mode)
df.course = df.course.map(course)
df.daytime_evening_attendance = df.daytime_evening_attendance.map(daytime_evening_attendance)
df.previous_qualification = df.previous_qualification.map(previous_qualification)
df.nacionality = df.nacionality.map(nacionality)
df.mother_s_qualification = df.mother_s_qualification.map(mother_s_qualification)
df.father_s_qualification = df.father_s_qualification.map(father_s_qualification)
df.mother_s_occupation = df.mother_s_occupation.map(mother_s_occupation)
df.father_s_occupation = df.father_s_occupation.map(father_s_occupation)

df.displaced = df.displaced.map(yes_no)
df.educational_special_needs = df.educational_special_needs.map(yes_no)
df.debtor = df.debtor.map(yes_no)
df.tuition_fees_up_to_date = df.tuition_fees_up_to_date.map(yes_no)
df.scholarship_holder = df.scholarship_holder.map(yes_no)
df.international = df.international.map(yes_no)
df.gender = df.gender.map(gender)

# Making target Binary
df.target = (df.target == 'Dropout').astype(int)

numerical_final = ['curricular_units_2nd_sem_approved', 'curricular_units_2nd_sem_grade', 'age_at_enrollment']

categorical_final = [
    'application_mode',
    'course',
    'previous_qualification',
    'mother_s_occupation',
    'tuition_fees_up_to_date',
    'scholarship_holder',
    'debtor',
    'gender',
]

# Splitting data (60/20/20)
ramdom_state = 1

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=ramdom_state)


df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.target.values
y_test = df_test.target.values

del df_test['target']
del df_full_train['target']

df_full_train = df_full_train[categorical_final + numerical_final]
df_test = df_test[categorical_final + numerical_final]

# ## Training the final model (XBoost)
dicts_full_train = df_full_train.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_full_train)

dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)

feature_names = dv.get_feature_names_out().tolist() 

dfulltrain = xgb.DMatrix(
    X_full_train,
    label=y_full_train,
    feature_names=feature_names
)

# XBoost

eta = 0.2
max_depth = 4
min_child_weight = 20
iterations = 30

xgb_params = {
    'eta': eta, 
    'max_depth': max_depth,
    'min_child_weight': min_child_weight,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

final_xgboost_model = xgb.train(xgb_params, dfulltrain, num_boost_round=iterations)

model_folder = "model"
os.makedirs(model_folder, exist_ok=True)
output_file = os.path.join(model_folder, "xboost_model.bin")

with open(output_file, 'wb') as f_out: # 'wb' means write-binary
    pickle.dump((dv, final_xgboost_model), f_out)

print('Model created')