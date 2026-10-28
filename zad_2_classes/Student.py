class Student:
    first_name: str
    last_name: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name, last_name, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f'{self.first_name} | {self.last_name} | {self.city} | '
                f'{self.street} | {self.zip_code} | {self.phone}')