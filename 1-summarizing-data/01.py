import pandas

all_ages = pandas.read_csv("all-ages.csv")
recent_grads = pandas.read_csv("recent-grads.csv")

# Use the Total column to calculate the number of people who fall under each Major_category in each data set.
# Store the result as a separate dictionary for each data set.
# The key for the dictionary should be the Major_category, and the value should be the total count.
# For the counts from all_ages, store the results as a dictionary named aa_cat_counts.
# For the counts from recent_grads, store the results as a dictionary named rg_cat_counts.

unique_major = all_ages["Major_category"].unique()

aa_cat_counts = {}
rg_cat_counts = {}

for u in unique_major:
    all_ages_category = all_ages["Major_category"] == u
    aa_cat_counts[u] = all_ages["Total"][all_ages_category].sum()

    recent_grads_category = recent_grads["Major_category"] == u
    rg_cat_counts[u] = recent_grads["Total"][recent_grads_category].sum()

    
# Use the Low_wage_jobs and Total columns to calculate the proportion of recent college graduates that worked low wage jobs.
# Recall that you can use the Series.sum() method to return the sum of the values in a column.
# Store the resulting float as low_wage_percent, and display the value with the print() function.

low_wage_percent = (recent_grads["Low_wage_jobs"].sum() / recent_grads["Total"].sum())

print(low_wage_percent)




# Use a for loop to iterate over majors.
# For each major, use Boolean filtering to find the corresponding row in both DataFrames.
# Compare the values for Unemployment_rate to see which DataFrame has a lower value.
# Increment rg_lower_count if the value for Unemployment_rate is lower for recent_grads than it is for all_ages.
# Display rg_lower_count with the print() function.

major_code = recent_grads["Major_code"].unique()
rg_lower_count = 0

for m in major_code:
    rg_filter = recent_grads["Major_code"] == m
    aa_filter = all_ages["Major_code"] == m
    
    rg_unemployment_sum = recent_grads["Unemployment_rate"][rg_filter].sum()
    aa_unemployment_sum = all_ages["Unemployment_rate"][aa_filter].sum()
    
    if rg_unemployment_sum  < aa_unemployment_sum:
        rg_lower_count = rg_lower_count + 1



print(rg_lower_count)






