
from source.exceptions import ValidationError
from source import employee_service

def display_menu():
    """Display the employee mangement menu"""
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Search Employee")

while True:
 display_menu()
 choice = input("Enter your choice: ")

 if choice == "1":
        data = {
            "name": input("Enter name: "),
            "email": input("Enter email: "),
            "department": input("Enter department: "),
            "salary": float(input("Enter salary: ")),
            "joining_date": input("Enter joining date (YYYY-MM-DD): "),
            "status": input("Enter status: ")
        }

        try:
            employee = employee_service.add_employee(data)
            print(employee)
        except ValidationError as e:
            print(e)
 
 elif choice == "2":
        search = input("Enter employee name: ")
        result = employee_service.search_employees(search)
        print(result)