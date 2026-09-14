class Car:
    def description(self):
        return "Basic car"

    def cost(self):
        return 20000


class Turbo:
    def __init__(self, car):
        self.car = car

    def description(self):
        return self.car.description() + " + Turbo"

    def cost(self):
        return self.car.cost() + 3000


class SportExhaust:
    def __init__(self, car):
        self.car = car

    def description(self):
        return self.car.description() + " + Sport exhaust"

    def cost(self):
        return self.car.cost() + 1000


if __name__ == "__main__":
    basic_car = Car()
    upgraded_car = SportExhaust(Turbo(basic_car))
    for car in [basic_car, upgraded_car]:
        print(f"{car.description()}: ${car.cost():,}")
