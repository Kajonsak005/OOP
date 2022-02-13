class Purchase:

    def __init__(self):
        self.price = ""
        self.taxes = ""

    def display(self):
        print("price:", self.price)
        print("taxes:", self.taxes)

    @staticmethod
    def prompt_init(price, taxes):
        return {"price": price, "taxes": taxes}
