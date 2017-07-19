
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


unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6,3))

x_values_1948_t = unrate["MONTH"][:12]
y_values_1948_t = unrate["VALUE"][:12]
x_values_1949_t = unrate["MONTH"][12:24]
y_values_1949_t = unrate["VALUE"][12:24]

#plt.xlabel("Month")
#plt.ylabel("Inemployment Rate")
#plt.title("Monthly Unemployment Trends, 1948/49")

plt.plot(x_values_1948_t, y_values_1948_t, c='red')
plt.plot(x_values_1949_t, y_values_1949_t, c='blue')
plt.show()


#################################
print("\n"*3)

fig = plt.figure(figsize=(10,6))

def plotMultipleLines(yearNumber, colorYear):
    x_values_year_t = unrate["MONTH"][(12*yearNumber):(12*(yearNumber+1))]
    y_values_year_t = unrate["VALUE"][(12*yearNumber):(12*(yearNumber+1))]

    plt.plot(x_values_year_t, y_values_year_t, color=colorYear)

plotMultipleLines(0, 'red')
plotMultipleLines(1, 'blue')
plotMultipleLines(2, 'green')
plotMultipleLines(3, 'orange')
plotMultipleLines(4, 'black')

plt.show()



#################################
print("\n"*3)


# Modify the code from the last screen that overlaid 5 plots to include a legend. Use the year value for each line chart as the label.
# E.g. the plot of 1948 data that uses "red" for the line color should be labeled "1948" in the legend.
# Place the legend in the "upper left" corner of the plot.
# Display the plot using plt.show().


unrate['YEAR'] = unrate['DATE'].dt.year


fig = plt.figure(figsize=(10,6))

def plotMultipleLines(yearNumber, colorYear):
    x_values_year_t = unrate["MONTH"][(12*yearNumber):(12*(yearNumber+1))]
    y_values_year_t = unrate["VALUE"][(12*yearNumber):(12*(yearNumber+1))]

    plt.plot(x_values_year_t, y_values_year_t, color=colorYear, label=unrate['YEAR'][12*yearNumber])

plotMultipleLines(0, 'red')
plotMultipleLines(1, 'blue')
plotMultipleLines(2, 'green')
plotMultipleLines(3, 'orange')
plotMultipleLines(4, 'black')

plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.legend(loc='upper left')

plt.show()


#################################
print("\n"*3)


