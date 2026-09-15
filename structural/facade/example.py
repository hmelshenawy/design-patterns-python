from car.car import Car


class CarStartup:
    def __init__(self, car):
        self.car = car

    def start(self):
        self.car.electronics.turn_on()
        self.car.fuel_system.check()
        self.car.start()
        print(f"{self.car.brand}: ready to drive.")


if __name__ == "__main__":
    car = Car("BMW")
    CarStartup(car).start()
