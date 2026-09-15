# Facade

## What problem does it solve?

Starting a car involves several parts. The driver should not have to operate
each part separately or remember the startup order.

## Core Idea

A facade offers a simple interface to several underlying components.
It coordinates their work for the caller.

## Car Example

`Engine`, `FuelSystem`, and `Electronics` live in `car/components.py` and
belong to the shared Car. `CarStartup(car)` is a facade holding that existing
car. Its `start()` turns on electronics, checks fuel, and calls `car.start()`.
The car's state starts the engine when needed. The `engine_system` component
is separate from the `engine` field describing the engine type. No new car is created.

## Mental Model

One simple button coordinates many parts.

## Run

From the repository root:

```sh
python -m structural.facade.example
```
