import pandas as pd
from pandas import Series

fandango = pd.read_csv("fandango_score_comparison.csv")

print(fandango.head(2))


print("\n" *5)

# Select the FILM column, assign it to the variable series_film, and print the first five values.
# Then, select the RottenTomatoes column, assign it to the variable series_rt, and print the first five values.

series_film = fandango["FILM"]
series_rt = fandango["RottenTomatoes"]

print(series_film[0:5])
print(series_rt[0:5])

print("\n" *5)


series_custom = pd.Series(series_rt.values, index=series_film.values)
print(series_custom[['Minions (2015)', 'Leviathan (2014)']])

print("\n" *5)

# Assign the values in series_custom at indexes 5 through 10 to the variable fiveten. Then, print fiveten to verify that you can still use integer values for selection.

fiveten = series_custom[5:11]

print(fiveten)

print("\n" *5)

# The list original_index contains the original index. Sort this index using the Python 3 core method sorted(), then pass the result in to the Series method reindex().
# Store the result in a variable named sorted_by_index.

original_index = series_custom.index

sorted_index = sorted(original_index)

sorted_by_index = series_custom.reindex(index=sorted_index)

print("\n" *5)

# Sort series_custom by index using sort_index(), and assign the result to the variable sc2.
# Sort series_custom by values, and assign the result to the variable sc3.
# Finally, print the first 10 values in sc2 and the first 10 values in sc3.

sc2 = series_custom.sort_index()

sc3 = series_custom.sort_values()

print(sc2.head(10))
print(sc3.head(10))


print("/n"*5)


# Normalize series_custom (which is currently on a 0 to 100-point scale) to a 0 to 5-point scale by dividing each value by 20.
# Assign the new normalized Series object to series_normalized.

print(series_custom)

#since the biggest value is 100, dividing by 20 will give to us the maximum value of 5.
print(series_custom.max())

series_normalized = series_custom / 20

print(series_normalized)


print("/n"*5)

# In the following code cell, the criteria_one and criteria_two statements return Boolean Series objects.
# Return a filtered Series object named both_criteria that only contains the values where both criteria are true. Use bracket notation and the & operator to obtain this Series object.

criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[criteria_one & criteria_two]

print(both_criteria)


print("/n"*5)

# rt_critics and rt_users are Series objects containing the average ratings from critics and users for each film.
# Both Series objects use the same custom string index, which they base on the film names. Use the Python arithmetic operators to return a new Series object, rt_mean, that contains the mean ratings from both critics and users for each film.

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

print(rt_critics.head(3))
print(rt_users.head(3))

rt_mean = ((rt_critics + rt_users)/2)

print(rt_mean)





