from creational.factory.example import create_car
from behavioral.strategy.example import SportMode


if __name__ == "__main__":
    turboS = create_car("Porsche")
    turboS.set_driving_mode(SportMode())
    turboS.drive()
