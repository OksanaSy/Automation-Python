class Engine:
    def __init__(self, etype, power):
        self.engine_type = etype
        self.power = power

    def print_info(self):
        print(f"This engine is {self.engine_type} with power: {self.power}kW")

    def get_e_type(self):
        return self.engine_type

    def get_power(self):
        return self.power
