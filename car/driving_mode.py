class DrivingMode:
    def __init__(self):
        self.name = type(self).__name__



class EcoMode(DrivingMode):
    def drive(self):
        print("Eco: accelerate gently to save energy.")


class SportMode(DrivingMode):
    def drive(self):
        print("Sport: accelerate quickly for a lively drive.")


class ComfortMode(DrivingMode):
    def drive(self):
        print("Comfort: accelerate smoothly for a relaxed ride.")