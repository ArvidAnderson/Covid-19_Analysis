import express from 'express';
import cors from 'cors'
import csv from 'csv-parser'
import fs from 'fs'

const app = express();
app.use(cors())
const port = 3000;
const AgeGroups = []

//Read AgeGroups csv
fs.createReadStream('./kaggle_data/National_Total_Deaths_by_Age_Group.csv')
    .pipe(csv({}))
    .on('data', (data) => AgeGroups.push(data))

app.get('/', (req, res) => {
    return res.send('Kazung Visualizer API');
});

//Return all agegroups
app.get('/age', (req, res) => {
    return res.send(AgeGroups);
});

//Return Specefic Agegroup
app.get('/age/:agegroup', (req, res) => {
    if (AgeGroups.filter(x => x.Age_Group === req.params.agegroup) != '') {
        return res.send(AgeGroups.filter(x => x.Age_Group === req.params.agegroup))
    } else {
        return res.send('Age group not found')
    }
});

app.listen(port, () => console.log(`Kazung Visualizer listening on port ${port}!`))