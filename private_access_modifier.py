class MyClass:
    def __init__(self, value):
        self.__value = value  # Private attribute

    def __show_value(self):
        print(self.__value)  # Private method

    def public_method(self):
        self.__show_value()  # Accessing the private method within the class


obj = MyClass(30)
obj.public_method()  # This works and calls the private method internally

# Direct access to private members will fail
# print(obj.__show_value())  # AttributeError: 'MyClass' object has no attribute '__show_value'
# print(obj.__value)  # AttributeError: 'MyClass' object has no attribute '__value'

# However, you can access private members using name mangling
print(obj._MyClass__value)  # Accessing private attribute through name mangling
