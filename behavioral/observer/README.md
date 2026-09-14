# Observer

## What problem does it solve?

Low fuel should alert both the dashboard and a phone. The car should not need
custom notification code for every component interested in its events.

## Core Idea

Interested objects subscribe to an event source. When an event occurs, the
source notifies its subscribers through a common method.

## Car Example

`Car` keeps subscribers and reports a low-fuel event to each one's `update()`
method. `Dashboard` displays a warning and `MobileApp` displays a notification.
After the phone unsubscribes, only the dashboard receives the next event.

## Mental Model

One event tells everyone who subscribed.

## Run

From this pattern folder:

```sh
python example.py
```
