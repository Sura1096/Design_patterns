from abc import ABC, abstractmethod


# Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def click(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self) -> str:
        pass


# Конкретные продукты для Windows
class WindowsButton(Button):
    def click(self) -> str:
        return "Clicking Windows button"


class WindowsCheckbox(Checkbox):
    def check(self) -> str:
        return "Checking Windows checkbox"


# Конкретные продукты для MacOS
class MacOSButton(Button):
    def click(self) -> str:
        return "Clicking MacOS button"


class MacOSCheckbox(Checkbox):
    def check(self) -> str:
        return "Checking MacOS checkbox"


# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Конкретные фабрики для Windows
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


# Конкретные фабрики для MacOS
class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


# Клиентский код
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.check())


# Используем клиентский код с конкретными фабриками
if __name__ == "__main__":
    print("Client: Testing client code with WindowsFactory:")
    client_code(WindowsFactory())

    print("\nClient: Testing client code with MacOSFactory:")
    client_code(MacOSFactory())