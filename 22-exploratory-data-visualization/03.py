# Read fandango_scores.csv into a Dataframe named reviews.
# Select the following columns and assign the resulting Dataframe to norm_reviews:
# FILM
# RT_user_norm
# Metacritic_user_nom (note the misspelling of norm)
# IMDB_norm
# Fandango_Ratingvalue
# Fandango_Stars
# Display the first row in norm_reviews

import pandas as pd

reviews = pd.read_csv("fandango_scores.csv")

norm_reviews = reviews[["FILM", "RT_user_norm","Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]]

print(norm_reviews.head(1))
print type(norm_reviews)

###############################

print("\n"*3)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Positions of the left sides of the 5 bars. [0.75, 1.75, 2.75, 3.75, 4.75]
from numpy import arange
bar_positions = arange(5) + 0.75

# Heights of the bars.  In our case, the average rating for the first movie in the dataset.
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values

ax.bar(bar_positions, bar_heights)
ax.bar(bar_positions, bar_heights, 1.5)


###############################

print("\n"*3)


fig, ax = plt.subplots()

# Positions of the left sides of the 5 bars. [0.75, 1.75, 2.75, 3.75, 4.75]
from numpy import arange
bar_positions = arange(5) + 0.75

# Heights of the bars.  In our case, the average rating for the first movie in the dataset.
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values

ax.bar(bar_positions, bar_heights)

plt.show()



###############################

print("\n"*3)

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75

fig, ax = plt.subplots()

ax.bar(bar_positions, bar_heights, 0.5)

plt.show()


###############################

print("\n"*3)

#Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
#Generate a bar plot with:
#left set to bar_positions
#height set to bar_heights
#width set to 0.5
#Set the x-axis tick positions to tick_positions.
#Set the x-axis tick labels to num_cols and rotate by 90 degrees.
#Set the x-axis label to "Rating Source".
#Set the y-axis label to "Average Rating".
#Set the plot title to "Average User Rating For Avengers: Age of Ultron (2015)".
#Use plt.show() to display the bar plot.

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()

ax.bar(bar_positions, bar_heights, 0.5)

ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_xlabel("Rating Source")
ax.set_ylabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")

plt.show()



###############################

print("\n"*3)


import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)


# Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
# Generate a bar plot with:
# bottom set to bar_positions
# width set to bar_widths
# height set to 0.5
# Set the y-axis tick positions to tick_positions.
# Set the y-axis tick labels to num_cols.
# Set the y-axis label to "Rating Source".
# Set the x-axis label to "Average Rating".
# Set the plot title to "Average User Rating For Avengers: Age of Ultron (2015)".
# Use plt.show() to display the bar plot.

fig, ax = plt.subplots()

print bar_positions
print bar_widths
print num_cols

# printing
# [ 0.75  1.75  2.75  3.75  4.75]
# [ 4.3   3.55  3.9   4.5   5.  ]
# ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

ax.barh(bottom=bar_positions, width=bar_widths, height=0.5)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
ax.set_ylabel("Rating Source")
ax.set_xlabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()



###############################
print("\n"*3)


# Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
# Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
# Use plt.show() to display the resulting plot.

fig, ax = plt.subplots()

Fandango_Ratingvalue = reviews["Fandango_Ratingvalue"]
RT_user_norm = reviews["RT_user_norm"]

ax.scatter(Fandango_Ratingvalue, RT_user_norm)

ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")

plt.show()

# The scatter plot suggests that there's a weak, positive correlation between the user ratings on Fandango and the user ratings on Rotten Tomatoes. The correlation is weak because for many x values, there are multiple corresponding y values. The correlation is positive because, in general, as x increases, y also increases.
# When using scatter plots to understand how 2 variables are correlated, it's usually not important which one is on the x-axis and which one is on the y-axis. This is because the relationship is still captured either way, even if the plots look a little different. If you want to instead understand how an independent variable affects a dependent variables, you want to put the independent one on the x-axis and the dependent one on the y-axis. Doing so helps emphasize the potential cause and effect relation.



###############################

print("\n"*3)

# For the subplot associated with ax1:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
# Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
# For the subplot associated with ax2:
# Generate a scatter plot with the RT_user_norm column on the x-axis and the Fandango_Ratingvalue column on the y-axis.
# Set the x-axis label to "Rotten Tomatoes" and the y-axis label to "Fandango".
# Use plt.show() to display the resulting plot.

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")

ax2.set_xlabel("Rotten Tomatoes")
ax2.set_ylabel("Fandango")

ax1.scatter(Fandango_Ratingvalue, RT_user_norm)
ax2.scatter(RT_user_norm, Fandango_Ratingvalue)

plt.show()



###############################

print("\n"*3)

# For the Subplot associated with ax1:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
# Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
# Set the x-axis and y-axis data limits to range from 0 and 5.
# For the Subplot associated with ax2:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the Metacritic_user_nom column on the y-axis.
# Set the x-axis label to "Fandango" and the y-axis label to "Metacritic".
# Set the x-axis and y-axis data limits to range from 0 and 5.
# For the Subplot associated with ax3:
# Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the IMDB_norm column on the y-axis.
# Set the x-axis label to "Fandango" and the y-axis label to "IMDB".
# Set the x-axis and y-axis data limits to range from 0 and 5.
# Use plt.show() to display the plots.

Metacritic_user_nom = reviews["Metacritic_user_nom"]
IMDB_norm = reviews["IMDB_norm"]

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(Fandango_Ratingvalue, RT_user_norm)
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax1.set_ylim(0,5)

ax2.scatter(Fandango_Ratingvalue, Metacritic_user_nom)
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_ylim(0,5)

ax3.scatter(Fandango_Ratingvalue, IMDB_norm)
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")
ax3.set_ylim(0,5)

plt.show()

# From the scatter plots, we can conclude that user ratings from IMDB and Fandango are the most similar. In addition, user ratings from Metacritic and Rotten Tomatoes have positive but weak correlations with user ratings from Fandango. We can also notice that user ratings from Metacritic and Rotten Tomatoes span a larger range of values than those from IMDB or Fandango. User ratings from Metacritic and Rotten Tomatoes range from 1 to 5. User ratings from Fandango range approximately from 2.5 to 5 while those from IMDB range approximately from 2 to 4.5.
# The scatter plots unfortunately only give us a cursory understanding of the distributions of user ratings from each review site. For example, if a hundred movies had the same average user rating from IMDB and Fandango in the dataset, we would only see a single marker in the scatter plot. In the next mission, we'll learn about two types of plots that help us understand distributions of values.


###############################

print("\n"*3)









