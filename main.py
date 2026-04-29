# Resource: https://pymysql.readthedocs.io/en/latest/user/examples.html

from controller.department_controller import DepartmentController
from controller.employee_controller import EmployeeController
from sql.sql_connector import MariaDBInstance
from view.ui import UserInterface

# This clause ensures that in this whole project, the only entry point of execution is in main.py
# Meaning, codes on other files that are global (not in classes/functions) are not executed
if __name__ == "__main__":
    # Create a connection with MariaDB using the created MariaDB Instance
    sql = MariaDBInstance(
        user="scott",
        password="tiger",
        database="scott",
    )

    # Instantiate the controllers
    emp_ctrl = EmployeeController(sql)
    dept_ctrl = DepartmentController(sql)

    # Instantiate the UI
    ui = UserInterface(emp_ctrl, dept_ctrl)
    ui.start()

    # Once the program exits, close the db connection
    sql.close()