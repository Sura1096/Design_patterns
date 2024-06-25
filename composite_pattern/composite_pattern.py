from abc import ABC, abstractmethod


# Базовый класс для графических объектов
class GraphicObject(ABC):
    def __init__(self, name):
        self.name = name
        self.parent = None

    def add(self, obj):
        raise NotImplementedError("Метод add() должен быть переопределен в подклассе")

    def remove(self, obj):
        raise NotImplementedError("Метод remove() должен быть переопределен в подклассе")

    @abstractmethod
    def draw(self):
        pass


# Конкретный класс для простых фигур
class Circle(GraphicObject):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def draw(self):
        print(f"Рисуем круг '{self.name}' с радиусом {self.radius}")


# Составной объект (группа)
class Group(GraphicObject):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, obj):
        self.children.append(obj)
        obj.parent = self

    def remove(self, obj):
        self.children.remove(obj)
        obj.parent = None

    def draw(self):
        print(f"Группа '{self.name}':")
        for child in self.children:
            child.draw()


if __name__ == '__main__':
    # Использование
    circle1 = Circle("Круг 1", 5)
    circle2 = Circle("Круг 2", 10)
    group = Group("Группа фигур")

    group.add(circle1)
    group.add(circle2)

    group.draw()
