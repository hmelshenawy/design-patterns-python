# Strategy

## What problem does it solve?

A car can drive in different ways. Putting every driving mode inside the car's
`drive()` method would mix the car with all those behavior choices.

## Core Idea

Put interchangeable behaviors in separate objects with the same interface.
The car delegates to the chosen behavior, which the caller can replace.

## Car Example

`EcoMode`, `SportMode`, and `ComfortMode` each provide a different `drive()`
behavior. `Car` holds the selected mode and calls its method. The example
switches modes on the same car while it runs.

## Mental Model

Which behavior should I use?

## Run

From this pattern folder:

```sh
python example.py
```
