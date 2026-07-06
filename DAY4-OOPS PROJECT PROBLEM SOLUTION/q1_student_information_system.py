class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = []

    def get_data(self, name=None, roll_number=None, marks=None):
        if name is None:
            self.name = input("Enter student name: ")
        else:
            self.name = name

        if roll_number is None:
            self.roll_number = input("Enter roll number: ")
        else:
            self.roll_number = roll_number

        if marks is None:
            self.marks = []
            for i in range(3):
                subject_mark = float(input(f"Enter marks for subject {i + 1}: "))
                self.marks.append(subject_mark)
        else:
            self.marks = marks

    def display_data(self):
        print("\nStudent Information")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Marks:")
        for i, mark in enumerate(self.marks, start=1):
            print(f"  Subject {i}: {mark}")

    def calculate_percentage(self):
        total = sum(self.marks)
        percentage = (total / (3 * 100)) * 100
        return percentage


if __name__ == "__main__":
    student = Student()
    student.get_data("Aarav", "101", [88, 92, 90])
    student.display_data()
    print(f"Percentage: {student.calculate_percentage():.2f}%")
