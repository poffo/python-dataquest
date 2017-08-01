
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






















