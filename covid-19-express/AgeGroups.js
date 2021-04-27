import csv from 'csv-parser'
import fs from 'fs'
const result = []

fs.createReadStream('./kaggle_data/National_Total_Deaths_by_Age_Group.csv')
    .pipe(csv({}))
    .on('data', (data) => result.push(data))
    .on('end', () => {
        var SelectedAge =  result.filter(x => x.Age_Group === '10-19');
        console.log(SelectedAge[0]['Total_Cases']);
    })
