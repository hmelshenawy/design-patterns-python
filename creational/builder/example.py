from car.car import Car


class CarBuilder:
    def __init__(self, car):
        self.car = car

    def with_engine(self, engine):
        self.car.engine = engine
        return self

    def with_body(self, body):
        self.car.body = body
        return self

    def with_color(self, color):
        self.car.color = color
        return self

    def with_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def with_sunroof(self):
        self.car.sunroof = True
        return self

    def build(self):
        return self.car


if __name__ == "__main__":
    original_car = Car("Custom")
    car = (CarBuilder(original_car).with_engine("electric").with_color("blue").with_body("SUV")
           .with_wheels("alloy").with_sunroof().build())
    car.describe()
    print("Same car:", car is original_car)
