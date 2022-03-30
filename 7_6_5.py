
import pandas as pd
import numpy as np
import os

df_schools = pd.read_csv('schools.csv')

print(df_schools)

print(df_schools.dtypes)

df_schools.rename({'NOR':'total_pupils', 'PNORG':'percent_girls', 'PNORB':'percent_boys',
                  'School_Phase': 'school_type', 'GFTE':'salary_teacher', 'Total_Teachers':'total_teachers',
                  'Total_Teaching_Assistants ':'total_teachassist', 'School_0ort':'school_support',
                  'Full_Time_Teachers':'fulltime_teachers', 'Pupil_Teacher_Ratio':'student:teacher',
                  'GPS_AVERAGE':'grammar_score', 'MAT_AVERAGE':'maths_score',
                  'READ_AVERAGE':'read_score'}, axis=1, inplace=True)

for col in df_schools.columns:
   print(col)

print(df_schools.describe(include='all'))

print(df_schools.isna().sum())
df_schools.info()

schools = df_schools.dropna()
print(schools)

print(schools.isna().sum())
# 1
print(schools.duplicated())

# 2
print(schools.duplicated().sum())

# Table 1
schools_1 = schools[['school_type', 'total_pupils', 'percent_girls', 'percent_boys']][::]

print(schools_1)

# Table 2
schools_2 = schools[['school_type', 'salary_teacher', 'total_teachers', 'total_teachassist',
                    'school_support', 'student:teacher', 'fulltime_teachers']][::]

print(schools_2)

# Table 3
schools_3 = schools[['school_type', 'grammar_score', 'maths_score', 'read_score']][::]

print(schools_3)

# Table 1
schools_1['school_type'].replace('Primary', '1', inplace=True)
schools_1['school_type'].replace('Secondary', '2', inplace=True)
schools_1['school_type'].replace('All through', '3', inplace=True)
schools_1['school_type'].replace('Middle deemed primary', '4', inplace=True)
schools_1['school_type'].replace('Middle deemed secondary', '5', inplace=True)

print(schools_1)


