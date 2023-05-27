class Transport:

    def __init__(self, passengers, color, producer, model):
        self._passengers = passengers
        self._producer = producer
        self._model = model
        self._color = color

    def get_passengers(self):
        return self._passengers

    def get_producer(self):
        return self._producer

    def get_model(self):
        return self._model

    def get_color(self):
        return self._color

    def set_passengers(self, passengers):
        self._passengers = passengers

    def set_producer(self, producer):
        self._producer = producer

    def set_model(self, model):
        self._model = model

    def set_color(self, color):
        self._color = color
