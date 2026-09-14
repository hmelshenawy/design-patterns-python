class Car:
    def start(self):
        print("Car: engine started.")

    def lock(self):
        print("Car: doors locked.")


class StartCarCommand:
    def __init__(self, car):
        self.car = car

    def execute(self):
        self.car.start()


class LockCarCommand:
    def __init__(self, car):
        self.car = car

    def execute(self):
        self.car.lock()


class RemoteControl:
    def __init__(self):
        self.queue = []

    def submit(self, command):
        self.queue.append(command)

    def run(self):
        for command in self.queue:
            command.execute()
        self.queue.clear()


if __name__ == "__main__":
    car, remote = Car(), RemoteControl()
    remote.submit(LockCarCommand(car))
    remote.submit(StartCarCommand(car))
    print("Actions queued; now executing:")
    remote.run()
