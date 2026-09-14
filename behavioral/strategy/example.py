class EcoMode:
    def drive(self):
        print("Eco: accelerate gently to save energy.")


class SportMode:
    def drive(self):
        print("Sport: accelerate quickly for a lively drive.")


class ComfortMode:
    def drive(self):
        print("Comfort: accelerate smoothly for a relaxed ride.")


class Car:
    def __init__(self, driving_mode):
        self.driving_mode = driving_mode

    def drive(self):
        self.driving_mode.drive()


if __name__ == "__main__":
    car = Car(EcoMode())
    car.drive()
    car.driving_mode = SportMode()
    car.drive()
    car.driving_mode = ComfortMode()
    car.drive()
