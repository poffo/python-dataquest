#Use the DataFrame.pivot_table() method to calculate the mean age for each passenger class ("pclass").
#Assign the result to passenger_age.
#Display the passenger_age pivot table using the print() function.

import pandas

titanic_survival = pandas.read_csv("titanic_survival.csv")

passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")

passenger_age = titanic_survival.pivot_table(index="pclass", values="age", aggfunc="mean")

print(passenger_age)


print("/n" *5)


#Make a pivot table that calculates the total fares collected ("fare") and total number of survivors ("survived") for each embarkation port ("embarked").
#Assign the result to port_stats.
#Display port_stats using the print() function.

import numpy as np

titanic_survival = pandas.read_csv("titanic_survival.csv")

port_stats = titanic_survival.pivot_table(index="embarked", values=["fare","survived"], aggfunc=np.sum)

print(port_stats)



print("/n" *5)

#Drop all columns in titanic_survival that have missing values and assign the result to drop_na_columns.
#Drop all rows in titanic_survival where the columns "age" or "sex" have missing values and assign the result to new_titanic_survival.

#axis : {0 or 'index', 1 or 'columns'}, or tuple/list thereof
#Pass tuple or list to drop on multiple axes
#how : {'any', 'all'}
#any : if any NA values are present, drop that label
#all : if all values are NA, drop that label

columns = titanic_survival.columns.tolist()
print(columns)

drop_na_rows = titanic_survival.dropna(axis='columns', how="any")

print("removed all columns with NULL as rows: ")
print(drop_na_rows)

new_titanic_survival = titanic_survival.dropna(axis='index', subset=["age","sex"], how="any")

print("removed rows when there is NULL: ")
print(new_titanic_survival)



print("/n" *5)


#Assign the first ten rows from new_titanic_survival to first_ten_rows.
#Assign the fifth row from new_titanic_survival to row_position_fifth.
#Assign the row with index label 25 from new_titanic_survival to row_index_25.

#Then s.iloc[:3] returns the first 3 rows (since it looks at the position) and s.loc[:3] returns the first 8 rows (since it looks at the labels):

new_titanic_survival = titanic_survival.sort_values(by="age", ascending=False)

first_ten_rows = new_titanic_survival.iloc[0:10]
print(first_ten_rows)

#starting from 0, getting the position 4 to get the fith element.
row_position_fifth = new_titanic_survival.iloc[4]

print(row_position_fifth)

row_index_25 = new_titanic_survival.loc[25]




print("/n" *5)

#using loc (by column name) and iloc (by column index) to get rows

first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row_index_83_age = new_titanic_survival.loc[83,"age"]
row_index_766_pclass = new_titanic_survival.loc[766,"pclass"]


row_index_1100_age = new_titanic_survival.loc[1100,"age"]
row_index_25_survived = new_titanic_survival.loc[25, "survived"]
five_rows_three_cols = new_titanic_survival.iloc[0:5, 0:3]


print("/n" *5)

# new_titanic_survival has the data sorted by age
titanic_reindexed = new_titanic_survival.reset_index(drop=True)

print(titanic_reindexed.iloc[0:5,0:3])



print("/n" *5)

# Write a function that counts the number of null elements in a Series.
# Use the DataFrame.apply() method along with your function to run across all the columns in titanic_survival.
# Assign the result to column_null_count.

def countNulls(column):
    nulls = pandas.isnull(column)
    # since column is a series, it's not needed to specify the columns (has only one)
    newDataSet = column[nulls]
    return len(newDataSet)


column_null_count = titanic_survival.apply(countNulls)

print(column_null_count)


print("/n" *5)


# Create a function that returns the string "minor" if someone is under 18, "adult" if they are equal to or over 18, and "unknown" if their age is null.
# Then, use the function along with .apply() to find the correct label for everyone in the titanic_survival dataframe.
# Assign the result to age_labels.
# You can use pd.isnull to check if a value is null or not.


def ageMeaning(row):
    if row["age"] < 18:
        return "minor"
    elif row["age"] >= 18:
        return "adult"
    if pandas.isnull(row["age"]):
        return "unknown"

age_labels = titanic_survival.apply(ageMeaning, axis=1)

print age_labels










