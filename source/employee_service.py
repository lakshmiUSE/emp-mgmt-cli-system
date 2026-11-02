
import uuid
from .validators import validate_employee_data
from .import repository

from .exceptions import DuplicateEmployeeError

def add_employee(employee_data):
    """
    Add a new employee after validating details and checking duplicate emails

    Args:
        employee_data (dict): Employee details

    Returns:
        dict: Newly added employee details

    Raises:
        DuplicateEmployeeError: If the email already exists
    """
     
    employee=validate_employee_data(employee_data)
    employees=repository.load_employees()

    for emp in employees:
        if emp["email"].lower()==employee["email"].lower():
             raise DuplicateEmployeeError("Email already exists")

    employee["employee_id"] = str(uuid.uuid4())
    repository.insert_employee(employee)
    return employee

def search_employees(search_term):
    """
    Search for employees by name.

    Args:
        search_term (str): Employee name or search keyword.

    Returns:
        list or str: List of matching employee records or
                     "Employee not found" if no match exists.
    """
    employees = repository.load_employees()
    result = []

    for emp in employees:
        if search_term.lower() in emp["name"].lower():
            result.append(emp)
    if result:
     return result
    else:
     return "Employee not found"
                  