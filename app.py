from time import sleep
from creational.factory.example import car_factory
from creational.builder.example import CarBuilder
from car.dashboard import Dashboard
from car.mobile import MobileApp
from car.driving_mode import EcoMode, SportMode

def main():
    gt3rs = car_factory("Porsche")

    gt3rs = CarBuilder(gt3rs).with_engine("V6").with_color("Green").with_body("Roadester").build()

    dashboard = Dashboard()
    iphone = MobileApp()

    gt3rs.subscribe(dashboard)
    gt3rs.subscribe(iphone)

    gt3rs.set_driving_mode(SportMode())

    gt3rs.notify("Engine light on")


if __name__ == "__main__":
    main()