class Property:
    area: str
    rooms: int
    price: float
    address: str

    def __init__(self, address, price, area, rooms):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address