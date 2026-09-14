class Car:
    def __init__(self):
        self.engine = "petrol"
        self.color = "white"
        self.wheels = "standard"
        self.sunroof = False
        self.body="Sedan"

    def describe(self):
        print(f"{self.color} car: {self.engine} engine, body: {self.body} "
              f"{self.wheels} wheels, sunroof={self.sunroof}")


class CarBuilder:
    def __init__(self):
        self.car = Car()

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
    car = (CarBuilder().with_engine("electric").with_color("blue").with_body("SUV")
           .with_wheels("alloy").with_sunroof().build())
    car.describe()
