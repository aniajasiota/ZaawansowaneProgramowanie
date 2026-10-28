from zad_3_classes.Property import Property


class House (Property):
    plot: int

    def __init__(self, address, price, area, rooms, plot):
        Property.__init__(self, address, price, area, rooms)
        self.plot = plot

    def __str__(self):
        return (f'{self.address}, {self.price}, {self.area}, '
                f'{self.rooms}, {self.plot}')