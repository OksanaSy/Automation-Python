from DZ36_OOP.Car import Car
from DZ36_OOP.Driver import Driver
from DZ36_OOP.Engine import Engine
from DZ36_OOP.Gasoline import Gasoline
from DZ36_OOP.TransportCompany import TransportCompany

gas = Gasoline(92)
gas.print_info()
eng = Engine("H4", 25)
eng.print_info()
c1 = Car("BM273834", "hatchback", 4, 5, "yellow", "volkswagen", "beetle", eng, gas)
c1.print_car_info()
comp1 = TransportCompany("007", "Ice'n'Fire", "Winterfell")
comp1.print_info()
emp1 = Driver("Jon Snow", None, "4815162342", c1, 5.4)
comp1.hier_employee(emp1)
emp1.print_info()
c1.drive()
c1.speed_up()
