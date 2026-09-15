from creational.factory.example import car_factory
from car.driving_mode import EcoMode, SportMode, ComfortMode


if __name__ == "__main__":
    car = car_factory("BMW")
    car.set_driving_mode(EcoMode())
    car.drive()
    car.set_driving_mode(SportMode())
    car.drive()
    car.set_driving_mode(ComfortMode())
    car.drive()
