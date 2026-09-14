# Facade

## What problem does it solve?

Starting a car involves several parts. The driver should not have to operate
each part separately or remember the startup order.

## Core Idea

A facade offers a simple interface to several underlying components.
It coordinates their work for the caller.

## Car Example

`Engine`, `FuelSystem`, and `Electronics` each perform one operation.
`StartupCar` extends the shared Car and is the facade: its `start()` method
turns on electronics, checks fuel, and starts the engine through one call.
Its `engine_system` holds the engine component; the shared `engine` field
still describes the engine type. The subsystem objects stay local to this example.

## Mental Model

One simple button coordinates many parts.

## Run

From the repository root:

```sh
python -m structural.facade.example
```
