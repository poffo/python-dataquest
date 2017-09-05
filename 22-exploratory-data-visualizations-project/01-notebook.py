
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib as plot


# In[3]:


# Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
recent_grads = pd.read_csv("recent-grads.csv")

# Use DataFrame.iloc[] to return the first row formatted as a table.
print(recent_grads.iloc[0])


# In[4]:


# Use DataFrame.head() and DataFrame.tail() to become familiar with how the data is structured.
print(recent_grads.head())
print(recent_grads.tail())


# In[5]:


# Use DataFrame.describe() to generate summary statistics for all of the numeric columns.
print(recent_grads.describe())


# In[6]:


# Look up the number of rows in recent_grads and assign the value to raw_data_count.
raw_data_count = len(recent_grads)

# Use DataFrame.dropna() to drop rows containing missing values and assign the resulting DataFrame back to recent_grads.
recent_grads.dropna(axis='index', how='any', inplace=True)

# Look up the number of rows in recent_grads now and assign the value to cleaned_data_count. If you compare cleaned_data_count and raw_data_count, you'll notice that only one row contained missing values and was dropped.

cleaned_data_count = len(recent_grads)

print('cleaned_data_count: %d and raw_data_count: %d' % (cleaned_data_count, raw_data_count))


# In[7]:


get_ipython().magic('matplotlib inline')


# In[8]:


recent_grads.plot(x='Sample_size', y='Employed', kind='scatter')


# In[9]:


recent_grads.plot(x='Sample_size', y='Employed', kind='scatter', title='Employed vs. Sample_size', figsize=(5,10))


# In[10]:


ax = recent_grads.plot(x='Sample_size', y='Employed', kind='scatter')
ax.set_title('Employed vs. Sample_size')


# In[11]:


ax = recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
ax.set_title("Sample_size and Median");


# In[12]:


ax = recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
ax.set_title("Sample_size and Unemployment_rate")


# In[13]:


# - Sample_size and Median
ax = recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
ax.set_title("Sample_size and Median");


# In[14]:


ax = recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
ax.set_title("Sample_size and Unemployment_rate")


# In[15]:


ax = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
ax.set_title('Full_time and Median')


# In[16]:


ax = recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')
ax.set_title('ShareWomen and Unemployment_rate')


# In[17]:


ax = recent_grads.plot(x='Men', y='Median')
ax.set_title('Men and Median')


# In[18]:


ax = recent_grads.plot(x='Women', y='Median')
ax.set_title('Woman and Median')


# In[19]:


major = recent_grads.sort_values(by=('Women'), ascending=False)["Major"].iloc[0:4]
print(major)


# In[20]:


filteredRecentGrads = recent_grads[recent_grads["Major"].isin(major)]


# In[21]:


filteredRecentGrads


# In[22]:


import matplotlib.pyplot as plt
'''
Analyzing the plotting, it shows that Engineering people normally make more money than lower grades category (like agriculture, arts, etc) 
'''

#   - Do students that majored in subjects that were majority female make more money?

major = recent_grads.sort_values(by=('Women'), ascending=False)["Major"].iloc[0:4]
filteredRecentGrads = recent_grads[recent_grads["Major"].isin(major)]


fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.scatter(filteredRecentGrads["Women"], filteredRecentGrads['Median'])
ax1.set_title('Majority Woman courses: women x median salaries')

ax2.scatter(filteredRecentGrads["Men"], filteredRecentGrads['Median'])
ax2.set_title('Majority Woman courses: men x median salaries')

plt.show()


recent_grads.plot(x='Major', y='Women', kind='line')
ax.set_title('Major x women')

plt.show()

'''
Women is majority in these courses:
145              PSYCHOLOGY
34                  NURSING
123                 BIOLOGY
138    ELEMENTARY EDUCATION

Considering these courses, women have the bigger salary comparing to men.
'''

#   - Is there any link between the number of full-time employees and median salary?

ax = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
ax.set_title('Full-time employees and median')

plt.show()

'''
Majority of the employees full-time earn less than 50,000 per year. This is the relation.
'''


# In[23]:


recent_grads['Sample_size'].plot(kind='hist')


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt

# Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
recent_grads = pd.read_csv("recent-grads.csv")

recent_grads["Sample_size"].plot(kind="hist")
plt.show()

recent_grads["Median"].plot(kind="hist")
plt.show()

recent_grads["Employed"].plot(kind="hist")
plt.show()

recent_grads["Full_time"].plot(kind="hist")
plt.show()

recent_grads["ShareWomen"].plot(kind="hist")
plt.show()

recent_grads["Unemployment_rate"].plot(kind="hist")
plt.show()

recent_grads["Men"].plot(kind="hist")
plt.show()

recent_grads["Women"].plot(kind="hist")
plt.show()


# In[25]:


recent_grads["Men"].hist(bins=10, range=(0,150000))
plt.show()

recent_grads["Women"].hist(bins=10, range=(0,150000))
plt.show()


# In[26]:


recent_grads["Men"].sum()


# In[27]:


recent_grads["Women"].sum()


# In[28]:


2876426.0/(3895228.0+2876426.0)


# In[29]:


3895228/(3895228.0+2876426.0)


# In[ ]:





# In[ ]:




