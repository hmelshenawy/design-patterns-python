from creational.factory.example import car_factory
from behavioral.strategy.example import SportMode


if __name__ == "__main__":
    turboS = car_factory("Porsche")
    turboS.set_driving_mode(SportMode())
    turboS.drive()
