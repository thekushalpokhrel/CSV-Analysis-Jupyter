#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('C:/Users/user/Downloads/Effects-of-COVID-19-on-trade-1-February-25-November-2020-provisional.csv')


# In[4]:


df


# In[5]:


print (country_df.head())


# In[6]:


country_df = df['country']


# In[7]:


df


# In[8]:


print (df.head())


# In[9]:


print (df.info())


# In[10]:


print (country_df.head())


# In[11]:


print (df.info())


# In[12]:


df_country = df ['Country']


# In[13]:


print (df_country.head())


# In[14]:


print (df_country.tail())


# In[15]:


print(subset.tail)


# In[16]:


df_subset = df[['Country', 'Measure','Value']]


# In[17]:


print(subset.head())


# In[18]:


print(subset.head)


# In[19]:


df_subset = df[['Country', 'Measure','Value']]


# In[20]:


print(subset.head)


# In[21]:


subset = df[['Country', 'Measure','Value']]


# In[22]:


print(subset.head())


# In[23]:


print(subset.tail())


# In[24]:


print(df.loc[0])


# In[25]:


print(df.loc[30])


# In[26]:


print(df.loc[12])


# In[27]:


print(df.tail(n=1))


# In[28]:


print(df.tail(n=2))


# In[29]:


print(df.tail(n=3))


# In[ ]:




