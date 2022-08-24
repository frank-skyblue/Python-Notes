# Lists: ordered, mutable, allows duplicate

# Creating a list
myList = [True, 2, "Hello"]

# Indexing
myBool = myList[0]

# Iterate over lists
for item in myList:
    print(item)

# Check membership
if "Hello" in myList:
    print(True)

# Inserting
myList.append("World")  # At end
myList.insert(0, "Start")  # At start

# Removing
myList.pop()  # At end
myList.pop(0)  # At first
myList.remove("Hello")  # Remove specific item
myList.clear()  # Remove all

# Tuples: ordered, immutable, and allows duplicate
myTuple = ("Hello", "World")
