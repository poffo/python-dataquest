import pandas

food_info = pandas.read_csv("food_info.csv")

print(food_info.columns.tolist())

col_names = food_info.columns.tolist()

print("\n"*3)

print(col_names[0:3])



print("\n"*3)
print("\n"*3)
print("\n"*3)


#dividing every value in the column by 100 and returning a new serie
div_1000 = food_info["Iron_(mg)"] / 1000


sodium_grams = food_info["Sodium_(mg)"] / 1000
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000



print("\n"*3)
print("\n"*3)
print("\n"*3)

grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]

weighted_protein = food_info["Protein_(g)"] * 2
weighted_fat = food_info["Lipid_Tot_(g)"] * -.75
initial_rating = weighted_protein + weighted_fat


print("\n"*3)
print("\n"*3)
print("\n"*3)


normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()


print("\n"*3)
print("\n"*3)



food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat



print("\n"*3)
print("\n"*3)


#it's already normalized, since I am making all operation with normalized data
food_info["Norm_Nutr_Index"] = (food_info["Normalized_Protein"] *2) + (food_info["Normalized_Fat"]*-.75)



print("\n"*3)
print("\n"*3)


# inplace parameter make the sort and auto assign the new dataframe
food_info.sort_values("Norm_Nutr_Index", inplace=True, ascending=False)

print(food_info)

