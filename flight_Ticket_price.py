#!/usr/bin/env python
# coding: utf-8

# In[231]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Import dataset

# In[232]:


df=pd.read_excel('C:/Users/Sakshi PC/Downloads/Data_Train.xlsx')


# In[233]:


df.head()


# In[234]:


df.info()


# In[235]:


df.shape


# In[236]:


df.count()


# In[237]:


df.dtypes


# In[238]:


df.describe()


# In[239]:


df.isna()     #isna()=isnull() both are equal


# In[240]:


df.isna().sum()


# In[241]:


df[df['Route'].isna()|df['Total_Stops'].isna()]


# In[242]:


df.dropna(inplace=True)


# In[243]:


df.isna().sum()


# # Exploratory data 

# ## Departure and Arrival Time  

# In[244]:


df['Dep_Time']=pd.to_datetime(df['Dep_Time'])
df['Arrival_Time']=pd.to_datetime(df['Arrival_Time'])
df.dtypes


# In[245]:


df['Dep_time_in_hours']=df['Dep_Time'].dt.hour
df['Dep_time_in_mins']=df['Dep_Time'].dt.minute
df['Arrival_time_in_hours']=df['Arrival_Time'].dt.hour
df['Arrival_time_in_mins']=df['Arrival_Time'].dt.minute
df.head()


# In[246]:


df.drop(['Dep_Time','Arrival_Time'],axis=1 , inplace=True)


# In[247]:


df.head()


# ### Date of Journey

# In[248]:


df['Date_of_Journey']=pd.to_datetime(df['Date_of_Journey'])


# In[249]:


df.head()


# In[250]:


df['Date_of_Journey'].dt.year.unique()


# In[251]:


df['Date_of_Journey'].dt.year.unique  #unique() and unique are both different outputs


# In[252]:


df['Day']=df['Date_of_Journey'].dt.day
df['Month']=df['Date_of_Journey'].dt.month
df.head()


# In[253]:


df.drop(['Date_of_Journey'],axis=1,inplace=True)


# In[254]:


df.head()


# ### Total Stops

# In[255]:


'''non-stop=0
1-stop=1
2-stop=2
3-stop=3
4-stop=4
'''


# In[256]:


df['Total_Stops'].value_counts()


# In[257]:


df['Total_Stops']=df['Total_Stops'].map({
    'non-stop':0,
    '1 stop':1,
    '2 stop':2,
    '3 stop':3,
    '4 stop':4
    
})


# In[258]:


df.head()


# ### Additional info 

# In[259]:


df['Additional_Info'].value_counts()


# In[260]:


df.drop(['Additional_Info'],axis=1,inplace=True)


# In[261]:


df.head()


# In[262]:


df.select_dtypes(['object']).columns


# In[263]:


for i in ['Airline', 'Source', 'Destination', 'Total_Stops']:
    plt.figure(figsize=(15,6))
    sns.countplot(data=df,x=i)
    ax=sns.countplot(x=i,data=df.sort_values('Price',ascending=True))
    ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
    plt.show()
    plt.tight_layout()


# ### Airline

# In[264]:


df['Airline'].value_counts()


# In[265]:


plt.figure(figsize=(15,6))
ax=sns.barplot(x='Airline',y='Price',data=df.sort_values('Price',ascending=False))
ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
plt.show()
plt.tight_layout()


# In[266]:


plt.figure(figsize=(15,6))
ax=sns.boxplot(x='Airline',y='Price',data=df.sort_values('Price',ascending=False))
ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
plt.show()
plt.tight_layout()


# In[267]:


df.groupby('Airline').describe()['Price'].sort_values('mean',ascending=False)


# ### Route

# In[268]:


route=df['Route']
route.head()


# In[269]:


df['Total_Stops'].value_counts()


# In[ ]:




