from abc import ABC, abstractmethod


class car_factory(ABC):
    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_hatchback(self):
        pass


class audi_factory(car_factory):
    def create_sedan(self):
        return A_model()

    def create_hatchback(self):
        return Q_model()


class volkswagen_factory(car_factory):
    def create_sedan(self):
        return passat()

    def create_hatchback(self):
        return beetle()


class volkswagen(ABC):
    @abstractmethod
    def move(self):
        pass


class passat(volkswagen):
    def move(self):
        print("Volkswagen passat on road")


class beetle(volkswagen):
    def move(self):
        print("Volkswagen beetle on road")


class audi(ABC):
    @abstractmethod
    def move(self):
        pass


class A_model(audi):
    def move(self):
        print("Audi model A on road")


class Q_model(audi):
    def move(self):
        print("Audi model Q on road")


class client:
    def get_car(self):
        abs_factory = audi_factory()
        car = abs_factory.create_sedan()
        car.move()
        # -------------------------------------------
        abs_factory = volkswagen_factory()
        car = abs_factory.create_hatchback()
        car.move()


client = client()
client.get_car()