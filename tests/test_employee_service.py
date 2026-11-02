import pytest

from source.employee_service import (
    add_employee,
)

from source.exceptions import ( DuplicateEmployeeError)


def test_add_employee():
   
    employee = {
        "name": "Rajesh",
        "email": "rameh1283@email.com",
        "department": "IT",
        "salary": "25000",
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    assert add_employee(employee)

def test_duplicate_email():
  
    employee = {
        "name": "Rajesh",
        "email": "rajesh9123gmail.com",
        "department": "IT",
        "salary": 25000,
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    add_employee(employee)

    with pytest.raises(DuplicateEmployeeError):
        add_employee(employee)
