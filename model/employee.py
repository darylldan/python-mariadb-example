import datetime
from dataclasses import dataclass

@dataclass
class Employee:
    empno: int
    ename: str | None = None
    job: str | None = None
    mgr: int | None = None
    hiredate : datetime.date | None = None
    sal: float | None = None
    comm: float | None = None
    deptno: int | None = None

    # Whenever the class is printed using print(), this function will be called instead
    def __str__(self):
        return f"-----\nEmployee No: {self.empno}\t\tEmployee Name: {self.ename}\nJob: {self.job}\t\tManager Empno: {self.mgr}\nSalary: {self.sal}\t\tCommission: {self.comm}\nDepartment No.: {self.deptno}\t\tHiredate: {self.hiredate}\n"