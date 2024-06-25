from abc import ABC, abstractmethod


# Абстрактный класс устройства
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# Конкретные реализации устройств
class SmartBulb(Device):
    def turn_on(self):
        print("Умная лампочка включена")

    def turn_off(self):
        print("Умная лампочка выключена")


class SmartThermostat(Device):
    def turn_on(self):
        print("Умный термостат включен")

    def turn_off(self):
        print("Умный термостат выключен")


# Абстрактный класс пульта управления
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self._device = device

    @abstractmethod
    def toggle_power(self):
        pass


# Конкретные реализации пультов
class BasicRemote(RemoteControl):
    def toggle_power(self):
        if self._device:
            self._device.turn_on()
        else:
            self._device.turn_off()


if __name__ == "__main__":
    # Использование
    bulb = SmartBulb()
    thermostat = SmartThermostat()

    bulb_remote = BasicRemote(bulb)
    thermostat_remote = BasicRemote(thermostat)

    bulb_remote.toggle_power()  # Вывод: Умная лампочка включена
    thermostat_remote.toggle_power()  # Вывод: Умный термостат включен
