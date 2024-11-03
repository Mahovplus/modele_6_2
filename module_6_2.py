class Vehicle:
    """Создание родительского класса"""
    owner = ''
    __engine_power = ''
    __model = ''
    __color = ''
    __COLOR_VARIANTS = ['red', 'purple', 'pink', 'yellow', 'black tea']

    def __init__(self, owner, model, engine, color):
        """Инициализация атрибутов класса"""
        self.owner = owner
        self.__model = model
        self.__engine_power = engine
        if color in self.__COLOR_VARIANTS:
            self.__color = color

    def get_model(self):
        print(f"Model: {self.__model}")

    def get_horsepower(self):
        print(f"Engine power: {self.__engine_power}")

    def get_color(self):
        print(f'Color: {self.__color.title()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Owner: {self.owner}")

    def set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            __color = new_color
        else:
            print(f"You can't changes the color to {new_color.title()}")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    owner = ''
    __engine_power = ''
    __model = ''
    __color = ''
    __COLOR_VARIANTS = ['red', 'purple', 'pink', 'yellow', 'black']

    def __init__(self, owner, model, engine, color):
        """Инициализация атрибутов класса"""
        self.owner = owner
        self.__model = model
        self.__engine_power = engine
        if color in self.__COLOR_VARIANTS:
            self.__color = color

    def get_model(self):
        print(f"Model: {self.__model}")

    def get_horsepower(self):
        print(f"Engine power: {self.__engine_power}")

    def get_color(self):
        print(f'Color: {self.__color.title()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Owner: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"You can't changes the color to {new_color}")


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'red')

vehicle1.print_info()
vehicle1.set_color('blue')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()