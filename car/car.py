from car.dashboard import Dashboard
from car.components import Engine, FuelSystem, Electronics
from behavioral.state.example import Parked
from creational.singleton.example import CarSettings


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = "petrol"
        self.color = "white"
        self.wheels = "standard"
        self.sunroof = False
        self.body = "Sedan"
        self.observers = []
        self.driving_mode = None
        self.dashboard = Dashboard()
        self.settings = CarSettings()
        self.state = Parked()
        self.engine_system = Engine()
        self.fuel_system = FuelSystem()
        self.electronics = Electronics()

    def set_driving_mode(self, driving_mode):
        print("Driving Mode Selected: ", driving_mode.name)
        self.driving_mode = driving_mode

    def drive(self):
        if self.driving_mode is None:
            print(f"{self.brand}: no driving mode selected.")
            return
        print(f"{self.brand}: ", end="")
        self.driving_mode.drive()

    def describe(self):
        print(f"{self.color} {self.brand}: {self.engine} engine, "
              f"body: {self.body}, {self.wheels} wheels, sunroof={self.sunroof}")

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

    def start(self):
        self.state.start(self)

    def press_accelerator(self):
        self.state.press_accelerator(self)

    def lock(self):
        print(f"{self.brand}: doors locked.")

    def charge_with(self, charger):
        charger.charge()
        print(f"{self.brand}: battery charging successfully.")

    def description(self):
        return f"Basic {self.brand}"

    def cost(self):
        return 20000
