import numpy

vector = numpy.array([5,10,15,20])
print(vector == 10)
print(vector * 2)
print(vector + 2)


#world_alcohol = numpy.genfromtxt("world_alcohol.csv", dtype="U75", skip_header=True, delimiter=",")

print "\n"*6

world_alcohol = numpy.array([['1986', 'Western Pacific', 'Viet Nam', 'Wine', '0'],
                           ['1986', 'Americas', 'Uruguay', 'Other', '0.5'],
                           ['1985', 'Africa', "Cte d'Ivoire", 'Wine', '1.62'],
                           ['1986', 'Europe', 'Switzerland', 'Spirits', '2.54'],
                           ['1987', 'Western Pacific', 'Papua New Guinea', 'Other', '0'],
                           ['1986', 'Africa', 'Swaziland', 'Other', '5.15']])

print(world_alcohol[:,2])
countries_canada = (world_alcohol[:,2] == 'Canada')
print(countries_canada)

print("\n"*2)
print(world_alcohol[:,0])
# if I use:
# print(world_alcohol[:,0:1])
# it will return an array 2 D, wrong for this exercise.
years_1984 = (world_alcohol[:,0] == '1984')
print(years_1984)
