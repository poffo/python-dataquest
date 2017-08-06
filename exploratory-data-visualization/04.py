
'''
    histograms-and-box-plots
'''

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
print(norm_reviews[:5])


########################################################
print("\n"*4)
########################################################
# Example:

df = pd.read_csv('fandango_scores.csv')

freq_counts = df['Fandango_Ratingvalue'].value_counts()

freq_counts = df['Fandango_Ratingvalue'].value_counts()
sorted_freq_counts = freq_counts.sort_index()

# Exercise
# Use the value_counts() method to return the frequency counts for the Fandango_Ratingvalue column. Sort the resulting Series object by the index and assign to fandango_distribution.
# Use the value_counts() method to return frequency counts the IMDB_norm column. Sort the resulting Series object by the index and assign to imdb_distribution.
# Use the print() function to display fandango_distribution and imdb_distribution.

import pandas as pd
df = pd.read_csv('fandango_scores.csv')

fandango_distribution = df['Fandango_Ratingvalue'].value_counts().sort_index()
imdb_distribution = df['IMDB_norm'].value_counts().sort_index()

print(fandango_distribution)
print(imdb_distribution)



########################################################
print("\n"*4)
########################################################

# While histograms use bars whose lengths are scaled to the values they're representing, they differ from bar plots in a few ways. Histograms help us visualize continuous values using bins while bar plots help us visualize discrete values. The locations of the bars on the x-axis matter in a histogram but they don't in a simple bar plot. Lastly, bar plots also have gaps between the bars, to emphasize that the values are discrete.

# Exercise
# Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
# Generate a histogram from the values in the Fandango_Ratingvalue column using a range of 0 to 5.
# Use plt.show() to display the plot.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fandango_scores.csv')
fig, ax = plt.subplots()

ax.hist(df['Fandango_Ratingvalue'], range=(0,5))

plt.show()

########################################################
print("\n"*4)
########################################################

# 5: Comparing Histograms

# For the subplot associated with ax1:
# Generate a histogram of the values in the Fandango_Ratingvalue column using 20 bins and a range of 0 to 5.
# Set the title to Distribution of Fandango Ratings.
# For the subplot associated with ax2:
# Generate a histogram of the values in the RT_user_norm column using 20 bins and a range of 0 to 5.
# Set the title to Distribution of Rotten Tomatoes Ratings.
# For the subplot associated with ax3:
# Generate a histogram of the values in the Metacritic_user_nom column using 20 bins and a range of 0 to 5.
# Set the title to Distribution of Metacritic Ratings.
# For the subplot associated with ax4:
# Generate a histogram of the values in the IMDB_norm column using 20 bins and a range of 0 to 5.
# Set the title to Distribution of IMDB Ratings.
# For all subplots:
# Set the y-axis range to 0 to 50 using Axes.set_ylim().
# Set the y-axis label to Frequency using Axes.set_ylabel().
# Use plt.show() to display the plots.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fandango_scores.csv')

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(df["Fandango_Ratingvalue"], bins=20, range=(0,5))
ax1.set_title("Distribution of Fandango Ratings")

ax2.hist(df["RT_user_norm"], bins=20, range=(0,5))
ax2.set_title("Distribution of Rotten Tomatoes Rating")

ax3.hist(df["Metacritic_user_nom"], bins=20, range=(0,5))
ax3.set_title("Distribution of Metacritic Ratings")

ax4.hist(df["IMDB_norm"], bins=20, range=(0,5))
ax4.set_title("Distribution of IMDB Ratings")

def applyAx(ax):
    ax.set_ylim(0,50)
    ax.set_ylabel("Frequency")

applyAx(ax1)
applyAx(ax2)
applyAx(ax3)
applyAx(ax4)

plt.show()


########################################################
print("\n"*4)
########################################################

# 7: Box Plot

# Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
# Generate a box plot from the values in the RT_user_norm column.
# Set the y-axis limit to range from 0 to 5.
# Set the x-axis tick label to Rotten Tomatoes.
# Use plt.show() to display the plot.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fandango_scores.csv')

fig, ax = plt.subplots()

ax.boxplot(df["RT_user_norm"])
ax.set_ylim(0,5)
ax.set_xticklabels(["Rotten Tomatoes"])


plt.show()


########################################################
print("\n"*4)
########################################################

# 8: Multiple Box Plots

# Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
# Generate a box plot containing a box-and-whisker diagram for each column in num_cols.
# Set the x-axis tick labels to the column names in num_cols and rotate the ticks by 90 degrees.
# Set the y-axis limit to range from 0 to 5.
# Use plt.show() to display the plot.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fandango_scores.csv')

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

fig, ax = plt.subplots()

ax.boxplot(df[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)

plt.show()



# From the boxplot, we can reach the following conclusions:
#   user ratings from Rotten Tomatoes and Metacritic span a larger range of values
#   user ratings from IMDB and Fandango are both skewed in the positive direction and span a more constrained range of values


