from .exceptions import ValidationError
from config.config import ALLOWED_DEPARTMENTS, ALLOWED_STATUSES, DATE_FORMAT
from datetime import datetime
import re
def validate_name(name):

    """
    Validate and return the employee's full name

    Args:
        name (str): Employee's full name

    Returns:
        str: Validated employee name without extra spaces

    Raises:
        ValidationError: If the name is missing or not a string
    """
    if not isinstance(name,str) or not name.strip():
      raise ValidationError("Full name is requried")
    return name.strip() 

def validate_email(email):
    """
      Validate and return the employee's email address.

     Args:
        email (str): Employee's email address.

     Returns:
        str: Validated email address.

     Raises:
        ValidationError: If the email is missing or invalid.
    """
    if not isinstance(email,str) or not email.strip():
        raise ValidationError(" email is requried")
   
    email= email.strip()
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern,email):
       raise ValidationError("Please enter a valid email address")
   
    return email

def validate_salary(salary):
    """
    Validate and return the employee's salary.

    Args:
        salary (float): Employee's salary.

    Returns:
        float: Validated salary amount.

    Raises:
        ValidationError: If the salary is invalid or less than or equal to zero.
    """
    if  isinstance(salary,bool):
        raise ValidationError("salary must be valid number")
    

    try:
        salary = float(salary)
    except (ValueError, TypeError):
        raise ValidationError("Salary must be a valid number.")

    if salary <= 0:
        raise ValidationError("Salary must be greater than zero.")

    return salary

def validate_department(department):
    """
    Validate and return the employee's department.

    Args:
        department (str): Employee's department.

    Returns:
        str: Validated department name.

    Raises:
        ValidationError: If the department is missing or not allowed.
    """
    if not isinstance(department,str) or not department.strip():
        raise ValidationError("Department is required")

    department = department.strip()

    if department not in ALLOWED_DEPARTMENTS:
        raise ValidationError(
            f"Choose a department from: {', '.join(ALLOWED_DEPARTMENTS)}"
        )

    return department

def validate_joining_date(joining_data):
    """
    Validate the employee's joining date.

    Args:
        joining_data (str): Employee's joining date.

    Returns:
        str: Validated joining date.

    Raises:
        ValidationError: If the joining date is missing or invalid.
    """
    if not isinstance(joining_data,str) or not joining_data.strip():
        raise ValidationError("Joining date is required. Use YYYY-MM-DD")

    try:
         data=datetime.strptime(joining_data,DATE_FORMAT)

         if data.strftime(DATE_FORMAT)!=joining_data:
             raise ValueError
    except ValueError:
        raise  ValidationError(" Invalid joining date. Use YYYY-MM-DD, for example 2026-10-15")

    return joining_data


def validate_status(status):
    """
    Validate and return the employee's employment status.

    Args:
        status (str): Employee's employment status.

    Returns:
        str: Validated employment status.

    Raises:
        ValidationError: If the status is not Active or Inactive.
    """
    if not isinstance(status, str) or status not in ALLOWED_STATUSES:
        raise ValidationError("Status must be Active or Inactive.")

    return status

def validate_employee_data(employee_data):
    """
    Validate all employee information.

    Args:
        employee_data (dict): Employee details to validate.

    Returns:
        dict: Validated employee information.

    Raises:
        ValidationError: If the employee data is invalid.
    """
    if not isinstance(employee_data, dict):
        raise ValidationError("Employee information must be a dictionary.")

    return {
        "name": validate_name(employee_data.get("name")),
        "email": validate_email(employee_data.get("email")),
        "department": validate_department(employee_data.get("department")),
        "salary": validate_salary(employee_data.get("salary")),
        "joining_date": validate_joining_date(
            employee_data.get("joining_date")
        ),
        "status": validate_status(employee_data.get("status", "Active"))
    }

          
        