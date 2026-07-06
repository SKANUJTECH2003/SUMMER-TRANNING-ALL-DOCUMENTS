def calculate_gross_income(basic_salary, hra_percentage=20, da_percentage=10, tax_percentage=10):
    hra = basic_salary * hra_percentage / 100
    da = basic_salary * da_percentage / 100
    gross_income = basic_salary + hra + da
    tax_amount = gross_income * tax_percentage / 100
    net_income = gross_income - tax_amount
    return {
        "basic_salary": basic_salary,
        "hra": hra,
        "da": da,
        "gross_income": gross_income,
        "tax_amount": tax_amount,
        "net_income": net_income,
    }


if __name__ == "__main__":
    salary = float(input("Enter basic salary: "))
    result = calculate_gross_income(salary)
    print(f"Basic Salary: {result['basic_salary']:.2f}")
    print(f"HRA (20%): {result['hra']:.2f}")
    print(f"DA (10%): {result['da']:.2f}")
    print(f"Gross Income: {result['gross_income']:.2f}")
    print(f"Tax Amount (10%): {result['tax_amount']:.2f}")
    print(f"Net Income: {result['net_income']:.2f}")
