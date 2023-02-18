#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd 
import numpy as np


# In[15]:


#Tried running the df but it ran into error cos it wasnt saved as utf-8
df = pd.read_csv(r'/Users/mohamedsalah/Downloads/Minimum Wage Data.csv', encoding ='latin')

# here we saved the data to utf-8
df.to_csv(r'/Users/mohamedsalah/Downloads/Minimum Wage Data.csv', encoding ='UTF-8')

df.head()


# In[16]:


# create groups by unique column values. Groping state of Alabama by year. 

gb = df.groupby("State")

gb.get_group("Alabama").set_index("Year").head()


# In[25]:


# Aside from grouping year by state, we are also iterating over the groups:


act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name}))
act_min_wage.head()


# In[29]:


act_min_wage.describe().head()


# In[31]:


#Another one that we can do is .corr() or .cov() to get correlation and covariance respectively
act_min_wage.corr().head()


# In[43]:


#Covariance

act_min_wage.cov().head()


# In[32]:


df.head()


# In[34]:


issue_df = df[df['Department.Of.Labor.Cleaned.Low.Value.2020.Dollars']==0]

issue_df.head()


# In[41]:


# grab the uniques from the state column

issue_df['State'].unique()


# In[44]:


# cleaning the data and replacing all the 0 to np 
# axis 1 is for columns, axis 0 (default) is for rows
# this way we only have state with actual minimum wage and not 0
act_min_wage.replace(0, np.NaN).dropna(axis=1).corr().head()


# In[46]:


# check for mistakes

min_wage_corr =act_min_wage.replace(0, np.NaN).dropna(axis=1).corr().head()
for problem in issue_df['State'].unique():
    if problem in min_wage_corr.columns:
        print("Missing something here....")


# In[47]:


grouped_issues = issue_df.groupby("State")

grouped_issues.get_group("Alabama").head(3)


# In[52]:


# creating viz for minimun waga correlation or covariance respectively

df = pd.read_csv(r'/Users/mohamedsalah/Downloads/Minimum Wage Data.csv')

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name}))

act_min_wage.head()

min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

min_wage_corr.head()


# In[53]:


# creating correlation

import matplotlib.pyplot as plt

plt.matshow(min_wage_corr)
plt.show()


# In[55]:


# Customization
labels = [c[:2] for c in min_wage_corr.columns]  # get abbv state names.

fig = plt.figure(figsize=(12,12))  # figure so we can add axis
ax = fig.add_subplot(111)  # define axis, so we can modify

ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix

ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!

ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

plt.show()


# In[56]:


# Am using this website to get all the state names and the first 2 letters of every state becouse 
# The graph above is not verifying the state names as expected for example Alabama and Alaska the both
# have similar first 2 letters etc.

import requests

web = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")
dfs = pd.read_html(web.text)


import pandas as pd

# https://www.infoplease.com/state-abbreviations-and-state-postal-codes

dfs = pd.read_html("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")


# In[57]:


# one is states, the other territory
for df in dfs:
    print(df.head()) 


# In[62]:


state_abbv = dfs[0]

state_abbv.head()


# In[83]:


# Now am saving the state_abbv dataset in my computer
state_abbv.to_csv(r'/Users/mohamedsalah/Downloads/state_abbv.csv',index = False)


# In[143]:


state_abbv = pd.read_csv(r'/Users/mohamedsalah/Downloads/state_abbv.csv')
state_abbv.head()


# In[142]:


abbv_dict = state_abbv[["Postal Code"]].to_dict()

abbv_dict = abbv_dict ["Postal Code"]
abbv_dict


# In[145]:


abbv_dict = state_abbv.to_dict()

abbv_dict


# In[140]:


# Now you can see all the state correlation with their unique postal codes

abbv_dict['Guam'] = "GU"
abbv_dict['Puerto Rico'] = "PR"
abbv_dict['Alaska'] = "AK"
abbv_dict['Arkansas'] = "AR"
abbv_dict['California'] = "CA"
abbv_dict['Colorado'] = "CO"
abbv_dict['Connecticut'] = "CT"
abbv_dict['Delaware'] = "DE"
abbv_dict['District of Columbia'] = "DC"
abbv_dict['Hawaii'] = "HI"
abbv_dict['Idaho'] = "ID"
abbv_dict['Indiana'] = "IN"
abbv_dict['Kentucky'] = "KY"
abbv_dict['Maine'] = "ME"
abbv_dict['Maryland'] = "MD"
abbv_dict['Massachusetts'] = "MA"
abbv_dict['Michigan'] = "MI"
abbv_dict['Minnesota'] = "MN"
abbv_dict['Nebraska'] = "NE"
abbv_dict['Nevada'] = "NV"
abbv_dict['New Hampshire'] = "NH"
abbv_dict['New Jersey'] = "NJ"
abbv_dict['New Mexico'] = "NM"
abbv_dict['New York'] = "NY"
abbv_dict['North Carolina'] = "NC"
abbv_dict['North Dakota'] = "ND"
abbv_dict['Ohio'] = "OH"
abbv_dict['Oklahoma'] = "OK"
abbv_dict['Oregon'] = "OR"
abbv_dict['Pennsylvania'] = "PA"
abbv_dict['Rhode Island'] = "RI"
abbv_dict['South Dakota'] = "SD"
abbv_dict['Utah'] = "UT"
abbv_dict['Vermont'] = "VT"
abbv_dict['Washington'] = "WA"
abbv_dict['West Virginia'] = "WV"
abbv_dict['Wisconsin'] = "WI"
abbv_dict['Wyoming'] = "WY"



labels = [abbv_dict[c] for c in min_wage_corr.columns]  # get abbv state names.

fig = plt.figure(figsize=(12,12))  # figure so we can add axis

ax = fig.add_subplot(111)  # define axis, so we can modify
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix

ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!
ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

plt.show()


# In[ ]:




