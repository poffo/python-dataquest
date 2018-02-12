import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv")

print(data.head(4))

print("###########")

print(data[["TOT_ENR_M", "TOT_ENR_F"]].head(5))

print("###########")

      
#print(list(data.columns.values))


data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]


print(data[["TOT_ENR_M", "TOT_ENR_F", "total_enrollment"]].head(5))

columns = ["SCH_ENR_HI_M","SCH_ENR_HI_F","SCH_ENR_AM_M","SCH_ENR_AM_F","SCH_ENR_AS_M","SCH_ENR_AS_F","SCH_ENR_HP_M","SCH_ENR_HP_F","SCH_ENR_BL_M","SCH_ENR_BL_F","SCH_ENR_WH_M","SCH_ENR_WH_F","SCH_ENR_TR_M","SCH_ENR_TR_F"]

#data["total_enrollment"] = data["total_enrollment"] + data["SCH_ENR_HI_M"] + data["SCH_ENR_HI_F"] + data["SCH_ENR_AM_M"] + data["SCH_ENR_AM_F"] + data["SCH_ENR_AS_M"] + data["SCH_ENR_AS_F"] + data["SCH_ENR_HP_M"] + data["SCH_ENR_HP_F"] + data["SCH_ENR_BL_M"] + data["SCH_ENR_BL_F"] + data["SCH_ENR_WH_M"] + data["SCH_ENR_WH_F"] + data["SCH_ENR_TR_M"] + data["SCH_ENR_TR_F"]

for c in columns:
    data["total_enrollment"] += data[c]

all_enrollment = data["total_enrollment"].sum()
print(all_enrollment)

for c in columns:
    print("percentage for '" + c + "': " + str((data[c].sum() / all_enrollment)*100) + ", total sum: " + str(data[c].sum()))

