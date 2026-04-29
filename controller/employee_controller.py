import pymysql
from model.employee import Employee
from sql.sql_connector import MariaDBInstance

class EmployeeController():
    db: MariaDBInstance
    TABLE_NAME = "emp"

    def __init__(self, db: MariaDBInstance):
        self.db = db
        pass

    def get_all_employees(self):
        self.db.cur().execute(f"SELECT * FROM {self.TABLE_NAME}") 
        raw_result = self.db.cur().fetchall()

        results: list[Employee] = []

        for row in raw_result:
            results.append(
                Employee(*row)
            )

        for r in results:
            print(r)

        return results
    
    def get_employee_by_id(self, empno: int) -> Employee | None:
        self.db.cur().execute(f"SELECT * FROM {self.TABLE_NAME} WHERE empno= %s", (empno,)) 
        raw_result = self.db.cur().fetchone()

        if raw_result == None:
            return None
        
        return Employee(*raw_result)
    
    def insert_employee(self, employee: Employee) -> bool | None:
        try: 
            self.db.cur().execute(
                f"INSERT INTO {self.TABLE_NAME} VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    employee.empno,
                    employee.ename,
                    employee.job,
                    employee.mgr,
                    employee.hiredate,
                    employee.sal,
                    employee.comm,
                    employee.deptno
                )
            )

            return True
        except pymysql.Error as e:
            print(f"A database error occurred: {e}")
        
            # If this was an INSERT/UPDATE/DELETE, you would call conn.rollback() here
            # to undo any partial changes.
            return None

    def delete_employee_by_empno(self, empno: int) -> bool | None:
        try:
            self.db.cur().execute(
                f"DELETE FROM {self.TABLE_NAME} WHERE empno=%s",
                (empno,)
            )

            return True
        except pymysql.Error as e:
            print(f"A database error occurred: {e}")

            return None

