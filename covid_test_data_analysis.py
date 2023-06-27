#!/usr/bin/env python
# coding: utf-8

# Import Packages


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action='ignore')


# Read file


df = pd.read_csv(r'C:\Users\703310783\OneDrive - Genpact\Documents\DE - Course\states_current.csv')


# Read head files:


df.head()


# Descrribe the dataset:


df.describe()


# Describe the datatypes:


df.dtypes


# Remove duplicates:


duplicate_rows = df[df.duplicated()]
duplicate_rows


# Analyse null values:


df.isnull().sum()


# shape of the dataset:


df.shape


# Remove empty columns:


columns_to_remove = ['pending', 'inIcuCumulative','grade','dataQualityGrade','positiveTestsViral',
'negativeTestsViral',
'positiveCasesViral',
'deathConfirmed',
'deathProbable',
'totalTestEncountersViral',
'totalTestsPeopleViral',
'totalTestsAntibody',
'positiveTestsAntibody',
'negativeTestsAntibody',
'totalTestsPeopleAntibody',
'positiveTestsPeopleAntibody',
'negativeTestsPeopleAntibody',
'totalTestsPeopleAntigen',
'positiveTestsPeopleAntigen',
'totalTestsAntigen',
'positiveTestsAntigen'
]
df = df.drop(columns_to_remove, axis=1)


# View list of columns:


df.columns


# Fill the values


df_impute_mean = df.fillna(df.mean())
df_impute_mean.head()


# View total results by states:


sns.barplot(x = 'state', y = 'totalTestResults', data = df)
plt.xlabel('state')
plt.ylabel('totalTestResults')
plt.title('Barplot')
plt.show()


# View totalTestResults by totalTestResultsSource :


sns.barplot(x = 'totalTestResultsSource', y = 'totalTestResults', data = df)




