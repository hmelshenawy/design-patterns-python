from creational.factory.example import create_car
from behavioral.strategy.example import SportMode, EcoMode


if __name__ == "__main__":
    # Factory -> creates the car
    car = create_car("BMW")

    # Strategy -> controls how the car drives
    car.set_driving_mode(SportMode())
    car.drive()

    print("--------------------------")
    # Swap behavior on the same car.
    car.set_driving_mode(EcoMode())
    car.drive()
