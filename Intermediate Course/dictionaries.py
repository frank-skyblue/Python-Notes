# Dictionary: Key-value pairs, unordered, mutable
myDict = {"Hello": "World", "Year": 2022}

# Adding pairs
myDict["email"] = "email@email.com"

# Deleting pairs
del myDict["Hello"]
myDict.pop()

# Can check for membership or iterate over
for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, value)
