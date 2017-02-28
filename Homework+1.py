
# coding: utf-8

# In[1]:



from __future__ import print_function, division

import nsfg


# In[2]:

nsfg.ReadFemPreg()
pres = nsfg.ReadFemPreg()


# In[3]:

pres


# In[4]:

pres.head(20)


# In[5]:

pres.tail(30)


# In[6]:

print("There are", len(pres.index), "rows and", len(pres.columns), "columns.")


# In[7]:

agescrn = pres.agescrn


# In[8]:

agescrn


# In[9]:

print("Maximum age is", max(agescrn), "and the minimum age is", min(agescrn))


# In[10]:

pres.loc[pres.caseid==2298, "prglngth"]


# In[11]:

numpregs = pres[pres["agescrn"] <=25 ]


# In[12]:

numpregs


# In[13]:

average = sum(pres.agescrn) / len(pres.agescrn)


# In[14]:

print average


# In[15]:

print (average)


# In[ ]:



