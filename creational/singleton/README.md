# Singleton

## What problem does it solve?

The car dashboard and GPS need to share settings. Separate settings objects
could disagree about whether distances use kilometers or miles.

## Core Idea

A singleton returns the same instance each time it is requested.
Changes made through one reference are visible through the others.

## Car Example

`CarSettings` stores distance units. Python's `__new__()` method creates an
object before initialization; here it creates the instance only once and
returns that saved instance on later calls. The dashboard and GPS references
therefore share one object within this Python process. This teaching example
does not handle concurrent creation or subclasses.

## Mental Model

Everyone uses the same settings object.

## Run

From this pattern folder:

```sh
python example.py
```
