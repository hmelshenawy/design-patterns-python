from common.car import Car


class Engine:
    def start(self):
        print("Engine: started.")


class FuelSystem:
    def check(self):
        print("Fuel system: fuel available.")


class Electronics:
    def turn_on(self):
        print("Electronics: powered on.")


class StartupCar(Car):
    def __init__(self, brand):
        super().__init__(brand)
        self.engine_system = Engine()
        self.fuel_system = FuelSystem()
        self.electronics = Electronics()

    def start(self):
        self.electronics.turn_on()
        self.fuel_system.check()
        self.engine_system.start()
        print(f"{self.brand}: ready to drive.")


if __name__ == "__main__":
    car = StartupCar("BMW")
    car.start()
