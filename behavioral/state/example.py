from common.car import Car


class Parked:
    def press_accelerator(self, car):
        print("Parked: start the engine before driving.")

    def start(self, car):
        print("Parked -> Running: engine started.")
        car.state = Running()


class Running:
    def press_accelerator(self, car):
        print("Running -> Moving: the car pulls away.")
        car.state = Moving()

    def start(self, car):
        print("Running: engine is already on.")


class Moving:
    def press_accelerator(self, car):
        print("Moving: the car speeds up.")

    def start(self, car):
        print("Moving: engine is already on.")


class StatefulCar(Car):
    def __init__(self, brand):
        super().__init__(brand)
        self.state = Parked()

    def start(self):
        self.state.start(self)

    def press_accelerator(self):
        self.state.press_accelerator(self)


if __name__ == "__main__":
    car = StatefulCar("BMW")
    car.press_accelerator()
    car.start()
    car.start()
    car.press_accelerator()
    car.press_accelerator()
