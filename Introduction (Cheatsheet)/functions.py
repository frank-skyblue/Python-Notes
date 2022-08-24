def spam():
    global my_var  # global variables can be changed with global keyword
    my_var = 'world'


my_var = 'hello'
print(my_var)
spam()
print(my_var)
