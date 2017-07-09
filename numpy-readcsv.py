import numpy as py

world_alcohol = py.genfromtxt("world_alcohol.csv",dtype="U75", skip_header=True, delimiter=",")

print(world_alcohol)