from copy import deepcopy


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


if __name__ == '__main__':
    john = Person('John', Address('123 London Road', 'London', 'UK'))
    jane = deepcopy(john)
    jane.name = 'Jane'
    jane.address.street = '567 London Road'
    print(john)
    print()
    print(jane)
