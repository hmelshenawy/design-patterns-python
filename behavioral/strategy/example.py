from creational.factory.example import car_factory
from car.driving_mode import DrivingMode


class EcoMode(DrivingMode):
    def drive(self):
        print("Eco: accelerate gently to save energy.")


class SportMode(DrivingMode):
    def drive(self):
        print("Sport: accelerate quickly for a lively drive.")


class ComfortMode(DrivingMode):
    def drive(self):
        print("Comfort: accelerate smoothly for a relaxed ride.")


if __name__ == "__main__":
    car = car_factory("BMW")
    car.set_driving_mode(EcoMode())
    car.drive()
    car.set_driving_mode(SportMode())
    car.drive()
    car.set_driving_mode(ComfortMode())
    car.drive()
