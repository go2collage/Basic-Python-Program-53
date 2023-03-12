# Python Program

# Simple Inheritance

# Create Class

# Super / Parent class
class Student():

    # Attribute of Parent Class
    name = ""
    address = ""
    marks = None

    # Define Method
    def aboutME(self):
        print("I have studying in 10th Standard.")
    
# Subclass
class Class_10th(Student):
    # Subclass Method
    def display(self):
        print("Student Details")
        print("Student Name: ", self.name)
        print("Student Address: ", self.address)
        print("Student Marks: ", self.marks)

# Create object
obj = Class_10th()

# Superclass attributes & methods
obj.name = "Rahul Raj"
obj.address = "Pune, India"
obj.marks = 92

obj.aboutME()

# Subclass Method
obj.display()


# Thanks for Watching
