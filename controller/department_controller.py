from model.department import Department
from sql.sql_connector import MariaDBInstance

class DepartmentController:
    db: MariaDBInstance
    TABLE_NAME = "dept"

    def __init__(self, db: MariaDBInstance):
        self.db = db

    def get_all_dept(self):
        self.db.cur().execute(f"SELECT * FROM {self.TABLE_NAME}") 
        raw_result = self.db.cur().fetchall()

        results: list[Department] = []

        for row in raw_result:
            results.append(
                Department(*row)
            )
            
        return results
    
    def get_employee_count_per_department(self):
        self.db.cur().execute(f'''SELECT d.dname DEPARTMENT_NAME, COUNT(e.empno) EMPLOYEE_COUNT 
                              FROM {self.TABLE_NAME} d LEFT JOIN emp e ON d.deptno=e.deptno
                              GROUP BY d.deptno''')
        
        results =  self.db.cur().fetchall()

        return results