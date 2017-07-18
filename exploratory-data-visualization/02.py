
# https://www.dataquest.io/m/143/multiple-plots

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("unrate.csv")

unrate["DATE"] = pd.to_datetime(unrate["DATE"])

x_values = unrate["DATE"][:12]
y_values = unrate["VALUE"][:12]

plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.plot(x_values, y_values)
plt.show()


#################################
print("\n"*3)


import matplotlib.pyplot as plt
fig = plt.figure()
#axes_obj = fig.add_subplot(nrows, ncols, plot_number)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()


#################################
print("\n"*3)


x_values_1948 = unrate["DATE"][:12]
y_values_1948 = unrate["VALUE"][:12]

x_values_1949 = unrate["DATE"][12:24]
y_values_1949 = unrate["VALUE"][12:24]

print(x_values_1949)

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(x_values_1948, y_values_1948)
ax2.plot(x_values_1949, y_values_1949)
plt.show()


#################################
print("\n"*3)


#fig = plt.figure(figsize=(width, height))
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(x_values_1948, y_values_1948)
ax2.plot(x_values_1949, y_values_1949)
plt.show()


#################################
print("\n"*3)


fig = plt.figure(figsize=(12,12))

def plotData(yearNumber, figg):
    x_values = unrate["DATE"][yearNumber*12:(yearNumber+1)*12]
    y_values = unrate["VALUE"][yearNumber*12:(yearNumber+1)*12]

    ax = figg.add_subplot(5,1,(yearNumber+1))
    
    ax.plot(x_values, y_values)

plotData(0, fig)
plotData(1, fig)
plotData(2, fig)
plotData(3, fig)
plotData(4, fig)

plt.show()



#################################
print("\n"*3)






