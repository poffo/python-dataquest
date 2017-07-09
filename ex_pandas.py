import pandas

food_info = pandas.read_csv("food_info.csv")

print(type(food_info))





print("\n" *6)

print(food_info.head(10))




print("\n" *6)

print(food_info.loc[0:10])
hundredth_row = food_info.loc[99]
print(hundredth_row)

#print the type for each column
print(food_info.dtypes)

last_rows = food_info.loc[(len(food_info)-5):len(food_info)]
print(last_rows)

#selecting specific columns
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]
print(saturated_fat)
print(cholesterol)
selenium_thiamin = food_info[["FA_Sat_(g)","Cholestrl_(mg)"]]
print(selenium_thiamin)

print("\n" *6)

#Select and display only the columns that use grams for measurement (that end with "(g)"). To accomplish this:
#Use the columns attribute to return the column names in food_info and convert to a list by calling the method tolist()
#Create a new list, gram_columns, containing only the column names that end in "(g)". The string method endswith() returns True if the string object calling the method ends with the string passed into the parentheses.
#Pass gram_columns into bracket notation to select just those columns and assign the resulting dataframe to gram_df
#Then use the dataframe method head() to display the first 3 rows of gram_df.

columns = food_info.columns.tolist()
gram_columns = []

for c in columns:
    if c.endswith('(g)'):
        gram_columns.append(c)

gram_df = food_info[gram_columns]
print(gram_df.head(3))

print("\n" *6)



print("\n" *6)










