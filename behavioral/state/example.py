class Parked:
    def press_accelerator(self, car):
        print("Parked: start the engine before driving.")

    def start(self, car):
        car.engine_system.start()
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


if __name__ == "__main__":
    from car.car import Car

    car = Car("BMW")
    car.press_accelerator()
    car.start()
    car.start()
    car.press_accelerator()
    car.press_accelerator()
