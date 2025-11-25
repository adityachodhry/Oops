# One class can inherit properties of another.

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of Parent
        self.age = age

    def introduce(self):
        parent_greeting = self.greet()  # Call method from Parent
        return f"{parent_greeting} I am {self.age} years old."


# Create an instance of Child
child_instance = Child("Aditya", 10)
print(child_instance.introduce())