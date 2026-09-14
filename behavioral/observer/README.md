# Observer

## What problem does it solve?

Low fuel should alert both the dashboard and a phone. The car should not need
custom notification code for every component interested in its events.

## Core Idea

Interested objects subscribe to an event source. When an event occurs, the
source notifies its subscribers through a common method.

## Car Example

`ObservableCar` extends the shared Car with a subscriber list and reports a
low-fuel event to each subscriber's `update()` method. `Dashboard` displays a
warning and `MobileApp` displays a notification. Neither observer is a car.
After the phone unsubscribes, only the dashboard receives the next event.

## Mental Model

One event tells everyone who subscribed.

## Run

From the repository root:

```sh
python -m behavioral.observer.example
```
