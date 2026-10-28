from zad_2_classes.Library import Library


class Book:
    title: str
    library: Library
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, title, library, publication_date,
                 author_name, author_surname, number_of_pages):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'{self.title} | {self.library} | {self.publication_date} | '
                f'{self.author_name} | {self.author_surname} | '
                f'{self.number_of_pages} ')