'''
Create a Employee Class
'''
class Employee():

# Define the details for the Employee class
    def __init__(self, name,dob,emp_id):
        self.name = name
        self.dob = dob
        self.id = emp_id


# Add a __str__ method to give a Human readable desciption of the class. 
    def __str__(self):
        return "This is the Employee Class __str__"

# Add a __repr__ method to return the Class used to create the object
    def __repr__(self):    
        return "Employee(self, name,dob,emp_id)"

# Method to display the Employee's information

    def display(self):
        print('\n') # Inserts new line.
        print("The Employee's name is: " + self.name)
        print("The Employee's date of Birth is " + self.dob)
        print("The Employee's ID is " + self.id)
        print("\n")

