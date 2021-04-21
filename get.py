#Imports
import pandas as pd
from datafiles import *

#Read file, uses data_files
dfAge = pd.read_csv(NationalTotalDeathsByAgeGroup, delimiter=',')

#Function to search date to get deaths on that specefic date
def TotalCasesByAgeGroup(age_span):
    age = dfAge[dfAge['Age_Group'] == age_span]
    return (age.values[0][1])

def TotalICUByAgeGroup(age_span):
    age = dfAge[dfAge['Age_Group'] == age_span]
    return (age.values[0][2])

def TotalDeathsByAgeGroup(age_span):
    age = dfAge[dfAge['Age_Group'] == age_span]
    return (age.values[0][3])