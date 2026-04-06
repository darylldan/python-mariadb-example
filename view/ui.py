from datetime import datetime
from typing import Literal
from controller.department_controller import DepartmentController
from controller.employee_controller import EmployeeController
from model.employee import Employee

class UserInterface():
    emp_ctrl: EmployeeController
    dept_ctrl: DepartmentController

    def __init__(self, emp_ctrl: EmployeeController, dept_ctrl: DepartmentController):
        self.emp_ctrl = emp_ctrl
        self.dept_ctrl = dept_ctrl

    def print_main_menu(self):
        print('''
[1] Get all employees
[2] Get employee by employee no.
[3] Get all departments
[4] Get employee count per department
[5] Insert employee
[6] Delete employee by employee no.
[0] Exit
''')
        
    def print_all_employees(self):
        for e in self.emp_ctrl.get_all_employees():
            print(e)

    def print_employee_by_no(self):
        empno = int(input("Enter employee number: "))

        result = self.emp_ctrl.get_employee_by_id(empno)

        if result == None:
            print(f"Employee not found!\n")
            return
        
        print(result)

    def print_all_departments(self):
        for d in self.dept_ctrl.get_all_dept():
            print(d)

    def print_employee_count_per_department(self):
        print(f"Department Name\t\tEmployee Count")

        for r in self.dept_ctrl.get_employee_count_per_department():
            print(f"{r[0]}\t\t{r[1]}")

    def get_user_input(self, prompt: str, input_type: Literal["str", "int", "float", "date"]):
        while True:
            user_input = input(prompt + "\nEnter /cancel to abort operation\nInput: ")

            if user_input == "/cancel":
                return "__ABORT__"
            
            if user_input == "":
                print(f"Please enter 'n/a' for empty field.\n")
                continue

            if user_input == "n/a":
                return None

            if input_type == "str":
                return user_input
            
            if input_type == "int":
                try:
                    converted = int(user_input)
                    return converted
                except ValueError:
                    print("Invalid ingeter. Please try again.")
                    continue
            
            if input_type == "float":
                try:
                    converted = float(user_input)
                    return converted
                except ValueError:
                    print("Invalid float. Please try again.")
                    continue
            
            if input_type == "date":
                try:
                    converted = datetime.strptime(user_input, "%Y-%m-%d")
                    return converted
                except ValueError:
                    print("Invalid date. Please try again.")
                    continue

    def insert_employee(self) -> bool:
        empno = self.get_user_input("Enter employee number:", "int")
        if empno == "__ABORT__":
            return False

        ename = self.get_user_input("Enter employee name:", "str")
        if ename == "__ABORT__":
            return False
        
        job = self.get_user_input("Enter job:", "str")
        if job == "__ABORT__":
            return False
        
        mgr = self.get_user_input("Enter manager's employee no.: ", "int")
        if mgr == "__ABORT__":
            return False
        
        hiredate = self.get_user_input("Enter hiredate (YYYY-MM-DD):", "str")
        if hiredate == "__ABORT__":
            return False
        
        sal = self.get_user_input("Enter salary:", "float")
        if sal == "__ABORT__":
            return False
        
        comm = self.get_user_input("Enter commission:", "float")
        if comm == "__ABORT__":
            return False
        
        deptno = self.get_user_input("Enter Department No.:", "int")
        if deptno == "__ABORT__":
            return False
        
        new_emp = Employee(
            empno=empno,
            ename=ename,
            job=job,
            mgr=mgr,
            hiredate=hiredate,
            sal=sal,
            comm=comm,
            deptno=deptno
        )

        res = self.emp_ctrl.insert_employee(new_emp)
        if res == None:
            print(f"Failed to insert.\n")
            return
        
        print(f"Successfully inserted employee:")
        print(new_emp)
        return True

    def delete_employee(self):
        empno = self.get_user_input("Enter employee number to delete:", "int")

        emp = self.emp_ctrl.get_employee_by_id(empno)
        if not emp:
            print(f"Employee not found.\n")
            return
        
        res = self.emp_ctrl.delete_employee_by_empno(empno)

        if res == None:
            print(f"Deletion failed\n")
            return
        
        print(f"Successfully deleted {emp.ename}.")


    def start(self):
        while True:
            self.print_main_menu()
            inp = int(input("Enter choice: "))

            match inp:
                case 1: self.print_all_employees()
                case 2: self.print_employee_by_no()
                case 3: self.print_all_departments()
                case 4: self.print_employee_count_per_department()
                case 5: 
                    res = self.insert_employee()
                    if not res:
                        print("Insertion cancelled.\n")
                case 6: self.delete_employee()
                case 0: return
                case _ : 
                    print("Invalid input!")
                    continue