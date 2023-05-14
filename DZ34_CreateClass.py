"""
Создать два класса, предметную область выбрать по своему желанию.

Классы должны содержать:

- минимум два поля экземпляров и одно поле класса

- минимум два метода экземпляра

Хотя бы в одном классе:

- минимум один метод класса

- минимум один статический метод

К методам добавить строки документации.



Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)

Написать код который создает несколько экземпляров и взаимодействует с объектами

Задание в том числе и на фантазию



Как пример, классы Employee (сотрудник) и Company (компания).
"""


class Cat:
    sound='mrrrrrrrrrrrr...'

    def __init__(self, fname, colour):
        self.fname = fname
        self.colour = colour
        self.hungry = True


    def get_name(self):
        return self.fname

    def set_name(self, fname):
        self.fname = fname

    def say_meow(self):  # котик каже мяв :)
        print(f"{self.fname} say MEOW")

    # основна котяча функція, на яку іде основна енергія і калорії :)
    def do_nothing(self):
        self.hungry = True
        print("Cat does nothing and become hungry!")

    @staticmethod
    def be_nice(): # демон-процес, сенсу не має
        print(Cat.sound)


class Home_Cat(Cat):
    owner = None

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def cry_for_food(self):  # Котячий метод отримання енершії для do_nothing
        print("What a noise! ", self.owner, " added food to plate.", self.fname, "now is fed.")
        self.hungry = False


class Clinic:
    patients = []  # БД спільна на клініки мережі

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def print_data(self):  # Виводимо назву і адресу вет.клініки
        print(f"It's {self.name} clinic in {self.address}")

    def add_patient(self, cat):  # Додаємо пацієнтів в клініку (власником або волонтером)
        if isinstance(cat, Home_Cat):
            print(cat.get_owner(), " took ", cat.get_name(), "to clinic")
        else:
            print(cat.get_name(), "sent to clinic by volonteers.")
        Clinic.patients.append(cat)
        print("Now in clinic:")
        for p in self.patients:
            print(p.get_name())


class Homeless_Cat(Cat):

    def hunting(self):  # Метод отримання енергії для вуличних котів :(
        print(self.fname, "is hunting.")
        self.hungry = False
        print("Hungry set to", self.hungry)


vetClinic = Clinic("Health", "Sumy")
vetClinic.print_data()
helha = Home_Cat('Helha', 'Gray')
helha.set_owner("Oksana")
tailless = Homeless_Cat('Tailless', 'Black')
unfamiliarCat = Cat(' - ', 'White')
vetClinic.add_patient(helha)  # Додаємо пацієнта з домашніх котів
vetClinic.add_patient(tailless)  # Додаємо пацієнта з вуличних котів
helha.cry_for_food()
helha.do_nothing()
helha.be_nice()
helha.cry_for_food()
tailless.hunting()
tailless.do_nothing()
tailless.be_nice()
tailless.hunting()
helha.say_meow()

# Втомилася фантазувати :(
