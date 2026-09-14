# Facade

## What problem does it solve?

Starting a car involves several parts. The driver should not have to operate
each part separately or remember the startup order.

## Core Idea

A facade offers a simple interface to several underlying components.
It coordinates their work for the caller.

## Car Example

`Engine`, `FuelSystem`, and `Electronics` each perform one operation.
`Car` is the facade: its `start()` method turns on electronics, checks fuel,
and starts the engine through one call.

## Mental Model

One simple button coordinates many parts.

## Run

From this pattern folder:

```sh
python example.py
```
