class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = "petrol"
        self.color = "white"
        self.wheels = "standard"
        self.sunroof = False
        self.body = "Sedan"
        # self.driving_mode = None

    def set_driving_mode(self, driving_mode):
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
