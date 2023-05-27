from abc import abstractmethod


class Movable:
    @abstractmethod
    def speed_up(self):
        pass

    @abstractmethod
    def drive(self):
        pass
