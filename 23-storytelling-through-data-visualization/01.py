'''
Improving Plot Aesthetics
'''


'''
Generate a line chart that visualizes the historical percentage of Biology degrees awarded to women:
- Set the x-axis to the Year column from women_degrees.
- Set the y-axis to the Biology column from women_degrees.
- Display the plot.
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

ax = women_degrees.plot.line(x='Year', y='Biology', legend=None)
ax.set_xlabel("")
ax.set_xlim(1970, 2015)


plt.show()


#####################################


'''
- Generate 2 line charts on the same figure:
  - One that visualizes the percentages of Biology degrees awarded to women over time. Set the line color to "blue" and the label to "Women".
  - One that visualizes the percentages of Biology degrees awarded to men over time. Set the line color to "green" and the label to "Men".
- Set the title of the chart to "Percentage of Biology Degrees Awarded By Gender".
- Generate a legend and place it in the "upper right" location.
- Display the chart.
'''

for col in women_degrees:
    women_degrees[col + '_men'] = 100-women_degrees[col]

women_degrees.rename(columns={"Biology":"Women", "Biology_men":"Men"}, inplace=True)

ax = women_degrees.plot.line(x='Year', y=["Women", 'Men'], color=["blue", "green"], legend=False)

ax.legend(loc='upper right')

#women = mpatches.Patch(label='Women', color='blue')
#men = mpatches.Patch(label='Men', color='green')

ax.tick_params(bottom="off", top="off", left="off", right="off")
ax.set_title("Percentage of Biology Degrees Awarded By Gender")
ax.set_xlim(1970, 2015)
ax.set_xlabel("")

#plt.legend(handles=[women, men], loc='upper right')


plt.show()


#####################################

'''
- Generate 2 line charts on the same plotting area:
    - One that visualizes the percentages of Biology degrees awarded to women over time. Set the line color to "blue" and the label to "Women".
    - One that visualizes the percentages of Biology degrees awarded to men over time. Set the line color to "green" and the label to "Men".
- Remove all of the axis tick marks.
- Hide all of the spines.
- Set the title of the plot to "Percentage of Biology Degrees Awarded By Gender".
- Display the chart.
'''

for col in women_degrees:
    women_degrees[col + '_men'] = 100-women_degrees[col]

women_degrees.rename(columns={'Biology':'Women','Biology_men':'Men'}, inplace=True)

ax = women_degrees.plot.line(x='Year', y=['Women', 'Men'], color=['blue','green'], legend=False)
ax.legend(loc='upper right')
ax.tick_params(bottom='off', top='off', left='off', right='off')

ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)

ax.set_title("Percentage of Biology Degrees Awarded by Gender")

plt.show()


#####################################

'''
- Generate a line chart using the women and men percentages for Biology in the top left subplot.
- Generate a line chart using the women and men percentages for Computer Science in the top right subplot.
- Generate a line chart using the women and men percentages for Engineering in the bottom left subplot.
- Generate a line chart using the women and men percentages for Math and Statistics in the bottom right subplot.
- For all subplots:
    - For the line chart visualizing female percentages, set the line color to "blue" and the label to "Women".
    - For the line chart visualizing male percentages, set the line color to "green" and the label to "Men".
    - Set the x-axis limit to range from 1968 to 2011.
    - Set the y-axis limit to range from 0 to 100.
    - Hide all of the spines and tick marks.
    - Set the title of each subplot to the name of the major category (e.g. "Biology", "Computer Science").
- Place a legend in the upper right corner of the bottom right subplot.
- Display the plot.
'''


major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Add your code here.

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()










