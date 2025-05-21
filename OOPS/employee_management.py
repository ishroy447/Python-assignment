class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Department: {self.department}, Salary: ${self.salary}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if employee.department == self.name:
            self.employees.append(employee)
            return f"Employee {employee.name} added to {self.name} department"
        return f"Employee {employee.name} does not belong to {self.name} department"

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return f"Employee {employee.name} removed from {self.name} department"
        return "Employee not found in this department"

    def list_employees(self):
        return self.employees

    def get_department_salary(self):
        return sum(employee.salary for employee in self.employees)

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department
        return f"Department {department.name} added to company"

    def add_employee(self, employee):
        if employee.department in self.departments:
            return self.departments[employee.department].add_employee(employee)
        return f"Department {employee.department} does not exist"

    def get_department_employees(self, department_name):
        if department_name in self.departments:
            return self.departments[department_name].list_employees()
        return []

# Example usage
if __name__ == "__main__":
    # Create a company
    company = Company("Tech Corp")
    
    # Create departments
    it_dept = Department("IT")
    hr_dept = Department("HR")
    finance_dept = Department("Finance")
    
    company.add_department(it_dept)
    company.add_department(hr_dept)
    company.add_department(finance_dept)
    
    # Create employees
    emp1 = Employee("E001", "John Doe", 30, "IT", 80000)
    emp2 = Employee("E002", "Jane Smith", 28, "HR", 65000)
    emp3 = Employee("E003", "Bob Johnson", 35, "IT", 90000)
    emp4 = Employee("E004", "Alice Brown", 32, "Finance", 75000)
    
    # Add employees to company
    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)
    company.add_employee(emp4)
    
    # Display employees in IT department
    print("\nIT Department Employees:")
    for employee in company.get_department_employees("IT"):
        print(employee)
    
    # Display employees in HR department
    print("\nHR Department Employees:")
    for employee in company.get_department_employees("HR"):
        print(employee)
    
    # Display employees in Finance department
    print("\nFinance Department Employees:")
    for employee in company.get_department_employees("Finance"):
        print(employee) 