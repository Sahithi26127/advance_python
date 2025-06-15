class Employee:
    
    def __init__(self, n, i, s, d):
        self.name = n
        self.id = i
        self.salary = s
        self.department = d
        
    def calculate_emp_sal(self, hours):
        if hours > 10:
            overtime = (hours - 10) * 100
            self.salary += overtime
            print(f"Overtime added: ₹{overtime}")
        else:
            print("No Overtime ")
        print(f"Total Salary: ₹{self.salary}")
        
    def change_department(self, new_dep):
        self.department = new_dep
        print(f"Department changed to: {self.department}")
        
    def print_details(self):
        print("\n------ Employee Details ------")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: ₹{self.salary}")
        print(f"Department: {self.department}")
        print("------------------------------")


# Storage for employee(s)
employee_list = []

while True:
    role = input("\nWho are you? (HR/Employee) or type 'exit' to quit: ").upper()
    
    if role == 'EMPLOYEE':
        print("\n--- Enter Your Details ---")
        name = input("Name: ")
        emp_id = input("Employee ID: ")
        salary = int(input("Base Salary: ₹"))
        dept = input("Department: ")
        hours = int(input("Hours Worked: "))

        emp = Employee(name, emp_id, salary, dept)
        emp.calculate_emp_sal(hours)
        employee_list.append(emp)
        print("Your info has been saved!\n")

    elif role == 'HR':
        if not employee_list:
            print("No employee data available yet! ")
            continue

        print("\n HR's ACCOUNT:")
        while True:
            option = input("\nChoose an option:\n  1. Check employee details\n  2. Change department\n  3. Check salary with overtime\n  4. Exit HR Menu\nEnter choice: ")
        
            if option == '1':
                for emp in employee_list:
                    emp.print_details()

            elif option == '2':
                emp_id = input("Enter Employee ID to change department: ")
                for emp in employee_list:
                    if emp.id == emp_id:
                        new_dep = input("Enter new department: ")
                        emp.change_department(new_dep)
                        break
                else:
                    print("Employee not found ")

            elif option == '3':
                emp_id = input("Enter Employee ID: ")
                for emp in employee_list:
                    if emp.id == emp_id:
                        hours = int(input("Enter hours worked: "))
                        emp.calculate_emp_sal(hours)
                        break
                else:
                    print("Employee not found ")

            elif option == '4':
                print("Exiting HR Portal ")
                break

            else:
                print("Bruhh pick a valid option ")

    elif role == 'EXIT':
        print("Thank you for using the system ")
        break

    else:
        print("Invalid input! Please enter 'HR', 'Employee', or 'exit'")
