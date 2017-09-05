'''
- Import scatter_matrix from pandas.tools.plotting
- Create a 2 by 2 scatter matrix plot using the Sample_size and Median columns.
- Create a 3 by 3 scatter matrix plot using the Sample_size, Median, and Unemployment_rate columns.
- Explore the questions from the last few steps using these scatter matrix plots. You may need to create more scatter matrix plots.
'''

import pandas as pd
import matplotlib.pyplot as plt

import pandas.plotting as plotting

# Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
recent_grads = pd.read_csv("recent-grads.csv")

plotting.scatter_matrix(recent_grads[["Sample_size", "Median"]], figsize=(10,10))
plt.show()

plotting.scatter_matrix(recent_grads[["Sample_size", "Median", "Unemployment_rate"]])
plt.show()
