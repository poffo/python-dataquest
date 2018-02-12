# conditional plots

# Read train.csv into a DataFrame named titanic. Keep only the following columns:
# "Survived"
# "Pclass"
# "Sex"
# "Age"
# "SibSp"
# "Parch"
# "Fare"
# "Embarked"
# Use the DataFrame.dropna() method to remove rows containing missing values.

import pandas as pd

titanic = pd.read_csv("train.csv")

titanic = titanic[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]

titanic.dropna(inplace=True)

print(titanic)


###################################

# Import seaborn as sns and matplotlib.pyplot as plt.
# Use the seaborn.distplot() function to visualize the distribution of the "Age" column.
# Display the plot using pyplot.show().

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv("train.csv")
titanic = titanic[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
titanic.dropna(inplace=True)

sns.distplot(titanic["Fare"])
plt.show()

sns.distplot(titanic["Age"])
plt.show()


###################################

# Generate a kernel density plot:
# Using the values in the "Age" column
# With the area under the curve shaded
# Set the x-axis label to "Age" using pyplot.xlabel().
# KDE: kernel density estimation

sns.kdeplot(titanic["Age"], shade=True)
plt.xlabel("Age")
plt.show()

###################################

# Testing

sns.kdeplot(titanic["Age"], shade=True)
sns.despine(left=True, bottom=True);
plt.xlabel("Age")
plt.show()

###################################

# Set the style to the style sheet that hides the coordinate grid and sets the background color to white.
# Generate a kernel density plot of the "Age" column, with the area under the curve shaded.
# Set the x-axis label to "Age".
# Despine all of the axes.

sns.set_style("white")
sns.kdeplot(titanic["Age"], shade=True)
sns.despine(left=True, bottom=True)
plt.xlabel("Age")
plt.show()

###################################

# Condition on unique values of the "Survived" column.
g = sns.FacetGrid(titanic, col="Survived", size=6)

# For each subset of values, generate a kernel density plot of the "Age" columns.
g.map(sns.kdeplot, "Age", shade=True)
plt.show()

g = sns.FacetGrid(titanic, col="Survived", size=6)
g.map(plt.hist, "Age")
plt.show()

###################################

# Use a FacetGrid instance to generate three plots on the same row:
#   One for each unique value of Pclass.
#   Each plot should be a kernel density plot of the "Age" column, with the area under the curve shaded.
#   Each plot should have a height of 6 inches.
# Remove all of the spines using seaborn.despine().
# Display the plots.

g = sns.FacetGrid(titanic, col="Pclass", size=6)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

###################################

# We can use two conditions to generate a grid of plots, each containing a subset of the data with a unique combination of each condition. When creating a FacetGrid, we use the row parameter to specify the column in the dataframe we want used to subset across the rows in the grid. The best way to understand this is to see a working example.
# 
# The starter code subsets the dataframe on different combinations of unique values in both the Pclass and Survived columns. Try changing the conditions to see the resulting plots.

# Generate the KDE (Kernel Desenty Estimation using both 'validations', Pclass=X and Survived=Y). It will plot all possibilities.

g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

###################################

# Use a FacetGrid instance to generate a grid of plots using the following conditions:
#   The Survived column across the columns in the grid.
#   The Pclass column across the rows in the grid.
#   The Sex column using different hues.
# Each plot should be a kernel density plot of the "Age" column, with the area under the curve shaded.
# Each plot should have a height of 3 inches.
# Remove all of the spines using seaborn.despine().
# Display the plots.

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

###################################

# Use a FacetGrid instance to generate a grid of plots using the following conditions:
#   The Survived column across the columns in the grid.
#   The Pclass column across the rows in the grid.
#   The Sex column using different hues.
# Each plot should be a kernel density plot of the "Age" column, with the area under the curve shaded.
# Each plot should have a height of 3 inches.
# Remove all of the spines using seaborn.despine().
# Add a legend for the Sex column.
# Display the plots.

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex")
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)

###################################
