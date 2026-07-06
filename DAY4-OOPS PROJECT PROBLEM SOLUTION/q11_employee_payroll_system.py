from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display(self):
        print(f"Full-Time Employee: {self.name} ({self.employee_id})")
        print(f"Salary: {self.calculate_salary()}")


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display(self):
        print(f"Part-Time Employee: {self.name} ({self.employee_id})")
        print(f"Salary: {self.calculate_salary()}")


if __name__ == "__main__":
    employees = [
        FullTimeEmployee("F01", "Kavya", 60000),
        PartTimeEmployee("P01", "Aman", 500, 20),
    ]

    for employee in employees:
        employee.display()
