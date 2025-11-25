# Hiding complexity and showing only the necessary details.
# Use abc module:

class Aditya():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # private attribute
    
    def show_details(self):
        print("User Details...")
        print("Name:", self.name)
        print("Age:", self.age)

user = Aditya("Aditya", 24, 50000)
user.show_details()