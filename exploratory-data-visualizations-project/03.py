'''
page 3

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

recent_grads["Men"].hist(bins=25, range=(0,150000))
plt.show()

recent_grads["Women"].hist(bins=25, range=(0,150000))
plt.show()

recent_grads["Men"].sum()

recent_grads["Women"].sum()

2876426.0/(3895228.0+2876426.0)

3895228/(3895228.0+2876426.0)

# Use the plots to explore the following questions:
# What percent of majors are predominantly male? Predominantly female?
#   We can see something close to 42% men and 57% women.

# What's the most common median salary range?
# The most common salary is about 36,000.00
'''
count       173.000000
mean      40151.445087
std       11470.181802
min       22000.000000
25%       33000.000000
50%       36000.000000
75%       45000.000000
max      110000.000000
'''
print recent_grads["Median"].describe()




