
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")


# In[3]:


print(data.head())


# In[5]:


print(data.columns)


# In[ ]:


# Understanding the value in Age column
print(data.Age.head())

def parseAge(row):
    if(pd.isnull(row["Age"])):
        return None
    ageSplitted = row["Age"].split(" ")
    singleAge = ageSplitted[0]
    singleAge = int(singleAge.replace("+",""))
    return singleAge

int_age = data.apply(parseAge, axis=1)

print(int_age)

print(int_age.describe())



print(data["How much total combined money did all members of your HOUSEHOLD earn last year?"].head(10))
print(data["How much total combined money did all members of your HOUSEHOLD earn last year?"].unique())

def parseValue(row):
    column = row["How much total combined money did all members of your HOUSEHOLD earn last year?"]
    if(pd.isnull(column) or "Prefer" in column):
        return None
    valueSplitted = column.split(" ")
    singleValue = valueSplitted[0]
    singleValue = int(singleValue.replace("$", "").replace(",",""))
    return singleValue

int_income = data.apply(parseValue, axis=1)

print(int_income)
print(int_income.describe())


print(data["How far will you travel for Thanksgiving?"].value_counts())

# the difference between the first value_counts and the second two value_counts is because of None (null) values.

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

# Understandings:
# It looks how ear less than 150,000 is planning more trips on Thanksgiving holiday.
# It means that for those that have more money, they will give the party
# It means that for those that ear more they will spend the holiday in their town (maybe they live close to their family)
# Their poor family will travel to visit the rich one (hahaha)
# They have more flexibility and they will schedule the trip in another weekend, because they know the roads and airports are so crazy

print("Total Size population: ")
print(len(data))
data["int_age"] = int_age
print("pivot table:")
print(data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns="Have you ever attended a \"Friendsgiving?\"", values="int_age"))
#print(data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns="Have you ever attended a \"Friendsgiving?\"", values="int_age", aggfunc=lambda x: len(x)))

# In fact, there are much more young person attending Frindsgiving and whom tried to meet up with someone in hometown





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


# Find regional patterns in the dinner menus.







# Find age, gender, and income based patterns in dinner menus.


























