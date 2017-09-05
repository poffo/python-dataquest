import numpy

world_alcohol = numpy.genfromtxt("world_alcohol.csv", dtype="U75", skip_header=True, delimiter=",")

print(world_alcohol)

total_people = 0
total_drank = 0

for item in world_alcohol:
    if int(item[0]) == 1986 and item[2] == 'Uruguay' and item[3] == 'Other':
        total_people = total_people + 1
        total_drank = total_drank + float(item[4])

uruguay_other_1986 = total_drank/total_people
uruguay_other_1986 = '0.5'

third_country = world_alcohol[2][2]
