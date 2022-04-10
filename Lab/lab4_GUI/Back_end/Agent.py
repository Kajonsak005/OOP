class Agent:

    def __init__(self):
        self.property_list = []

    def add_property(self, property):
        self.property_list.append(property)

    def list_property(self):
        for property in self.property_list:
            property.display()
