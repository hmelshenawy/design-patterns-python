from common.car import Car


class BMW(Car):
    def __init__(self):
        super().__init__("BMW")


class Porsche(Car):
    def __init__(self):
        super().__init__("Porsche")


class Tesla(Car):
    def __init__(self):
        super().__init__("Tesla")
        self.engine = "electric"


def car_factory(brand):
    if brand == "BMW":
        return BMW()
    if brand == "Porsche":
        return Porsche()
    if brand == "Tesla":
        return Tesla()
    raise ValueError(f"Unknown car brand: {brand}")


if __name__ == "__main__":
    for brand in ["BMW", "Porsche", "Tesla"]:
        car = car_factory(brand)
        print(f"Created a {car.brand} car.")
