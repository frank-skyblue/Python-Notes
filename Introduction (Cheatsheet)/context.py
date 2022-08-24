with open('test.txt', 'r') as file:
    print(file.read())

# is equivalent to

file = open('test.txt', 'r')
try:
    print(file.read())
finally:
    file.close()

##############################################
# to define our own context manager, we must define __enter__ and __exit__ methods


class MyContextManager(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with MyContextManager('test.txt', 'r') as file:
    print(file.read())
