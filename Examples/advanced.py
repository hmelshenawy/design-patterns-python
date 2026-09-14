from creational.factory.example import create_car
from behavioral.strategy.example import SportMode, EcoMode, ComfortMode


turboS = create_car("Porsche")
turboS.drive()