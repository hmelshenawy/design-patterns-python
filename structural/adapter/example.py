from car.car import Car


class LegacyCharger:
    def supply_power(self):
        print("Legacy charger: supplying power.")


class ChargerAdapter:
    def __init__(self, legacy_charger):
        self.legacy_charger = legacy_charger

    def charge(self):
        print("Adapter: translating charge() to supply_power().")
        self.legacy_charger.supply_power()


if __name__ == "__main__":
    old_charger = LegacyCharger()
    compatible_charger = ChargerAdapter(old_charger)
    car = Car("Tesla")
    car.engine = "electric"
    car.charge_with(compatible_charger)
