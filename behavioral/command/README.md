# Command

## What problem does it solve?

A remote control needs to queue car actions for later. It should not need to
know the details of starting the engine or locking the doors.

## Core Idea

Represent a request as an object containing its receiver and action.
Another object can store the request and execute it later through a common method.

## Car Example

The shared `Car` receives start and lock actions. Starting delegates to its
current state, so an already-running engine is not restarted. `StartCarCommand` and
`LockCarCommand` each hold a car and expose `execute()`. `RemoteControl`
queues those command objects, executes them in order, and clears the queue.

## Mental Model

Turn an action into an object.

## Run

From the repository root:

```sh
python -m behavioral.command.example
```
