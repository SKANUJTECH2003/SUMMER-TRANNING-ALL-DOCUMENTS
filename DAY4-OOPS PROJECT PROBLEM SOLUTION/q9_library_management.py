class Library:
    def __init__(self, max_books):
        self.max_books = max_books
        self.books_issued = 0

    def issue_book(self):
        raise NotImplementedError("Child classes must implement issue_book()")


class StudentLibrary(Library):
    def __init__(self):
        super().__init__(2)

    def issue_book(self):
        if self.books_issued < self.max_books:
            self.books_issued += 1
            print(f"Book issued successfully. Books issued: {self.books_issued}")
        else:
            print("Student library limit reached (maximum 2 books).")


class FacultyLibrary(Library):
    def __init__(self):
        super().__init__(5)

    def issue_book(self):
        if self.books_issued < self.max_books:
            self.books_issued += 1
            print(f"Book issued successfully. Books issued: {self.books_issued}")
        else:
            print("Faculty library limit reached (maximum 5 books).")


if __name__ == "__main__":
    student_lib = StudentLibrary()
    faculty_lib = FacultyLibrary()

    for _ in range(3):
        student_lib.issue_book()

    for _ in range(6):
        faculty_lib.issue_book()
