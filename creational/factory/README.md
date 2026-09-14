# Factory

## What problem does it solve?

You want a car for a chosen brand without repeating the creation decisions
everywhere you need a car.

## Core Idea

A factory chooses and creates an object for its caller. This example uses a
Simple Factory function, not the inheritance-based Factory Method variant.

## Car Example

`BMW`, `Porsche`, and `Tesla` inherit from the shared `common.car.Car`.
`create_car()` chooses the concrete class from a brand name and returns a new
car. The example prints which car was created. Factory chooses the object;
it does not choose or implement driving behavior.

## Mental Model

Which object should I create?

## Run

From the repository root:

```sh
python -m creational.factory.example
```
