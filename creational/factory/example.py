
from car.models.Mercedes import Mercedes
from car.models.porsche import Porsche
from car.models.bmw import BMW


# class BMW(Car):
#     def __init__(self):
#         super().__init__("BMW")


# class Porsche(Car):
#     def __init__(self):
#         super().__init__("Porsche")


# class Tesla(Car):
#     def __init__(self):
#         super().__init__("Tesla")
#         self.engine = "electric"


def car_factory(brand):
    if brand == "BMW":
        return BMW()
    if brand == "Porsche":
        return Porsche()
    if brand == "Mercedes":
        return Mercedes()
    raise ValueError(f"Unknown car brand: {brand}")


if __name__ == "__main__":
    for brand in ["BMW", "Porsche", "Mercedes"]:
        car = car_factory(brand)
        print(f"Created a {car.brand} car.")
