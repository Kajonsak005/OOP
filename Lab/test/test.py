class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **data):
        super().__init__(**data)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **data):
        super().__init__(**data)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **data):
        super().__init__(**data)
        self.phone = phone


test = Friend(phone="1", street='3', city='3333',
              state='3', code='3',  email='3')

print(test.city)
print(test.email)
