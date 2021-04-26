#Imports
import pandas as pd
import plotly.express as px
import json
from datafiles import *

################################################################

#NationalTotalDeathsByAgeGroup Functions and Graphs

#File

dfAge = pd.read_csv(NationalTotalDeathsByAgeGroup, delimiter=',')

# Functions

def TotalCasesByAgeGroup(age_span):
    age = dfAge[dfAge['Age_Group'] == age_span]
    return (age.values[0][1])

def TotalICUByAgeGroup(age_span):
    age = dfAge[dfAge['Age_Group'] == age_span]
    return (age.values[0][2])

def TotalDeathsByAgeGroup(age_span):
    age = dfAge[dfAge['Age_Group'] == age_span]
    return (age.values[0][3])

#Graphs

#Total Cases Fig
AgeTotalCasesFig = px.bar(dfAge, x='Age_Group', y='Total_Cases',
      labels={'Age_Group': 'Age Group', 'Total_Cases': 'Total Cases'})
#Total ICU Fig
AgeTotalICUFig = px.bar(dfAge, x='Age_Group', y='Total_ICU_Admissions',
      labels={'Age_Group': 'Age Group', 'Total_ICU_Admissions': 'Total ICU Admissions'})

#Total Deaths FIG
AgeTotalDeathsFig = px.bar(dfAge, x='Age_Group', y='Total_Deaths',
      labels={'Age_Group': 'Age Group', 'Total_Deaths': 'Total Deaths'})

################################################################

#RegionalTotalsData - geojson choroleth map map overview

SwedishCounties = json.load(open('swedish_counties.geojson', 'r', encoding='utf-8'))

SwedishCountiesMap = {}
for feature in SwedishCounties['features']:
    feature['id'] = feature['properties']['cartodb_id']
    SwedishCountiesMap[feature['properties']['name']] = feature['id']

dfChMap = pd.read_csv(RegionalTotalsData)
dfChMap['id'] = dfChMap['Region'].apply(lambda x: SwedishCountiesMap[x])

RegionalMapFig = px.choropleth(dfChMap, locations='id', hover_name='Region', scope='europe', hover_data=['Total_ICU_Admissions', 'Cases_per_100k_Pop', 'Total_Deaths'], geojson=SwedishCounties,
                        color='Total_Cases', labels={
                         'Total_Cases': 'Total Cases', 'id': 'Identifier ID',
                          'Total_ICU_Admissions': 'Total ICU Admissions', 'Total_Deaths': 'Total Deaths', 'Cases_per_100k_Pop': 'Cases per 100k pop'
                        })
RegionalMapFig.update_geos(fitbounds='locations', visible=False)

################################################################