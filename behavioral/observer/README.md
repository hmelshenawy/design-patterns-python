# Observer

## What problem does it solve?

Low fuel should alert both the dashboard and a phone. The car should not need
custom notification code for every component interested in its events.

## Core Idea

Interested objects subscribe to an event source. When an event occurs, the
source notifies its subscribers through a common method.

## Car Example

`Car` directly provides `subscribe()`, `unsubscribe()`, and `notify(event)`.
Its `dashboard` is a `Dashboard` from `car/dashboard.py`; it displays warnings
when subscribed. The external `MobileApp` displays notifications. The same
generic notification method handles low-fuel and engine events. After the
phone unsubscribes, only the dashboard receives subsequent events.

## Mental Model

One event tells everyone who subscribed.

## Run

From the repository root:

```sh
python -m behavioral.observer.example
```
