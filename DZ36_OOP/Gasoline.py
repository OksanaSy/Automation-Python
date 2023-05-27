class Gasoline:
    def __init__(self, o_numb):
        self.octane_number = o_numb

    def print_info(self):
        print(f"This gas has octane number:{self.octane_number}")

    def get_octane(self):
        return self.octane_number
