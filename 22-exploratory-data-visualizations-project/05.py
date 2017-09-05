'''
- Use bar plots to compare the percentages of women (ShareWomen) from the 10 highest paying majors and from the 10 lowest paying majors.
- Use bar plots to compare the unemployment rate (Unemployment_rate) from the 10 highest paying majors and from the 10 lowest paying majors.
'''


import pandas as pd
import matplotlib.pyplot as plt

recent_grads = pd.read_csv("recent-grads.csv")


####################################

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

# plot the quantity of women
recent_grads[:5]['Women'].plot(kind='bar', ax=ax1)
# plot the courses (major) and the quantity of women
recent_grads[:5].plot.bar(x='Major', y='Women', ax=ax2)

plt.show();

####################################

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

recent_grads[:10].plot.bar(x='Major', y='ShareWomen', ax=ax1)
recent_grads[-10:].plot.bar(x='Major', y='ShareWomen', ax=ax2)

plt.show()

# I can conclude that we have much more women in the 10 lowest majors comparing to the 10 highest majors.

####################################

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate', ax=ax1)
recent_grads[-10:].plot.bar(x='Major', y='Unemployment_rate', ax=ax2)

plt.show();


