import pandas as pd

unrate = pd.read_csv("unrate.csv")

print(unrate.head(4))

unrate['DATE'] = pd.to_datetime(unrate['DATE'])

print(unrate.head(12))


print('\n'*4)
#############################



import matplotlib.pyplot as plt

# create a plot using data
# customize the appearance of the plot
# display the plot
# edit and repeat until satisfied

# plt.plot()
# plt.show()


print('\n'*4)
#############################

x_values = unrate['DATE'][:12]
y_values = unrate['VALUE'][:12]

print("x values: ")
print(x_values)

print("y values:")
print(y_values)

plt.xticks(rotation=90)
plt.title("Monthly Unemployment Trends, 1948")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.plot(x_values, y_values)
plt.show()








