from creational.singleton.example import CarSettings


class Dashboard:
    def __init__(self):
        self.settings = CarSettings()

    def update(self, event):
        print(f"Dashboard warning: {event}")
