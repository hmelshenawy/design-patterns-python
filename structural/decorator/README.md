# Decorator

## What problem does it solve?

Cars can have many combinations of optional features. Creating a separate car
class for every possible combination would quickly become confusing.

## Core Idea

Wrap an object to add behavior while keeping the same interface.
Wrappers can be stacked to combine features.

## Car Example

The shared `Car` supplies `description()` and `cost()` with a simple teaching price.
`Turbo` and `SportExhaust` wrap
any object with `description()` and `cost()`, call those methods, and add
their own feature and price. Both wrappers keep those same methods, so an
exhaust can wrap a turbo-equipped car. This is the object design pattern,
not Python's `@decorator` syntax. The wrappers preserve the pricing interface;
they do not inherit from Car or forward its other methods.

## Mental Model

Add features by wrapping an object.

## Run

From the repository root:

```sh
python -m structural.decorator.example
```
