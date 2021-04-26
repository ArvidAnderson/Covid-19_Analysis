#Imports
import pandas as pd
from get_DataFiles import *

#Read file, uses data_files
df = pd.read_csv(GenderData, delimiter=',')

#Get information about all males
def get_Male_TotalCases():
    return df['Total_Cases'][0]

def get_Male_TotalICU():
    return df['Total_ICU_Admissions'][0]

def get_Male_TotalDeaths():
    return df['Total_Deaths'][0]

#Get information about all females
def get_Female_TotalCases():
    return df['Total_Cases'][1]

def get_Female_TotalICU():
    return df['Total_ICU_Admissions'][1]

def get_Female_TotalDeaths():
    return df['Total_Deaths'][1]