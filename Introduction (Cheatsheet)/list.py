from pyrsistent import m


my_list = ['dog', 'cat', 'tiger', 'wolf']

print(my_list[0])  # first
print(my_list[-1])  # last
print(my_list[0:2])  # first and second
print(my_list[:2])  # until second
print(my_list[0:2] == my_list[:2])
print(my_list[0:2] is my_list[:2])
print(my_list[0:-1])  # until second last
print(my_list[1:])  # skip first

print("*" * 30)

# To copy list, just slice the entire list

# copy by address
my_list2 = my_list  # address assignment
print(my_list == my_list2)
print(my_list is my_list2)
my_list2.append('dragon')
print(my_list)

# copy entire list
my_list3 = my_list[:]  # list copy (new address)
print(my_list == my_list3)
print(my_list is my_list3)
my_list3.append('monkey')
print(my_list)
print(my_list3)

my_list[0] = 'doggy'
print(my_list2)

# concat and replication
print(my_list + my_list)
print(my_list * 2)
print(my_list + my_list == my_list * 2)
print(my_list + my_list is my_list * 2)

# deletion
del my_list[-1]
print(my_list2)

# loop through list
for i, animal in enumerate(my_list):
    print('At index {} is {}'.format(str(i), animal))

# loop through multiple lists
my_list4 = ['dog food', 'cat food', 'meattt', 'meatttttt']

for animal, food in zip(my_list, my_list4):
    print('{} eats {}'.format(animal, food))

# in and not in
print('dog' in my_list)
print('dog' not in my_list)
print('doggy' in my_list)

# assignment shortcut
animal1, animal2 = my_list[:2]
print(animal1, animal2)

animal3, animal4 = ['cat', 'dog']
print(animal3, animal4)

# swap
animal3, animal4 = animal4, animal3
print(animal3, animal4)

# finding index
print(my_list.index('doggy'))

# insert
my_list.insert(-1, 'fire')
print(my_list)

# remove
my_list.remove(my_list[-2])
print(my_list)

# destructure strings
print(list('hello'))

# tuples
print(tuple(my_list))
