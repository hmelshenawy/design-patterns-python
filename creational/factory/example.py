class BMW:
    def drive(self):
        print("BMW: enjoying a sporty drive.")


class Porsche:
    def drive(self):
        print("Porsche: enjoying your dream ride.")


class Tesla:
    def drive(self):
        print("Tesla: driving on electric power.")


def create_car(brand):
    if brand == "BMW":
        return BMW()
    if brand == "Porsche":
        return Porsche()
    if brand == "Tesla":
        return Tesla()
    raise ValueError(f"Unknown car brand: {brand}")


if __name__ == "__main__":
    for brand in ["BMW", "Porsche", "Tesla"]:
        car = create_car(brand)
        car.drive()
