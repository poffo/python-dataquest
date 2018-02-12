import read
from collections import Counter

df = read.load_data()
all_headline = ""

for index, row in df.iterrows():
    all_headline += str(row["headline"]).lower()
    all_headline += " "


print(all_headline)
list_strings = all_headline.split(" ")
print("List of words:  " + str(len(list_strings)))
print("List unique words: " + str(len(set(list_strings))))

counter = Counter(list_strings)

print("Most common: " + str(counter.most_common(100)))
