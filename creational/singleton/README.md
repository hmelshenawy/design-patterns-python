# Singleton

## What problem does it solve?

The car dashboard and MBUX infotainment system need to share settings. Separate settings objects
could disagree about whether distances use kilometers or miles.

## Core Idea

A singleton returns the same instance each time it is requested.
Changes made through one reference are visible through the others.

## Car Example

`CarSettings` stores distance units, language, and brightness. Python's `__new__()` method creates an
object before initialization; here it creates the instance only once and
returns that saved instance on later calls. The dashboard and MBUX references
therefore share one object within this Python process. This teaching example
does not handle concurrent creation or subclasses. The example changes language
and units through the dashboard reference. Settings belong to the car world,
but are not a Car and do not need to inherit from the shared model.
The shared Car and its Dashboard also obtain this same settings instance.

## Mental Model

Everyone uses the same settings object.

## Run

From the repository root:

```sh
python -m creational.singleton.example
```
