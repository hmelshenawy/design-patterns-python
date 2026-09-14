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
| [Factory](creational/factory/) | Creational | Create a BMW, Toyota, or Tesla | Which object should I create? |
| [Builder](creational/builder/) | Creational | Choose an engine, color, wheels, and sunroof | Build an object one choice at a time. |
| [Singleton](creational/singleton/) | Creational | Share one CarSettings instance | Everyone uses the same settings object. |
| [Adapter](structural/adapter/) | Structural | Connect an incompatible charger | Make something incompatible fit my interface. |
| [Facade](structural/facade/) | Structural | Start a car with one call | One simple button coordinates many parts. |
| [Decorator](structural/decorator/) | Structural | Wrap a car with Turbo and SportExhaust | Add features by wrapping an object. |
| [Strategy](behavioral/strategy/) | Behavioral | Switch Eco, Sport, and Comfort driving modes | Which behavior should I use? |
| [Observer](behavioral/observer/) | Behavioral | Send low-fuel alerts to a dashboard and phone | One event tells everyone who subscribed. |
| [Command](behavioral/command/) | Behavioral | Queue start and lock actions | Turn an action into an object. |
| [State](behavioral/state/) | Behavioral | Change between Parked, Running, and Moving | My current state decides what happens next. |

## Why always cars?

Every example intentionally uses the same car domain so you can compare the
patterns without learning a new story each time. Focus on how the objects work
together. The examples favor clarity over production features.

## Run an example

Use Python 3. No dependencies or installation steps are needed.
From the repository root:

```sh
python creational/factory/example.py
```

Each pattern folder has its own explanation and a directly executable example.
