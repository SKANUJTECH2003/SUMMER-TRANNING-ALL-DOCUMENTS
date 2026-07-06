class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print(f"Subject: {self.subject}")


class Principal(Teacher):
    def __init__(self, name, age, subject, school_name):
        super().__init__(name, age, subject)
        self.school_name = school_name

    def display_details(self):
        self.display_teacher()
        print(f"School Name: {self.school_name}")


if __name__ == "__main__":
    principal = Principal("Mr. Sharma", 45, "Computer Science", "Green Valley School")
    principal.display_details()
