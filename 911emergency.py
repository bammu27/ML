#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


dt = pd.read_csv('911.csv')


# In[4]:


dt.head(5)


# In[5]:


dt.info()


# In[9]:


dt['zip'].value_counts().head(5)


# In[10]:


dt['twp'].value_counts().head(5)


# In[12]:


len(dt['title'].unique())


# In[13]:


dt['title'].nunique()


# In[37]:


def reason(res):
    
    return res.split(':')[0]
    


# In[38]:



dt['reason'] = dt['title'].apply(lambda x:reason(x))


# In[39]:


dt.head()


# In[41]:


dt.drop('e' ,axis=1,inplace=True)


# In[43]:


dt.head()


# In[44]:


dt['reason'].value_counts()


# In[48]:


sn.countplot(x='reason', data=dt)


# In[55]:


type(dt['timeStamp'][0])


# In[56]:


dt['timeStamp'] = pd.to_datetime(dt['timeStamp'])
type(dt['timeStamp'][0])


# In[57]:


time  = dt['timeStamp'].iloc[0]


# In[58]:


time.hour


# In[59]:


time.year


# In[62]:


time.d


# In[69]:


def timeh(x):
    return x.hour


def timem(x):
    return x.month


def timed(x):
    return x.day_of_week

    


# In[70]:


dt['hour'] = dt['timeStamp'].apply(timeh)


# In[71]:


dt['month'] = dt['timeStamp'].apply(timem)


# In[72]:


dt['day'] = dt['timeStamp'].apply(timed)


# In[78]:


dt['day'].unique()


# In[101]:


dict1 = {0:'sunday',1:'monday',2:'thuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}


# In[102]:


def week(x,y):
    if x==0:
        return y[0]
    elif x==1:
        return y[1]
    elif x==2:
        return y[2]
    elif x==3:
        return y[3]
    elif x==4:
        return y[4]
    elif x==5:
        return y[5]
    else:
        return y[6]


# In[106]:


dt.head()


# In[111]:


sn.countplot(x="dayS" ,data=dt,hue = 'reason')


# In[114]:


dt.drop('dayS',axis=1).head()


# In[115]:


sn.countplot(x="month" ,data=dt,hue = 'reason')


# In[121]:


bym = dt.groupby('month').count()


# In[122]:


bym.resetindex


# In[124]:


sn.lmplot(x='month',y='twp',data=bym.reset_index())


# In[135]:


def Date(x):
    return x.date()

dt['date'] = dt['timeStamp'].apply(Date)
    


# In[136]:


dt.head()


# In[144]:


dayhour = dt.groupby(['hour','month']).count()['reason'].unstack()


# In[145]:


sn.heatmap(dayhour)


# In[ ]:




