class Driver:
    def __init__(self, name, company_id, licence, car, experience):
        self.__name = name
        self.__company_id = company_id
        self.__licence = licence
        self.__car = car
        car.set_driver(self)
        self.__experience = experience

    def print_info(self):
        print(f"{type(self).__name__}:{self.__company_id} - {self.__name}"
              f"\n\tCar number:{self.__car.get_car_number()}"
              f"\n\tLicence:{self.__licence} for {self.__experience} years")

    def get_name(self):
        return self.__name

    def set_company_id(self, cid):
        self.__company_id = cid

    def set_car(self, car):
        self.__car = car

    def set_experience(self, exp):
        self.__experience = exp
