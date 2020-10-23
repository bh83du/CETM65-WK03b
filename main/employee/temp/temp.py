'''
Create a Sub Class of Employee for Temporary Employees
'''
# Need to add Decoraters and Properties tags.  Must be clearner way to do it.
class Temporary(Employee):

    number_of_temp_emp = 0  # Class variable to allow tracking of number of Employees

    def __init__(self, name, dob, emp_id):
        super().__init__(name, dob, emp_id) # Attributes inherited from Employee Class
        self.hourlyrate = None              # Hourly Rate specific to Temporary Class
        self.weeklyhours = None             # Weekly Hours specific to Temporary Class
        self.tgp = None                     # Temporary Gross Weekly Pay
        Temporary.number_of_temp_emp = Temporary.number_of_temp_emp + 1  # Add to running total of Temporary Employees

# Add a __str__ method to give a Human readable desciption of the class. 

    def __str__(self):
        return "This is the Temporary Employee Class __str__method"

# Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Temporary(self, name,dob,emp_id)"

# Method to calculate the gross weekly wage of the Employee

    def salary_info(self):
        self.tgp = (self.hourlyrate * self.weeklyhours)
        print('\n')
        print(f'Contract Type is Temporary')
        print(f'Employee hourly rate is: £{self.hourlyrate}')
        print(f'Employee contracted weekly hours are: {self.weeklyhours} hours')
        print(f'Employee gross weekly salary is: £{self.tgp}')

        
