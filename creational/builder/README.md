# Builder

## What problem does it solve?

A car has several optional choices. Making all those choices in one long
constructor call can be hard to read.

## Core Idea

Build an object step by step, then ask for the finished result.
Each named step makes a configuration choice easy to see.

## Car Example

`Car` holds the engine, color, wheels, and sunroof choices. `CarBuilder` starts
with a default car and provides methods to configure it. Each method returns
the builder so calls can be chained; `build()` returns its car. Use a new
builder for each new car in this minimal example.

## Mental Model

Build an object one choice at a time.

## Run

From this pattern folder:

```sh
python example.py
```
