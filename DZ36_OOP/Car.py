from DZ36_OOP.Movable import Movable
from DZ36_OOP.Transport import Transport


class Car(Transport, Movable):
    __driver = None

    def __init__(self, car_num, tr_type, whl, passengers, color, producer, cmodel, engine, gas_type):
        self.__wheels = whl
        self.__car_number = car_num
        self.__gas_type = gas_type
        self.__trunk_type = tr_type
        self.__eng = engine
        Transport.__init__(self, passengers, color, producer, cmodel)

    def print_car_info(self):
        print(
            f"{type(self).__name__}:{self.__car_number};\n\t{self.get_color()},{self.__trunk_type},{self.get_producer()} {self.get_model()}"
            f";\n\tpassengers:{self.get_passengers()}, wheels:{self.__wheels}, gas:{self.__gas_type.get_octane()};"
            f"\n\tengine:{self.__eng.get_e_type()}({self.__eng.get_power()}kW)")

    def set_driver(self, driver):
        self.__driver=driver
        print(f"{self.__driver.get_name()} now driving {self.get_color()} {self.get_producer()} {self.get_model()}")

    def get_car_number(self):
        return self.__car_number

    def speed_up(self):
        print(f"{self.__driver.get_name()} on {self.get_color()} {self.get_producer()} {self.get_model()} reaches untrackable speed.")

    def drive(self):
        print(f"OMG! {self.__driver.get_name()} on {self.get_color()} {self.get_producer()} {self.get_model()} is on road!")
