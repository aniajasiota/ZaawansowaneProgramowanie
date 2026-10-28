class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f'{self.first_name} | {self.last_name} | {self.hire_date} | '
                f'{self.birth_date} | {self.city} | {self.street} | '
                f'{self.zip_code}')