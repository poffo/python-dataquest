'''
Rank - Rank by median earnings (the dataset is ordered by this column).
Major_code - Major code.
Major - Major description.
Major_category - Category of major.
Total - Total number of people with major.
Sample_size - Sample size (unweighted) of full-time.
Men - Male graduates.
Women - Female graduates.
ShareWomen - Women as share of total.
Employed - Number employed.
Median - Median salary of full-time, year-round workers.
Low_wage_jobs - Number in low-wage service jobs.
Full_time - Number employed 35 hours or more.
Part_time - Number employed less than 35 hours.
'''

'''
questions: 

Do students in more popular majors make more money?
    Using scatter plots
How many majors are predominantly male? Predominantly female?
    Using histograms
Which category of majors have the most students?
    Using bar plots
'''

'''
Instructions

 - Let's setup the environment by importing the libraries we need and running the necessary Jupyter magic so that plots are displayed inline.
    - Import pandas and matplotlib into the environment.
    - Run the Jupyter magic %matplotlib inline so that plots are displayed inline.
 - Read the dataset into a DataFrame and start exploring the data.
    - Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
    - Use DataFrame.iloc[] to return the first row formatted as a table.
    - Use DataFrame.head() and DataFrame.tail() to become familiar with how the data is structured.
    - Use DataFrame.describe() to generate summary statistics for all of the numeric columns.
 - Drop rows with missing values. Matplotlib expects that columns of values we pass in have matching lengths and missing values will cause matplotlib to throw errors.
    - Look up the number of rows in recent_grads and assign the value to raw_data_count.
    - Use DataFrame.dropna() to drop rows containing missing values and assign the resulting DataFrame back to recent_grads.
    - Look up the number of rows in recent_grads now and assign the value to cleaned_data_count. If you compare cleaned_data_count and raw_data_count, you'll notice that only one row contained missing values and was dropped.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
recent_grads = pd.read_csv("recent-grads.csv")

# Use DataFrame.iloc[] to return the first row formatted as a table.
print(recent_grads.iloc[0])

# Use DataFrame.head() and DataFrame.tail() to become familiar with how the data is structured.
print(recent_grads.head())
print(recent_grads.tail())

# Use DataFrame.describe() to generate summary statistics for all of the numeric columns.
print(recent_grads.describe())

# Look up the number of rows in recent_grads and assign the value to raw_data_count.
raw_data_count = len(recent_grads)

# Use DataFrame.dropna() to drop rows containing missing values and assign the resulting DataFrame back to recent_grads.
recent_grads.dropna(axis='index', how='any', inplace=True)

# Look up the number of rows in recent_grads now and assign the value to cleaned_data_count. If you compare cleaned_data_count and raw_data_count, you'll notice that only one row contained missing values and was dropped.

cleaned_data_count = len(recent_grads)

print('cleaned_data_count: %d and raw_data_count: %d' % (cleaned_data_count, raw_data_count))


'''
 - Generate scatter plots in separate jupyter notebook cells to explore the following relations:
    - Sample_size and Median
    - Sample_size and Unemployment_rate
    - Full_time and Median
    - ShareWomen and Unemployment_rate
    - Men and Median
    - Women and Median
- Use the plots to explore the following questions:
    - Do students in more popular majors make more money?
    - Do students that majored in subjects that were majority female make more money?
    - Is there any link between the number of full-time employees and median salary?
'''

# - Sample_size and Median
ax = recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
ax.set_title("Sample_size and Median");

plt.show()


# Sample_size and Unemployment_rate
ax = recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
ax.set_title("Sample_size and Unemployment_rate")

plt.show()

# Full_time and Median
ax = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
ax.set_title('Full_time and Median')

plt.show()

# ShareWomen and Unemployment_rate
ax = recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')
ax.set_title('ShareWomen and Unemployment_rate')

plt.show()

# Men and Median
ax = recent_grads.plot(x='Men', y='Median', kind='scatter')
ax.set_title('Men and Median')

plt.show()


# Women and Median
ax = recent_grads.plot(x='Women', y='Median', kind='scatter')
ax.set_title('Women and Median')

plt.show()

# - Use the plots to explore the following questions:
#   - Do students in more popular majors make more money?

ax = recent_grads.plot(x='Major_category', y='Median', kind='line')
ax.set_title('Major_category x Median')

plt.show()

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






# 3: Pandas, Histograms

'''
Instructions

- Generate histograms in separate jupyter notebook cells to explore the distributions of the following columns:
    - Sample_size
    - Median
    - Employed
    - Full_time
    - ShareWomen
    - Unemployment_rate
    - Men
    - Women

- We encourage you to experiment with different bin sizes and ranges when generating these histograms.
- Use the plots to explore the following questions:
    - What percent of majors are predominantly male? Predominantly female?
    - What's the most common median salary range?
'''







