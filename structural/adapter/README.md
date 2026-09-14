# Adapter

## What problem does it solve?

The car expects a charger with `charge()`, but an older charger only provides
`supply_power()`. The two objects cannot work together directly.

## Core Idea

Wrap an existing object with the interface the caller expects.
The adapter translates the call to the wrapped object's interface.

## Car Example

`ElectricCar` extends the shared Car with `charge_with()`, which calls
`charge()` on its charger. `LegacyCharger` supplies power through
`supply_power()`. `ChargerAdapter` wraps the legacy charger and connects those
two method names without changing either original interface. The adapter is
a charger wrapper, not a car.

## Mental Model

Make something incompatible fit my interface.

## Run

From the repository root:

```sh
python -m structural.adapter.example
```
