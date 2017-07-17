
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")


# In[5]:


print(data.head())


# In[6]:


print(data.columns)


# In[7]:


data.loc[:,"Do you celebrate Thanksgiving?"].value_counts()


# In[8]:


data["Do you celebrate Thanksgiving?"] == "Yes"


# In[9]:


filterHad = data["Do you celebrate Thanksgiving?"] == "Yes"


# In[10]:


data_filtered = data[filterHad]


# In[11]:


# now it has only 980 rows, it begin it had 1058 rows
len(data)


# In[12]:


data.loc[:,"What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[13]:


filterTofurkey = data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"


# In[14]:


dataTofurkey = data[filterTofurkey]


# In[15]:


dataTofurkey.loc[:,"Do you typically have gravy?"].value_counts()


# In[16]:


dataTofurkey["Do you typically have gravy?"]


# In[17]:


# Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple column is null. Assign to the apple_isnull variable.
# Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin column is null. Assign to the pumpkin_isnull variable.
# Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan column is null. Assign to the pecan_isnull variable.
# Join all three Series using the & operator, and assign the result to ate_pies.
# Display the unique values and how many times each occurs in the ate_pies column.


# In[18]:


apple_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull()


# In[19]:


pumpkin_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()


# In[20]:


pecan_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()


# In[21]:


ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull


# In[22]:


ate_pies.value_counts()


# In[23]:


print(data.Age.head())


# In[24]:


def parseAge(row):
    if(pd.isnull(row["Age"])):
        return None
    ageSplitted = row["Age"].split(" ")
    singleAge = ageSplitted[0]
    singleAge = int(singleAge.replace("+",""))
    return singleAge


# In[25]:


int_age = data.apply(parseAge, axis=1)


# In[26]:


print(int_age)


# In[27]:


print(int_age.describe())


# In[28]:


# since the original dataset has an range of the age, the right one is get the average of the age. Because it's saying from 18-29, it doesn't mean 18, but something in the interval.


# In[29]:


print(data["How much total combined money did all members of your HOUSEHOLD earn last year?"].head(10))
print(data["How much total combined money did all members of your HOUSEHOLD earn last year?"].unique())


# In[30]:


def parseValue(row):
    column = row["How much total combined money did all members of your HOUSEHOLD earn last year?"]
    if(pd.isnull(column) or "Prefer" in column):
        return None
    valueSplitted = column.split(" ")
    singleValue = valueSplitted[0]
    singleValue = int(singleValue.replace("$", "").replace(",",""))
    return singleValue


# In[31]:


int_income = data.apply(parseValue, axis=1)


# In[32]:


print(int_income)
print(int_income.describe())


# In[33]:


print(data["How far will you travel for Thanksgiving?"].value_counts())


# In[34]:


# the difference between the first value_counts and the second two value_counts is because of None (null) values.


# In[35]:


def howFar(bigger):
    if bigger:
        filterIncome = int_income > 150000
    else:
        filterIncome = int_income <= 150000

    filterIncomeData = data["How far will you travel for Thanksgiving?"][filterIncome]
    print(filterIncomeData.value_counts())

print("Those earning more than 150,000: ")
howFar(True)
print("Those earning less than 150,000: ")
howFar(False)


# In[36]:


# Understandings:
# It looks how ear less than 150,000 is planning more trips on Thanksgiving holiday.
# It means that for those that have more money, they will give the party
# It means that for those that ear more they will spend the holiday in their town (maybe they live close to their family)
# Their poor family will travel to visit the rich one (hahaha)
# They have more flexibility and they will schedule the trip in another weekend, because they know the roads and airports are so crazy


# In[37]:


print("Total Size population: ")
print(len(data))
data["int_age"] = int_age
print("pivot table:")
print(data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns="Have you ever attended a \"Friendsgiving?\"", values="int_age"))
#print(data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns="Have you ever attended a \"Friendsgiving?\"", values="int_age", aggfunc=lambda x: len(x)))

# In fact, there are much more young person attending Frindsgiving and whom tried to meet up with someone in hometown


# In[38]:


# Figure out the most common dessert people eat.

import operator

columnsDessert = [col for col in data.columns if "desserts" in col]
dessertsValues = {}

for c in columnsDessert:
    dicValues = data[c].value_counts()
    for v in dicValues.keys():
        finalKey = v.lower()
        if v in dessertsValues:
            dessertsValues[finalKey] = (dicValues[v] + dessertsValues[finalKey]);
        else:
            dessertsValues[finalKey] = dicValues[v];

sortedDesserts = sorted(dessertsValues.items(), key=operator.itemgetter(1), reverse=True)

print(sortedDesserts[:5])

# Understandings:
# - I should handle the "others" category, normalize the data (currently, I am working with lower case to avoid duplications)
# - I am seeing that the first category is 'none', it means that the majority is not having dessert
# - The most common dessert: ice cream, cookies and cheesecake



# In[39]:


# Figure out the most common complete meal people eat.

columnsDishes = [col for col in data.columns if "dishes" in col]
dishesValues = {}

for c in columnsDishes:
    dicValues = data[c].value_counts()
    for v in dicValues.keys():
        finalKey = v.lower()
        if v in dishesValues:
            dishesValues[finalKey] = (dicValues[v] + dishesValues[finalKey]);
        else:
            dishesValues[finalKey] = dicValues[v];

sortedDishes = sorted(dishesValues.items(), key=operator.itemgetter(1), reverse=True)

print(sortedDishes[:5])

# Understandings:
# - The most common dishes: mashed potatoes, rolls/biscuits, green beans, sweet potato casserole


# In[40]:


# Identify how many people work on Thanksgiving.

def parseBooleanToInt(row, args):
    for c in args:
        if c in row:
            if row[c] == "Yes":
                row[c] = 1
            else:
                row[c] = 0

print("\n"*3)
print("Analyzing who works on Blackfriday:")
print(data["Will you employer make you work on Black Friday?"].value_counts())
print(data["Do you work in retail?"].value_counts())

#data.apply(parseBooleanToInt, axis='columns', args=[['Will you employer make you work on Black Friday?','Do you work in retail?']])

data.rename(columns={'Do you work in retail?':'retail', 'Will you employer make you work on Black Friday?':'BF'}, copy=True, inplace=True)

print("\n"*3)

print(data.pivot_table(index="retail", columns="BF", values="int_age", aggfunc=lambda x: len(x)))


# In[41]:


# Find regional patterns in the dinner menus.




# In[42]:


# Find age, gender, and income based patterns in dinner menus.


# In[ ]:




