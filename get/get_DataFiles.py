# Arvid Anderson TE19D, https://github.com/arvidanderson

#Function to easily grab files from ./kaggle_data
def getFile(data_file):
    return './kaggle_data/{}.csv'.format(data_file)

#Making variables for every file, using function getFile, faster to use function in case of changes
GenderData = getFile('Gender_Data')
MunicipalityWeeklyData = getFile('Municipality_Weekly_Data')
NationalDailyDeaths = getFile('National_Daily_Deaths')
NationalDailyICUAdmissions = getFile('National_Daily_ICU_Admissions')
NationalTotalDeathsByAgeGroup = getFile('National_Total_Deaths_by_Age_Group')
RegionalDailyCases = getFile('Regional_Daily_Cases')
RegionalTotalsData = getFile('Regional_Totals_Data')
SwedenRawData = './kaggle_data/Sweden_raw_data.xls' # Exception function not handeling xls