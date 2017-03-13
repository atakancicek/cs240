
# coding: utf-8

# In[1]:

from __future__ import print_function, division

get_ipython().magic(u'matplotlib inline')

import numpy as np

import nsfg
import first


# In[2]:

pres = nsfg.ReadFemResp()


# In[3]:

pres.fmar1age


# In[4]:

first_mariage = pres.fmar1age


# In[5]:

first_mariage.value_counts()


# In[6]:

import thinkstats2
import thinkplot


# In[7]:

hist = thinkstats2.Hist(first_mariage, label='FIRST MARIAGES')
thinkplot.Hist(hist)
thinkplot.Config(xlabel='Age', ylabel='Number of People', width=0.5)


# In[8]:

pres.fmarno


# In[9]:

num_of_mariage = pres.fmarno


# In[10]:

num_of_mariage.value_counts()


# In[11]:

hist = thinkstats2.Hist(num_of_mariage, label='NUMBER OF MARRIAGES')
thinkplot.Hist(hist)
thinkplot.Config(xlabel='Times Married', ylabel="Number of People", width=0.5)


# In[12]:

pres.totincr


# In[13]:

total_income = pres.totincr


# In[14]:

total_income.value_counts()


# In[15]:

hist = thinkstats2.Hist(total_income, label='TOTAL INCOME')
thinkplot.Hist(hist)
thinkplot.Config(xlabel='Value', ylabel="Total", width=0.5)


# In[16]:

neverMarried = []
married = []


# In[17]:

for number in pres.fmarno:
    if number == 0:
        neverMarried.append(number)
    else:
        married.append(number)


# In[18]:

print (len(neverMarried), "people have never been married before.")
print (len(married), "people have married atleast once.")


# In[24]:

neverMarried = pres[pres.fmarno == 0]
married = pres[pres.fmarno != 0]
never_hist = thinkstats2.Hist(neverMarried.totincr, label='Never Married')
atleast_once_hist = thinkstats2.Hist(married.totincr, label='Marriage Atleast Once')


# In[27]:

width = 0.40
thinkplot.PrePlot(2)
thinkplot.Hist(never_hist, align='right', width=width)
thinkplot.Hist(atleast_once_hist, align='left', width=width)
thinkplot.Config(xlabel="Value", ylabel='Income')


# In[30]:

mean = pres.totincr.mean()
var = pres.totincr.var()
std = pres.totincr.std()


# In[31]:

print ("The mean of the respondents' total income is", mean)
print ("The variance respondents' total income is", var)
print ("The standart deviation of respondents' total income is", std)


# In[36]:

print ("The Maximum value for respondents' total income is", max(total_income))
print ("The Minimum value for respondents' total income is", min(total_income))


# In[ ]:



