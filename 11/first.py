class Car:
    """Класс автомобиля"""

    def __init__(self, mar, spd):
        self.marka = mar
        self.speed = spd
        self.odometr = None

    def car_ride(self):
        return "Автомобиль " + self.marka + " едет со скоростью " + str(self.speed)

    def read_odometr(self):
        """Вывод показаний одометра"""
        if self.odometr:
            return "Автомобиль проехал " + str(self.odometr)
        else:
            return "Показания одометра неизвестны"

    def write_odometr(self, mile):
        """Запись показаний одомоетра"""
        self.odometr = mile

    def increase_odometr(self, mile):
        """Увеличение показаний одометра"""
        self.odometr += mile


class ElectricCar(Car):
    """Класс электромобиля"""
    def __init__(self,mar, spd):
        """Инициализация атрибутов и методов родителя"""
        super().__init__(mar, spd)

        self.battery_charge = None

    def write_bcharge(self, value):
        self.battery_charge = value

    def read_bcharge(self):
        return self.battery_charge

    def power_reserve(self, rate):
        if self.battery_charge:
            return self.battery_charge / rate

    @staticmethod
    def classDetails():
        return 'Класс электромобиля. Наследник класса Car.'



if __name__ == "__main__":
    print(ElectricCar.classDetails())
    # tesla = ElectricCar('Tesla', 120)
    # print(tesla.car_ride())
    # tesla.write_bcharge(100)
    # print(tesla.read_bcharge())
    # print(tesla.power_reserve(4))
    # bmw = Car('bmw', 100)
    # bmw.write_odometr(10000)
    # bmw.increase_odometr(100)
    # print(bmw.read_odometr())
    # del bmw.speed
    # bmw.engine = 3.7
    # print(bmw.engine)
    # volvo = Car('volvo', 101)
    # print(volvo.car_ride())
    #
    # for attr in dir(volvo):
    #     print(attr)
