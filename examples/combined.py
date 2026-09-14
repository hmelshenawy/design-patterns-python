from creational.factory.example import car_factory
from behavioral.strategy.example import SportMode, EcoMode
from creational.builder.example import CarBuilder


if __name__ == "__main__":
    print("-----Start Building------")
    # Factory -> creates the car
    turboS = car_factory("Porsche")
    turboS = CarBuilder(turboS).with_body("Coupe").with_engine("V8").with_color("Red").build()
    turboS.describe()
    # Strategy -> controls how the car drives

    print("------Change Drive Mode--------")
    turboS.set_driving_mode(SportMode())
    turboS.drive()

    print("--------------------------")
    # Swap behavior on the same car.
    turboS.set_driving_mode(EcoMode())
    turboS.drive()
