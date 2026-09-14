# Factory

## What problem does it solve?

You want a car for a chosen brand without repeating the creation decisions
everywhere you need a car.

## Core Idea

A factory chooses and creates an object for its caller. This example uses a
Simple Factory function, not the inheritance-based Factory Method variant.

## Car Example

`BMW`, `Toyota`, and `Tesla` are different cars with the same `drive()` method.
`create_car()` chooses the class from a brand name and returns a new car.
The caller can drive the result without knowing its class.

## Mental Model

Which object should I create?

## Run

From this pattern folder:

```sh
python example.py
```
