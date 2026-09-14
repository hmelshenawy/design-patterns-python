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
| [Builder](creational/builder/) | Creational | Choose a brand, engine, body, color, wheels, and sunroof | Build an object one choice at a time. |
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
a new story each time. Examples share [the Car domain model](common/car.py)
so patterns can later be combined. It holds a brand, basic configuration, and
an optional driving mode.

Factory brands inherit from `Car`; Builder configures a plain `Car`. The other
car examples use small local subclasses to keep charging, startup, pricing,
notifications, remote actions, and state transitions out of the shared model.
Helpers such as chargers, commands, observers, states, and decorators remain
separate objects. Singleton shares settings and needs no Car inheritance.
The examples favor clarity over production features.

## Combining Patterns

- Factory -> creates the car.
- Strategy -> controls its driving behavior.
- Builder -> configures/builds the car.

[examples/combined.py](examples/combined.py) uses Factory to create one BMW,
then switches it from Sport to Eco mode using Strategy. Builder also returns
a shared `Car`, but is kept separate here to keep the demonstration small.

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
namespace packages, so empty `__init__.py` files are unnecessary.
