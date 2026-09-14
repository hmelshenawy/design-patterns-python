class Engine:
    def start(self):
        print("Engine: started.")


class FuelSystem:
    def check(self):
        print("Fuel system: fuel available.")


class Electronics:
    def turn_on(self):
        print("Electronics: powered on.")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.fuel_system = FuelSystem()
        self.electronics = Electronics()

    def start(self):
        self.electronics.turn_on()
        self.fuel_system.check()
        self.engine.start()
        print("Car: ready to drive.")


if __name__ == "__main__":
    car = Car()
    car.start()
