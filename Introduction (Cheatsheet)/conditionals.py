print(42 == 42)  # comparison between value
a = 42
b = 42
print(a is b)  # comparison between address
print(42 is not 43)

# While loop and break/continue
# while True:
while False:
    print("Type frank")
    name = input()
    if name == "frank":
        break
    elif name == "mike":
        break
    else:
        continue  # return to beginning
    print("should not be reached")

for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

container = ["apple", "carrot"]
for item in container:
    if (item == "bananas"):
        print("Found items!")
        break
else:
    print("Did not find item")
    print("For loop has fully executed (did not break)")
