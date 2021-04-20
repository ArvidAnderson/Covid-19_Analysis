#Imports
import pandas as pd
from get_DataFiles import *

#Read file, uses data_files
df = pd.read_csv(NationalDailyDeaths, delimiter=',')

#Function to search date to get deaths on that specefic date
def get_DeathByDate(date_input):
    day = df[df['Date'] == date_input]
    return (day.values[0][1])

Example
#print(get_DeathByDate('2020-03-20'))
