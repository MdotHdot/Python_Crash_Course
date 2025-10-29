#tests the employee class and the give_raise method
import pytest
from employee import Employee  

def test_annual_salary():
    emp = Employee('John', 'Doe', 4000)
    assert emp.annual_salary() == 48000 
    
def test_give_default_raise():
    emp = Employee('Jane', 'Smith', 3000)
    emp.give__default_raise()
    assert emp.monthly_salary == 8000 
    
def test_give_custom_raise():
    emp = Employee('Alice', 'Johnson', 3500)
    emp.give_custom_raise(2000)
    assert emp.monthly_salary == 5500