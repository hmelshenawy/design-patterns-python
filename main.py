from creational.factory.example import car_factory
from creational.builder.example import CarBuilder
from behavioral.strategy.example import SportMode, EcoMode
from behavioral.observer.example import MobileApp
from behavioral.command.example import StartCarCommand, LockCarCommand, RemoteControl
from structural.facade.example import CarStartup
from structural.decorator.example import Turbo, SportExhaust
from structural.adapter.example import ChargerAdapter, LegacyCharger


def main():
    # Factory creates the one car used throughout this demonstration.
    original_car = car_factory("Porsche")

    # Builder configures that same object, preserving its identity.
    turboS = (CarBuilder(original_car).with_engine("V8").with_color("Red")
           .with_body("Coupe").build())
    print("Factory and Builder use the same car:", turboS is original_car)
    turboS.describe()

    # Singleton: the car and its dashboard share settings.
    turboS.settings.language = "Arabic"
    print("Shared settings:", turboS.settings is turboS.dashboard.settings)
    print("Dashboard language:", turboS.dashboard.settings.language)

    # Observer: the car notifies its own dashboard and an external phone.
    mobile = MobileApp()
    turboS.subscribe(turboS.dashboard)
    turboS.subscribe(mobile)

    # Facade coordinates the car's components; State tracks engine startup.
    CarStartup(turboS).start()

    # Strategy delegates driving behavior to interchangeable modes.
    turboS.set_driving_mode(SportMode())
    turboS.drive()
    turboS.set_driving_mode(EcoMode())
    turboS.drive()

    # State handles acceleration: Running -> Moving, then speeding up.
    turboS.press_accelerator()
    turboS.press_accelerator()
    turboS.notify("Low fuel, please refuel.")
    turboS.unsubscribe(mobile)
    turboS.notify("Check Brake Pads")

    # Command queues actions on the same car; its engine is already on.
    remote = RemoteControl()
    remote.submit(StartCarCommand(turboS))
    remote.submit(LockCarCommand(turboS))
    remote.run()

    # Decorator wraps this car's pricing interface without replacing it.
    upgraded_car = SportExhaust(Turbo(turboS))
    print(f"{upgraded_car.description()}: ${upgraded_car.cost():,}")

    # Adapter connects a legacy charger to the car's battery interface.
    turboS.charge_with(ChargerAdapter(LegacyCharger()))


if __name__ == "__main__":
    main()
