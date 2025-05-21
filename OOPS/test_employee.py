from employee_management import Employee, Department, Company

def test_employee_management():
    # Create a company
    company = Company("Test Corp")
    
    # Create departments
    it_dept = Department("IT")
    hr_dept = Department("HR")
    finance_dept = Department("Finance")
    
    # Test adding departments
    print("Test 1: Adding Departments")
    print(company.add_department(it_dept))
    print(company.add_department(hr_dept))
    print(company.add_department(finance_dept))
    print("Expected: Three success messages for adding departments")
    print()
    
    # Create employees
    emp1 = Employee("E001", "John Doe", 30, "IT", 80000)
    emp2 = Employee("E002", "Jane Smith", 28, "HR", 65000)
    emp3 = Employee("E003", "Bob Johnson", 35, "IT", 90000)
    emp4 = Employee("E004", "Alice Brown", 32, "Finance", 75000)
    
    # Test adding employees
    print("Test 2: Adding Employees")
    print(company.add_employee(emp1))
    print(company.add_employee(emp2))
    print(company.add_employee(emp3))
    print(company.add_employee(emp4))
    print("Expected: Four success messages for adding employees")
    print()
    
    # Test listing IT department employees
    print("Test 3: IT Department Employees")
    print("IT Department Employees:")
    for employee in company.get_department_employees("IT"):
        print(employee)
    print("Expected: Should show John Doe and Bob Johnson")
    print()
    
    # Test listing HR department employees
    print("Test 4: HR Department Employees")
    print("HR Department Employees:")
    for employee in company.get_department_employees("HR"):
        print(employee)
    print("Expected: Should show Jane Smith")
    print()
    
    # Test listing Finance department employees
    print("Test 5: Finance Department Employees")
    print("Finance Department Employees:")
    for employee in company.get_department_employees("Finance"):
        print(employee)
    print("Expected: Should show Alice Brown")
    print()
    
    # Test department salary calculation
    print("Test 6: Department Salary")
    print(f"IT Department Total Salary: ${it_dept.get_department_salary()}")
    print("Expected: $170000 (80000 + 90000)")
    print()

if __name__ == "__main__":
    test_employee_management() 