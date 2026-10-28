from zad_2_classes.Employee import Employee
from zad_2_classes.Book import Book
from zad_2_classes.Student import Student


class Order:
    employee: Employee
    student: Student
    books: list[Book]
    order_date: str

    @staticmethod
    def book_titles(books: list[Book]):
        b_titles = []
        for book in books:
            b_titles.append(book.title)

        return b_titles

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (f'{self.student.first_name} {self.student.last_name} | '
                f'{self.order_date} | '
                f'{", ".join(self.book_titles(self.books))} | '
                f'{self.employee.last_name}')