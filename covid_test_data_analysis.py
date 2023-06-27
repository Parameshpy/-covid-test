#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action='ignore')


# In[4]:


df = pd.read_csv(r'C:\Users\703310783\OneDrive - Genpact\Documents\DE - Course\states_current.csv')


# In[5]:


df.head()


# In[6]:


df.describe()


# In[7]:


df.dtypes


# In[8]:


duplicate_rows = df[df.duplicated()]
duplicate_rows


# In[9]:


df.isnull().sum()


# In[10]:


df.shape


# In[11]:


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


# In[21]:


df.columns


# In[16]:


df.isnull().sum()


# In[51]:


df_impute_mean = df.fillna(df.mean())
df_impute_mean.head()


# In[50]:


sns.barplot(x = 'state', y = 'totalTestResults', data = df)
plt.xlabel('state')
plt.ylabel('totalTestResults')
plt.title('Barplot')
plt.show()


# In[55]:


sns.barplot(x = 'totalTestResultsSource', y = 'totalTestResults', data = df)


# In[ ]:





# In[ ]:




