
import pytest

from source.validators import validate_name,validate_email,validate_salary,validate_department,validate_joining_date,validate_status,validate_employee_data
from source.exceptions import ValidationError

def test_valid_name():
    
    assert validate_name("rajesh")

def test_invalid_name():
    
    with pytest.raises(ValidationError):
        validate_name("")

def test_valid_email():

    assert validate_email("rajesh123@gmail.com")

def test_invalid_email():
  
    with pytest.raises(ValidationError):
        validate_email("rajesh123gmail.com")

def test_valid_salary():
  
    assert validate_salary("2300")

def test_invalid_salary():
    
    with pytest.raises(ValidationError):
        validate_salary("-100")

def test_valid_department():

    assert validate_department("IT")

def test_invalid_department():
   
    with pytest.raises(ValidationError):
        validate_department("Marketing")

def test_valid_joiningdata():

    assert validate_joining_date("2026-10-22")
@pytest.mark.xfail()
def test_invalid_joiningdata():
   
    with pytest.raises(ValidationError) :                              
        validate_joining_date("22-10-2003")
@pytest.mark.status()
def test_valid_status():

    assert validate_status("Active")
@pytest.mark.status()
def test_invalid_status():
  
    with pytest.raises(ValidationError):
        validate_status("inactive")


def test_valid_employee_data():
  
    employee = {
        "name": "Rajesh",
        "email": "rajesh@gmail.com",
        "department": "IT",
        "salary": "25000.0",
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    assert validate_employee_data(employee) 


def test_invalid_employee_data():
  
    employee = {
        "name": "",
        "email": "rajesh@gmail.com",
        "department": "IT",
        "salary": 25000,
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    with pytest.raises(ValidationError):
        validate_employee_data(employee)
       
