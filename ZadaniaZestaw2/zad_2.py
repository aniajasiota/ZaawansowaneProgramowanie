
class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __init__(
        self,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: str,
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"{self.city} | {self.street} | {self.zip_code} | "
            f"{self.open_hours} | {self.phone}"
        )


class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"{self.first_name} | {self.last_name} | {self.hire_date} | "
            f"{self.birth_date} | {self.city} | {self.street} | "
            f"{self.zip_code} | {self.phone}"
        )


class Book:
    title: str
    library: Library
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(
        self,
        title: str,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"{self.title} | {self.library} | {self.publication_date} | "
            f"{self.author_name} | {self.author_surname} | "
            f"{self.number_of_pages}"
        )


class Student:
    first_name: str
    last_name: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(
        self,
        first_name: str,
        last_name: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"{self.first_name} | {self.last_name} | {self.city} | "
            f"{self.street} | {self.zip_code} | {self.phone}"
        )


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

    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list[Book],
        order_date: str,
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (
            f"{self.student.first_name} {self.student.last_name} | "
            f"{self.order_date} | "
            f"{', '.join(self.book_titles(self.books))} | "
            f"{self.employee.last_name}"
        )


library1 = Library(
    "Katowice", "Lipowa 23", "30-320", "8.00-16.00", "725982475"
)
library2 = Library(
    "Warszawa", "Akacjowa 12", "41-103", "13.00-18.00", "666666666"
)

book1 = Book(
    "Leonardo da Vinci", library1, "2019-05-15", "Walter", "Isaacson", 800
)
book2 = Book(
    "W pustyni i w puszczy",
    library1,
    "2025-09-24",
    "Henryk",
    "Sienkiewicz",
    432,
)
book3 = Book(
    "Wiedźmin", library1, "1986-12-01", "Andrzej", "Sapkowski", 320
)
book4 = Book(
    "Lalka", library2, "2026-09-09", "Bolesław", "Prus", 864
)
book5 = Book(
    "Kubuś Puchatek", library2, "2022-01-26", "Alan", "Milne", 144
)

employee1 = Employee(
    "Jan", "Kowalski", "2020-02-01", "1985-04-12",
    "Katowice", "Polna 5", "40-001", "500111222"
)
employee2 = Employee(
    "Anna", "Nowak", "2019-06-15", "1990-08-23",
    "Warszawa", "Lesna 10", "00-101", "500222333"
)
employee3 = Employee(
    "Piotr", "Wisniewski", "2022-09-01", "1995-12-03",
    "Katowice", "Szkolna 8", "40-002", "500333444"
)

student1 = Student(
    "Maria", "Zielinska", "Katowice", "Kwiatowa 4",
    "40-003", "600111222"
)
student2 = Student(
    "Tobiasz", "Mruk", "Warszawa", "Długa 7",
    "00-102", "600222333"
)
student3 = Student(
    "Katarzyna", "Kaminska", "Katowice", "Mickiewicza 9",
    "40-004", "600333444"
)

order1 = Order(employee1, student1, [book1, book2], "2026-10-15")
order2 = Order(
    employee2, student2, [book3, book4, book5], "2026-10-16"
)

print(order1)
print(order2)
