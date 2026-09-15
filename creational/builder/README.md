# Builder

## What problem does it solve?

A car has several optional choices. Making all those choices in one long
constructor call can be hard to read.

## Core Idea

Build an object step by step, then ask for the finished result.
Each named step makes a configuration choice easy to see.

## Car Example

The shared `car.car.Car` holds the brand, engine, body, color, wheels, and
sunroof choices. `CarBuilder(car)` accepts an existing car and configures it
step by step. Each method returns the builder so calls can be chained;
`build()` returns that exact car, not a copy. A factory-created Porsche keeps
its identity and class. Builder does not select driving strategies.

## Mental Model

Build an object one choice at a time.

## Run

From the repository root:

```sh
python -m creational.builder.example
```
