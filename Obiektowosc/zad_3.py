class Property:
    area : str
    rooms : int
    price : float
    address : str

    def __init__(self, address, price, area, rooms):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House (Property):
    plot : int

    def __init__(self, address, price, area, rooms, plot):
        Property.__init__(self, address, price, area, rooms)
        self.plot = plot

    def __str__(self):
        return f'{self.address}, {self.price}, {self.area}, {self.rooms}, {self.plot}'

class Flat (Property):
    floor : int

    def __init__(self, address, price, area, rooms, floor):
        Property.__init__(self, address, price, area, rooms)
        self.floor = floor

    def __str__(self):
        return f'{self.address}, {self.price}, {self.area}, {self.rooms}, {self.floor}'

house1 = House('Promienna 22 Katowice', '850000', '150', '5', '600')
flat1 = Flat('Jasna 5A Katowice', '270000', '50', '2', '3')

print(house1)
print(flat1)