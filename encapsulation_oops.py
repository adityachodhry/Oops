# Encapsulation means protecting data by restricting access.
# Python uses:
# Public variables → accessible everywhere
# Protected variables (_var) → suggest internal use
# Private variables (__var) → name-mangled

class Aditya():
    def __init__(self, name, age, salary):
        self.name = name          # public attribute
        self._age = age          # protected attribute
        self.__salary = salary    # private attribute
    
    def show_details(self):
        print("User Details...")
        print("Name:", self.name)
        print("Age:", self._age)
        print("Salary:", self.__salary)  # Accessing private attribute within class

user = Aditya("Aditya", 24, 50000)
user.show_details()