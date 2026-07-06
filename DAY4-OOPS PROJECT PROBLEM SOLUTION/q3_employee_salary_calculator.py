class Employee:
    def __init__(self, employee_id, name, basic_salary):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display_details(self):
        print("\nEmployee Details")
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Basic Salary: {self.basic_salary:.2f}")
        print(f"HRA: {self.calculate_hra():.2f}")
        print(f"DA: {self.calculate_da():.2f}")
        print(f"Gross Salary: {self.calculate_gross_salary():.2f}")


if __name__ == "__main__":
    employee = Employee("E101", "Neha", 40000)
    employee.display_details()
