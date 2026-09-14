# Strategy

## What problem does it solve?

A car can drive in different ways. Putting every driving mode inside the car's
`drive()` method would mix the car with all those behavior choices.

## Core Idea

Put interchangeable behaviors in separate objects with the same interface.
The car delegates to the chosen behavior, which the caller can replace.

## Car Example

`EcoMode`, `SportMode`, and `ComfortMode` each provide a different `drive()`
behavior. The example gets a BMW from `create_car()` and uses the shared Car's
`set_driving_mode()` method to switch between them. The same car delegates
`drive()` to the selected mode. Factory supplies the car; Strategy is the focus
here because its driving behavior changes without creating another car.

## Mental Model

Which behavior should I use?

## Run

From the repository root:

```sh
python -m behavioral.strategy.example
```
