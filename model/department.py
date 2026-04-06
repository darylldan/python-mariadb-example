from dataclasses import dataclass

@dataclass
class Department:
    deptno: int
    dname: str | None
    loc: str | None = None

    def __str__(self):
        return f"-----\nDepartment Number: {self.deptno}\nDepartment Name: {self.dname}\nLocation: {self.loc}"