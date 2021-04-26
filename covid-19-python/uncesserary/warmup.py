# Arvid Anderson TE19D https://github.com/arvidanderson

import pandas as pd
import matplotlib.pyplot as plt
from get.get_DataFiles import *

df = pd.read_csv(NationalDailyDeaths, delimiter=',')
Dates = list(df['Date'])
DailyDeaths = list(df['National_Daily_Deaths'])

plt.plot(Dates, DailyDeaths, color='red', marker='o')
plt.title('People dead per day in Covid-19 (Sweden)', fontsize=14)
plt.xlabel('Day', fontsize=15)
plt.ylabel('Deaths', fontsize=15)
plt.grid(True)
plt.show()