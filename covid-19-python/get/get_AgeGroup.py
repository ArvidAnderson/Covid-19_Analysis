#Imports
import pandas as pd
from get_DataFiles import *

#Read file, uses data_files
df = pd.read_csv(NationalTotalDeathsByAgeGroup, delimiter=',')

#Function to search date to get deaths on that specefic date
def TotalCasesByAgeGroup(age_span):
    day = df[df['Age_Group'] == age_span]
    return (day.values[0][1])

def TotalICUByAgeGroup(age_span):
    day = df[df['Age_Group'] == age_span]
    return (day.values[0][2])

def TotalDeathsByAgeGroup(age_span):
    day = df[df['Age_Group'] == age_span]
    return (day.values[0][3])

print(TotalCasesByAgeGroup('10-19'))