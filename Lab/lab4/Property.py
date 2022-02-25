class Property:

    def __init__(self, square_feet='', num_bedrooms='', num_bathrooms='', **data):
        super().__init__(**data)
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    def display(self):
        print("square feet:", self.square_feet, "\nnum bedrooms:",
              self.num_bedrooms, "\nnum bathrooms:", self.num_bathrooms)

    @staticmethod
    def prompt_init(square_feet, num_bedrooms, num_bathrooms):
        return {
            "square_feet": square_feet,
            "num_bedrooms": num_bedrooms,
            "num_bathrooms": num_bathrooms,
        }
