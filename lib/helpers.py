from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    if employees:
        print("List of Employees:")
        for emp in employees:
            print(emp) 
    else:
        print("No employees found.")



def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employees = Employee.find_by_name(name)
    if employees:
        print(f"Employees with name '{name}':")
        for emp in employees:
            print(emp)
    else:
        print(f"No employees found with name '{name}'.")


def find_employee_by_id():
    id_ = input("Enter the employee's ID: ")
    if employee := Employee.find_by_id(id_):
        print("Employee found:")
        print(employee)
    else:
        print(f"No employee found with ID '{id_}'.")

def create_employee():
    name = input("Enter the employee's name: ")
    position = input("Enter the employee's position: ")
    salary = input("Enter the employee's salary: ")
    department_id = input("Enter the employee's department ID: ")

    employee = Employee.create(name=name, position=position, salary=salary, department_id=department_id)
    if employee:
        print("Employee created successfully:")
        print(employee)
    else:
        print("Failed to create employee.")

def update_employee():
    id_ = input("Enter the employee's ID to update: ")
    if employee := Employee.find_by_id(id_):
        print("Leave fields blank to keep current value.")
        name = input(f"Enter new name (current: {employee.name}): ") or employee.name
        position = input(f"Enter new position (current: {employee.position}): ") or employee.position
        salary = input(f"Enter new salary (current: {employee.salary}): ") or employee.salary
        department_id = input(f"Enter new department ID (current: {employee.department_id}): ") or employee.department_id

        updated_employee = employee.update(name=name, position=position, salary=salary, department_id=department_id)
        print("Employee updated successfully:")
        print(updated_employee)
    else:
        print(f"No employee found with ID '{id_}'.")

def delete_employee():
    id_ = input("Enter the employee's ID to delete: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f"Employee with ID '{id_}' deleted.")
    else:
        print(f"No employee found with ID '{id_}'.")

def list_employees_in_department():
    department_id = input("Enter the department ID: ")
    employees = Employee.get_by_department(department_id)
    if employees:
        print(f"Employees in Department {department_id}:")
        for emp in employees:
            print(emp)
    else:
        print(f"No employees found in Department {department_id}.")