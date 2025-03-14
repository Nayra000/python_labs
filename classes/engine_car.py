class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def start(self):
        print(f"The {self.fuel_type} engine with {self.horsepower} HP is starting.")


class Car:
    def __init__(self, make, model, year, fuel_type, horsepower):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(fuel_type, horsepower)

    def start(self):
        print(f"Starting {self.year} {self.make} {self.model}...")
        self.engine.start()

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} with a {self.engine.horsepower} HP {self.engine.fuel_type} engine.")



car = Car("Toyota", "Supra", 2022, "petrol", 250)

car.start()
car.display_info()
