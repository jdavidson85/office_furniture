from office_furniture_program import OfficeFurniture


class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_drawers):
        super().__init__(category, material, length, width, height, price)
        self.location_of_drawers = location_of_drawers
        self.number_drawers = number_drawers

    def __str__(self):
        return f"{super().__str__()} with {self.number_drawers} drawers located on the {self.location_of_drawers}"
    