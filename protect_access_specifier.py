class MyClass:
    def __init__(self, value):
        self._value = value  # Protected attribute

    def _show_value(self):
        print(self._value)  # Protected method


class SubClass(MyClass):
    def display(self):
        self._show_value()  # Accessing a protected method in a subclass


obj = SubClass(20)
obj.display()
print(obj._value)  # Accessing a protected attribute (though not recommended)
