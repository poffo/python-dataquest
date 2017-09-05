import pandas

passenger_classes = [1, 2, 3]
fares_by_class = {}

titanic_survival = pandas.read_csv("titanic_survival.csv")

for n in passenger_classes:
    fare_class = titanic_survival["pclass"] == n
    fare = titanic_survival["fare"][fare_class]
    print(fare)
    fares_by_class[n] = fare.mean()