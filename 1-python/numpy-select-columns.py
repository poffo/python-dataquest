import numpy

matrix = numpy.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])

second_column_25 = (matrix[:,1] == 25)
print(second_column_25)

#select rows where the second column is True
print(matrix[second_column_25, :])

print("\n"*6)

#Compare the third column of world_alcohol to the string Algeria.
#Assign the result to country_is_algeria.
#Select only the rows in world_alcohol where country_is_algeria is True.
#Assign the result to country_algeria.

world_alcohol = numpy.array([['1986', 'Western Pacific', 'Canada', 'Wine', '0'],
                           ['1986', 'Americas', 'Uruguay', 'Other', '0.5'],
                           ['1985', 'Africa', "Cte d'Ivoire", 'Wine', '1.62'],
                           ['1986', 'Europe', 'Switzerland', 'Spirits', '2.54'],
                           ['1986', 'Europe', 'Switzerland', 'Spirits', '2.54'],
                           ['1987', 'Western Pacific', 'Papua New Guinea', 'Other', '0'],
                           ['1987', 'Western Pacific', 'Papua New Guinea', 'Other', ''],
                           ['1986', 'Africa', 'Algeria', 'Other', '5.15']])


country_is_algeria = (world_alcohol[:,2] == 'Algeria')
country_algeria = (world_alcohol[(world_alcohol[:,2] == 'Algeria'),:])

print(country_is_algeria)
print(country_algeria)

print("\n"*6)

#Perform a comparison with multiple conditions, and join the conditions with &.
#Compare the first column of world_alcohol to the string 1986.
#Compare the third column of world_alcohol to the string Algeria.
#Enclose each condition in parentheses, and join the conditions with &.
#Assign the result to is_algeria_and_1986.
#Use is_algeria_and_1986 to select rows from world_alcohol.
#Assign the rows that is_algeria_and_1986 selects to rows_with_algeria_and_1986.

is_algeria_and_1986 = ((world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria'))
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

print(is_algeria_and_1986)
print(rows_with_algeria_and_1986)

print("\n"*6)

#Replace all instances of the string 1986 in the first column of world_alcohol with the string 2014.
#Replace all instances of the string Wine in the fourth column of world_alcohol with the string Grog.

print(world_alcohol)

is_1886 = (world_alcohol[:,0] == '1986')
world_alcohol[is_1886,0] = '2014'

is_wine = (world_alcohol[:,3] == 'Wine')
world_alcohol[is_wine,3] = 'Grog'

print(world_alcohol)

print("\n"*6)

#Compare all the items in the fifth column of world_alcohol with an empty string ''. Assign the result to is_value_empty.
#Select all the values in the fifth column of world_alcohol where is_value_empty is True, and replace them with the string 0.

print(world_alcohol)

is_value_empty = (world_alcohol[:,4] == '')
world_alcohol[is_value_empty,4] = '0'

print(world_alcohol)

print("\n"*6)

#Extract the fifth column from world_alcohol, and assign it to the variable alcohol_consumption.
#Use the astype() method to convert alcohol_consumption to the float data type.

print(world_alcohol)

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

print(alcohol_consumption)

print("\n"*6)



#sum() -- Computes the sum of all the elements in a vector, or the sum along a dimension in a matrix
#mean() -- Computes the average of all the elements in a vector, or the average along a dimension in a matrix
#max() -- Identifies the maximum value among all the elements in a vector, or the maximum along a dimension in a matrix

vector = numpy.array([5, 10, 15, 20])
vector.sum()


#Use the sum() method to calculate the sum of the values in alcohol_consumption. Assign the result to total_alcohol.
#Use the mean() method to calculate the average of the values in alcohol_consumption. Assign the result to average_alcohol.

alcohol_consumption = world_alcohol[:,4].astype(float)
print(alcohol_consumption)

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

print(total_alcohol)
print(average_alcohol)




print("\n"*6)

world_alcohol = numpy.array([['1986', 'Western Pacific', 'Canada', 'Wine', '2'],
                           ['1986', 'Americas', 'Canada', 'Other', ''],
                           ['1985', 'Africa', "Cte d'Ivoire", 'Wine', '1.62'],
                           ['1986', 'Europe', 'Switzerland', 'Spirits', '2.54'],
                           ['1986', 'Europe', 'Switzerland', 'Spirits', '2.54'],
                           ['1987', 'Western Pacific', 'Papua New Guinea', 'Other', '0'],
                           ['1987', 'Western Pacific', 'Papua New Guinea', 'Other', ''],
                           ['1986', 'Africa', 'Algeria', 'Other', '5.15']])



#Create a matrix called canada_1986 that only contains the rows in world_alcohol where the first column is the string 1986 and the third column is the string Canada.
#Extract the fifth column of canada_1986, replace any empty strings ('') with the string 0, and convert the column to the float data type. Assign the result to canada_alcohol.
#Compute the sum of canada_alcohol. Assign the result to total_canadian_drinking.

canada_1986 = world_alcohol[((world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada')),:]
print(canada_1986)

is_empty = (canada_1986[:,4] == '')
print(is_empty)
canada_1986[is_empty,4] = '0'
print(canada_1986)
canada_alcohol = canada_1986[:,4].astype(float)
print(canada_alcohol)

total_canadian_drinking = canada_alcohol.sum()
print(total_canadian_drinking)






print("\n"*6)

world_alcohol = numpy.array([['1989', 'Western Pacific', 'Canada', 'Wine', '2'],
                           ['1989', 'Americas', 'Canada', 'Other', ''],
                           ['1989', 'Africa', "Cte d'Ivoire", 'Wine', '1.62'],
                           ['1989', 'Europe', 'Switzerland', 'Spirits', '2.54'],
                           ['1989', 'Europe', 'Switzerland', 'Spirits', '2.54'],
                           ['1989', 'Western Pacific', 'Papua New Guinea', 'Other', '0'],
                           ['1989', 'Western Pacific', 'Papua New Guinea', 'Other', ''],
                           ['1989', 'Africa', 'Algeria', 'Other', '5.15']])

countries = world_alcohol[:,2]
print(countries)
totals = {}
world_alcohol_1989 = world_alcohol[(world_alcohol[:,0] == '1989'),:]
world_alcohol_1989[(world_alcohol_1989[:,4] == ''),4] = 0
print(world_alcohol_1989)

print(world_alcohol_1989)

for c in countries:
    print(c)
    country_alcohol = world_alcohol_1989[(world_alcohol_1989[:,2] == c),:]
    consumption = country_alcohol[:,4].astype(float)
    totals[c] = consumption.sum()

print(totals)





print("\n"*6)


highest_value = 0
highest_key = None

for key in totals:
    value = totals[key]
    if value > highest_value:
        highest_value = value
        highest_key = key

print(highest_key)
print(highest_value)





print("\n"*6)


















