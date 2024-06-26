from abc import ABC, abstractmethod


# Базовый класс для напитков
class Beverage(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Конкретные классы для напитков
class Coffee(Beverage):
    def __init__(self):
        super().__init__("Кофе", 1.5)

    def get_description(self):
        return "Кофе"

    def get_cost(self):
        return self.price


class Tea(Beverage):
    def __init__(self):
        super().__init__("Чай", 1.0)

    def get_description(self):
        return "Чай"

    def get_cost(self):
        return self.price


# Декоратор (добавка)
class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", " + self.get_condiment_description()

    @abstractmethod
    def get_condiment_description(self):
        pass

    def get_cost(self):
        return self.beverage.get_cost() + self.get_condiment_cost()

    @abstractmethod
    def get_condiment_cost(self):
        pass


# Конкретные классы для добавок
class Milk(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def get_condiment_description(self):
        return "с молоком"

    def get_condiment_cost(self):
        return 0.5


class Sugar(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def get_condiment_description(self):
        return "с сахаром"

    def get_condiment_cost(self):
        return 0.2


if __name__ == "__main__":
    coffee = Coffee()
    coffee_with_milk = Milk(coffee)
    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)

    print(f"Напиток: {coffee_with_milk_and_sugar.get_description()}")
    print(f"Стоимость: {coffee_with_milk_and_sugar.get_cost()}")
