class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, HDD: {self.hdd}, GPU: {self.gpu}"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_hdd(self, hdd):
        self.computer.hdd = hdd
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


# Директор контролирует процесс создания объекта
class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_office_computer(self):
        return self.builder.set_cpu("Intel i5").set_ram("16GB").set_hdd("1TB").set_gpu("Integrated").build()

    def build_gaming_computer(self):
        return self.builder.set_cpu("Intel i9").set_ram("32GB").set_hdd("2TB").set_gpu("NVIDIA RTX 3080").build()


# Клиентский код
if __name__ == "__main__":
    builder = ComputerBuilder()
    director = Director(builder)

    office_computer = director.build_office_computer()
    print("Office Computer Config:")
    print(office_computer)

    gaming_computer = director.build_gaming_computer()
    print("\nGaming Computer Config:")
    print(gaming_computer)
