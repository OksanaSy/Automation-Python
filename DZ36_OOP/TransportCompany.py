class TransportCompany:
    __employees = []

    def __init__(self, company_id, name, location):
        self.__company_id = company_id
        self.__name = name
        self.__location = location

    def hier_employee(self, driver):
        self.__employees.append(driver)
        driver.set_company_id(self.__company_id)
        print(f"{driver.get_name()} hired to {self.__name}")

    def print_info(self):
        print(f"{type(self).__name__}: {self.__name}, {self.__company_id} from {self.__location}")
