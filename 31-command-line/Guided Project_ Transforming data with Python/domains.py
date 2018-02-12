import read

data = read.load_data()

# removing subdomains
# more than 2 dots

def remove_subdomain(row):
    #print(row)
    domainComponents = str(row).split('.')
    #print(domainComponents)
    row = domainComponents[len(domainComponents)-2] + "." + domainComponents[len(domainComponents)-1]
    #print(row)
    return row


data['url'] = data['url'].apply(remove_subdomain)
domains = data["url"].value_counts()

domains = domains.head(15)
print(domains.head(100))

for index, row in domains.items():
    print("{0}: {1}".format(index, row))

