class Student:
    # __init__ is an constructor runs automatically when an object is created.

    def __init__(self, name, email, username, password, number):
        self.name = name
        self.email = email
        self.username = username
        self.__password = password  # private attribute
        self.number = number

    def display_student_info(self):
        print("Student Information:")
        print("Name:", self.name)
        print("Age:", self.email)
        print("Username:", self.username)
        print("Contact Number:", self.number)

# Create a student object
name = str(input("Enter your name: "))
email = str(input("Enter your email ID: "))
username = input("Enter your username: ")
password = input("Enter your password: ")
number = int(input("Enter your contact number: "))

student1 = Student(name, email, username, password, number)

# Display student information
student1.display_student_info()