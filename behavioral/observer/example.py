from common.car import Car


class Dashboard:
    def update(self, event):
        print(f"Dashboard warning: {event}")


class MobileApp:
    def update(self, event):
        print(f"Mobile notification: {event}")


class ObservableCar(Car):
    def __init__(self, brand):
        super().__init__(brand)
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def report_low_fuel(self):
        for observer in self.observers:
            observer.update(f"{self.brand}: low fuel, please refuel.")


if __name__ == "__main__":
    car = ObservableCar("BMW")
    dashboard = Dashboard()
    mobile = MobileApp()
    car.subscribe(dashboard)
    car.subscribe(mobile)
    car.report_low_fuel()
    car.unsubscribe(mobile)
    print("After the mobile app unsubscribes:")
    car.report_low_fuel()
