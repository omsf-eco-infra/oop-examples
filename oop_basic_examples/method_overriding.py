class Parent:
    def show(self):
        return "Parent method"


class Child(Parent):
    def show(self):
        return "Child method - overridden"


# Usage
parent = Parent()
child = Child()
print(parent.show())  # Parent method
print(child.show())  # Child method - overridden
