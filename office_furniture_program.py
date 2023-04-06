class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.category = category
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.price = price

    def __str__(self):
        return f"{self.category} made of {self.material} (dimensions: {self.length}L x " \
               f"{self.width}W x {self.height}H, price: ${self.price})"
    