from zad_3_classes.Property import Property


class Flat (Property):
    floor: int

    def __init__(self, address, price, area, rooms, floor):
        Property.__init__(self, address, price, area, rooms)
        self.floor = floor

    def __str__(self):
        return (f'{self.address}, {self.price}, {self.area}, '
                f'{self.rooms}, {self.floor}')