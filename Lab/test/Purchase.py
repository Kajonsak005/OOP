class Purchase:

    def __init__(self, price, taxes):
        self.price = price
        self.taxes = taxes

    def display(self):
        print("price:", self.price)
        print("taxes:", self.taxes)

    @staticmethod
    def prompt_init(price, taxes):
        return {
            "price": price,
            "taxes": taxes
        }
