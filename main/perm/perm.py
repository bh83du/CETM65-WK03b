'''
Create a Sub Class of Employee for Permanent Employees
'''
# Import base class from Employee

from employee.employee import Employee


# Need to add Decoraters and Properties tags.  Must be clearner way to do it.
class Permanent(Employee):

    number_of_perm_emp = 0 # Class variable to allow tracking of number of Employees


    def __init__(self, name, dob, emp_id, ):
        super().__init__(name, dob, emp_id) # Attributes inherited from Employee Class
        self.annualsalary = None            # Annual Salary specific to Permanent Class
        self.pensionplan = None             # Pension Plan Status for Permanent Class
        self.pgp = None                     # Permanent Gross Weekly Pay
        # Increment the number of permanent employees by 1
        Permanent.number_of_perm_emp = Permanent.number_of_perm_emp + 1

# Add a __str__ method to give a Human readable desciption of the class. 

    def __str__(self):
        return "This is the Permanent Employee Class __str__ method"

# Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Permanent(self, name,dob,emp_id)"

# Add a method to calculate the Permanent Gross Weekly salary
    def salary_info(self):
        self.pgp = (self.annualsalary / 52)
        print('\n')
        print(f'Contract Type is Permanent')
        print(f'Employee Annual Salary is: £{self.annualsalary}')
        print(f'Employee Pension Scheme Status: {self.pensionplan}')
        print(f'Employee gross weekly salary is: £{self.pgp}')
