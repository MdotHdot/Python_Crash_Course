#this program defines an Employee class with methods to calculate annual salary and apply a raise
class Employee:
    def __init__(self,first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12
    
    def give__default_raise(self):
        self.monthly_salary += 5000
        
    def give_custom_raise(self, amount):
        self.monthly_salary += amount
        
        

    # def apply_raise(self, percentage):
    #     self.monthly_salary += self.monthly_salary * (percentage / 100)