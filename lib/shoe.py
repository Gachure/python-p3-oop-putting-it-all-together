class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Size must be a positive integer")
        self._size = value

    def compare_size(self, other_shoe):
        if not isinstance(other_shoe, Shoe):
            raise ValueError("Argument must be a Shoe object")

        if self.size < other_shoe.size:
            return "This shoe is smaller."
        elif self.size > other_shoe.size:
            return "This shoe is larger."
        else:
            return "Sizes are the same."
