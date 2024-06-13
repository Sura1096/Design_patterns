from copy import deepcopy


class CarPrototype:
    def clone(self):
        return deepcopy(self)


class Car(CarPrototype):
    def __init__(self, model, color, features):
        self.model = model
        self.color = color
        self.features = features

    def __str__(self):
        return f'Car(model={self.model}, color={self.color}, features={self.features})'


# Create the base car model
base_car = Car('Sedan', 'Red', ['Air Conditioning', 'Power Steering'])

# Clone base car model
car1 = base_car.clone()
car1.color = 'Blue'
car1.features.append('Sunroof')

car2 = base_car.clone()
car2.color = 'Green'
car2.features.append('Leather Seats')

car3 = base_car.clone()
car3.color = 'Black'
car3.features.append('GPS Navigation')

print(base_car)
print(car1)
print(car2)
print(car3)
