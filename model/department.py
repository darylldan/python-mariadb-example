from dataclasses import dataclass

@dataclass
class Department:
    deptno: int
    dname: str | None
    loc: str | None = None

    # Whenever the class is printed using print(), this function will be called instead
    def __str__(self):
        return f"-----\nDepartment Number: {self.deptno}\nDepartment Name: {self.dname}\nLocation: {self.loc}"