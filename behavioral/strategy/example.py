from creational.factory.example import create_car


class EcoMode:
    def drive(self):
        print("Eco: accelerate gently to save energy.")


class SportMode:
    def drive(self):
        print("Sport: accelerate quickly for a lively drive.")


class ComfortMode:
    def drive(self):
        print("Comfort: accelerate smoothly for a relaxed ride.")


if __name__ == "__main__":
    car = create_car("BMW")
    car.set_driving_mode(EcoMode())
    car.drive()
    car.set_driving_mode(SportMode())
    car.drive()
    car.set_driving_mode(ComfortMode())
    car.drive()
