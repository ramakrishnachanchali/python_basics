class MyClass:
    def __init__(self, value):
        self.value = value  # Public attribute

    def show_value(self):
        print(self.value)  # Public method


obj = MyClass(10)
obj.show_value()  # Accessing a public method
print(obj.value)  # Accessing a public attribute
