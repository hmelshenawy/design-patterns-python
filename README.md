# Design Patterns explained through cars

Design patterns are reusable ideas for solving common software design problems.
They help you decide how to create objects, connect them, and share responsibilities.
This is a small Python cheat sheet, not a real car application.

## Three categories

- **Creational:** how objects are created.
- **Structural:** how objects fit together.
- **Behavioral:** how objects act and communicate.

## Cheat sheet

| Pattern | Category | Car Example | Mental Model |
| --- | --- | --- | --- |
| [Factory](creational/factory/) | Creational | Create a BMW, Porsche, or Tesla | Which object should I create? |
| [Builder](creational/builder/) | Creational | Configure an existing car's engine, body, color, wheels, and sunroof | Build an object one choice at a time. |
| [Singleton](creational/singleton/) | Creational | Share one CarSettings instance | Everyone uses the same settings object. |
| [Adapter](structural/adapter/) | Structural | Connect an incompatible charger | Make something incompatible fit my interface. |
| [Facade](structural/facade/) | Structural | Start a car with one call | One simple button coordinates many parts. |
| [Decorator](structural/decorator/) | Structural | Wrap a car with Turbo and SportExhaust | Add features by wrapping an object. |
| [Strategy](behavioral/strategy/) | Behavioral | Switch Eco, Sport, and Comfort driving modes | Which behavior should I use? |
| [Observer](behavioral/observer/) | Behavioral | Send low-fuel alerts to a dashboard and phone | One event tells everyone who subscribed. |
| [Command](behavioral/command/) | Behavioral | Queue start and lock actions | Turn an action into an object. |
| [State](behavioral/state/) | Behavioral | Change between Parked, Running, and Moving | My current state decides what happens next. |

## Why always cars?

All patterns use the same Car world so you can compare them without learning
a new story each time. Examples share [the Car domain model](car/car.py).
It holds the car's configuration, driving mode, state, subscribers, and components.

Factory brands inherit from `Car`; Builder configures the exact object it receives.
Every pattern works with this shared model. The car owns its
[Dashboard](car/dashboard.py) and [startup components](car/components.py).
[DrivingMode](car/driving_mode.py) supplies a name; concrete strategies keep
their behavior in the Strategy folder. States, commands, observers, chargers,
and decorators remain small separate objects, with no special Car subclasses
for individual patterns. Only the three Factory brands inherit from Car.

This is a teaching model: `drive()` delegates the driving style to Strategy,
while `start()` and `press_accelerator()` demonstrate State transitions.
Decorators wrap the pricing interface; they do not forward every Car method.

## Combining Patterns

- Factory -> creates the car.
- Strategy -> controls its driving behavior.
- Builder -> configures the existing car without replacing it.

[main.py](main.py) demonstrates all ten patterns around one Porsche: Factory
creates it, Builder configures it as a red V8 coupe, Strategy switches driving
modes, and Observer notifies its dashboard and a phone. The same car also uses
shared settings, startup coordination, queued commands, state transitions,
feature pricing, and a battery charger adapter.

From the `design-patterns-python` repository root:

```sh
python main.py
```

[examples/combined.py](examples/combined.py) preserves the smaller Porsche
demonstration of Factory, Builder, Strategy, and Observer.

```sh
python -m examples.combined
```

The existing [Porsche example](examples/advanced.py) also uses Factory and Strategy.

```sh
python -m examples.advanced
```

## Run an example

Use Python 3. No dependencies or installation steps are needed.
Run commands from the `design-patterns-python` repository root:

```sh
python -m creational.factory.example
```

Each pattern folder has its own explanation and module run command. Module
execution makes absolute imports resolve from the repository root; no path
changes or installation are needed. Python 3 supports these folders as
namespace packages. The central `car/` domain has its own `__init__.py`;
the pattern folders need no package boilerplate.
