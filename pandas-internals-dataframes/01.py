import pandas as pd

fandango = pd.read_csv("fandango_score_comparison.csv")

print(fandango.head(2))

# it's an attribute, not function!!!
print(fandango.index)


print("\n" *5)

# First five rows
# fandango[0:5]
# From row at 140 and higher
# fandango[140:]
# Just row at index 50
# fandango.iloc[50]
# Just row at index 45 and 90
# fandango.iloc[[45,90]]

# Return a dataframe containing just the first and last rows, and assign it to first_last.

first_last = fandango.iloc[[0,len(fandango)-1]]

print(first_last)


print("\n" *5)

# Use the pandas dataframe method set_index to assign the FILM column as the custom index for the dataframe. Also, specify that we don't want to drop the FILM column from the dataframe. We want to keep the original dataframe, so assign the new one to fandango_films.
# Display the index for fandango_films using the index attribute and the print function.

fandango_films = fandango.set_index("FILM", drop=False)

print(fandango_films.index)


print("\n" *5)


# Select the following movies from fandango_films (in the order in which they appear), and assign them to best_movies_ever:
# "The Lazarus Effect (2015)"
# "Gett: The Trial of Viviane Amsalem (2015)"
# "Mr. Holmes (2015)"

best_movies_ever = fandango_films.loc[["The Lazarus Effect (2015)","Gett: The Trial of Viviane Amsalem (2015)","Mr. Holmes (2015)"]]

print(best_movies_ever)


print("\n" *5)


#### DEMO

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(float_df.head(3))
print(deviations)


print("\n" *5)

# Use the apply() method on float_df to halve each value, and assign the result to halved_df. Then, print the first row.
# halve: Divide into two parts of equal or roughly equal size.

halved_df = float_df.apply(lambda x: x/2)

print(halved_df.head(1))



print("\n" *5)

# Use the apply() method to calculate the average of each movie's values for RT_user_norm and Metacritic_user_nom, and assign the result to the variable rt_mt_means.
# Display the first five values in rt_mt_means.


rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])


rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_means = rt_mt_user.apply(lambda x: np.average(x), axis=1)

print(rt_mt_means.head(5))





