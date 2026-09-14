# State

## What problem does it solve?

Pressing the accelerator should do different things when a car is parked,
running, or moving. Repeating state checks in every car action gets confusing.

## Core Idea

Represent each state as an object that handles the car's actions.
The car delegates to its current state, and that state can trigger a transition.

## Car Example

`StatefulCar` extends the shared Car, holds a state object, and delegates
`start()` and `press_accelerator()` to it. The states are separate objects.
`Parked`
means the engine is off and blocks acceleration; starting changes it to
`Running`, meaning the engine is on but the car is stationary. Accelerating
then changes it to `Moving`, where another press speeds it up. Unlike the
caller-selected driving strategies, these states change in response to actions.
This small example only models the startup-to-moving sequence through those
two actions; it does not combine state checks with the inherited Strategy `drive()`.

## Mental Model

My current state decides what happens next.

## Run

From the repository root:

```sh
python -m behavioral.state.example
```
