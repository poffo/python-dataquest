'''
page 2

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

import pandas as pd
import matplotlib.pyplot as plt

# Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
recent_grads = pd.read_csv("recent-grads.csv")

fig = plt.figure(figsize=(1,12))

#  - Sample_size and Median
ax1 = fig.add_subplot(3,2,1)
ax1.scatter(recent_grads["Sample_size"], recent_grads["Median"])
ax1.set_title("Sample Size x Median")
ax1.set_xlabel("Sample Size")
ax1.set_ylabel("Median")

#   - Sample_size and Unemployment_rate

ax2 = fig.add_subplot(3,2,2)
ax2.scatter(recent_grads["Sample_size"], recent_grads["Unemployment_rate"])
ax2.set_title("Sample size x Unemployment Rate")
ax2.set_xlabel("Sample Size")
ax2.set_ylabel("Unemployment Rate")

#   - Full_time and Median
ax3 = fig.add_subplot(3,2,3)
ax3.scatter(recent_grads["Full_time"], recent_grads["Median"])
ax3.set_title("Full time x Median")
ax3.set_xlabel("Full time")
ax3.set_ylabel("Median")

#  - ShareWomen and Unemployment_rate
ax4 = fig.add_subplot(3,2,4)
ax4.scatter(recent_grads["ShareWomen"], recent_grads["Unemployment_rate"])
ax4.set_title("ShareWomen x Unemployment_rate")
ax4.set_xlabel("ShareWomen")
ax4.set_ylabel("Unemployment Rate")

#  - Men and Median
ax5 = fig.add_subplot(3,2,5)
ax5.scatter(recent_grads["Men"], recent_grads["Median"])
ax5.set_title("Men x Median")
ax5.set_xlabel("Men")
ax5.set_ylabel("Median")

#  - Women and Median
ax6 = fig.add_subplot(3,2,6)
ax6.scatter(recent_grads["Women"], recent_grads["Median"])
ax6.set_title("Women x Median")
ax6.set_xlabel("Women")
ax6.set_ylabel("Median")

plt.show()


'''
- Use the plots to explore the following questions:
  - Do students in more popular majors make more money?
No, the more popular majors, normally, make the same money as the not popular majors. The first chart represents this idea. 

  - Do students that majored in subjects that were majority female make more money?
Considering these courses (line 22), women have a bigger salary comparing to men in women courses.

  - Is there any link between the number of full-time employees and median salary?
Majority of the employees full-time earn less than 50,000 per year. This is the relation.
'''










