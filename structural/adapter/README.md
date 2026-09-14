# Adapter

## What problem does it solve?

The car expects a charger with `charge()`, but an older charger only provides
`supply_power()`. The two objects cannot work together directly.

## Core Idea

Wrap an existing object with the interface the caller expects.
The adapter translates the call to the wrapped object's interface.

## Car Example

`Car` calls `charge()` on its charger. `LegacyCharger` supplies power through
`supply_power()`. `ChargerAdapter` wraps the legacy charger and connects those
two method names without changing either original class.

## Mental Model

Make something incompatible fit my interface.

## Run

From this pattern folder:

```sh
python example.py
```
