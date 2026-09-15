from car.car import Car


class MobileApp:
    def update(self, event):
        print(f"Mobile notification: {event}")


if __name__ == "__main__":
    car = Car("BMW")
    dashboard = car.dashboard
    mobile = MobileApp()
    car.subscribe(dashboard)
    car.subscribe(mobile)
    car.notify("Low fuel, please refuel.")
    car.unsubscribe(mobile)
    print("After the mobile app unsubscribes:")
    car.notify("Low fuel, please refuel.")
    print("_-_-_-_-_-_-_-_-_", car.brand)
    car.notify("Check engine: reduced power.")
