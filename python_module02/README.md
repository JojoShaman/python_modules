# Python Module 02

## Garden Guardian — Data Engineering for Smart Agriculture

This module introduces exception handling in Python through a smart agriculture monitoring system. The goal is to build **resilient programs** that don't crash when receiving invalid data or encountering unexpected situations.

A program that crashes is a program that fails silently. Exception handling lets you control what happens when something goes wrong, display a useful message, and keep running.

---

## Table of Contents

- [Key Concepts](#key-concepts)
- [Exercises](#exercises)
  - [Ex00 — ft_first_exception](#ex00--ft_first_exception)
  - [Ex01 — ft_raise_exception](#ex01--ft_raise_exception)
  - [Ex02 — ft_different_errors](#ex02--ft_different_errors)
  - [Ex03 — ft_custom_errors](#ex03--ft_custom_errors)
  - [Ex04 — ft_finally_block](#ex04--ft_finally_block)
- [Technical Choices](#technical-choices)

---

## Key Concepts

### try / except

The `try` block contains code that might fail. The `except` block catches the error if it occurs, allowing you to handle it gracefully without crashing the program.

```python
try:
    x = int("abc")
except ValueError as e:
    print(f"Error: {e}")
```

Without `try/except`, this code would crash. With it, the program continues running.

---

### raise

`raise` lets you manually trigger an error. This is useful when a value is technically valid (an integer, for example) but violates business rules (a temperature of 100°C for a plant).

```python
raise ValueError("100°C is too hot for plants (max 40°C)")
```

The message passed as an argument becomes accessible via `e` in the `except` block. Unlike `return`, which ends a function normally, `raise` signals that something went wrong — it propagates up the call stack until something catches it, or the program crashes.

---

### Error Types

Python distinguishes different error types depending on the situation:

| Type                | When                                         |
| ------------------- | -------------------------------------------- |
| `ValueError`        | Wrong value (e.g. `int("abc")`)              |
| `ZeroDivisionError` | Division by zero                             |
| `FileNotFoundError` | File doesn't exist                           |
| `TypeError`         | Incompatible types mixed (e.g. `"abc" + 42`) |
| `Exception`         | Base class of all errors                     |

Using the right type makes code more readable and allows more precise `except` blocks. You can also catch multiple types in a single `except` using a tuple: `except (ValueError, TypeError) as e`.

---

### Custom Exceptions

You can create your own error classes by inheriting from `Exception`. This lets you build a logical hierarchy tailored to your program's domain.

```python
class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)
```

An `except GardenError` catches both `PlantError` and `WaterError`, since they both inherit from `GardenError`. This is the same inheritance principle seen in Module 01 — applied to errors.

---

### finally

The `finally` block always runs, whether an error occurred or not. It's the right place to put cleanup code (closing a connection, releasing a resource) that must execute no matter what.

```python
try:
    water_plant("lettuce")
except PlantError as e:
    print(f"Caught PlantError: {e}")
    return
finally:
    print("Closing watering system")  # always runs, even after return
```

A key detail: `finally` runs even when `return` is called inside `except`. The return is deferred until after `finally` completes.

---

## Exercises

### Ex00 — ft_first_exception

**File:** `ex0/ft_first_exception.py`

First contact with exceptions. `input_temperature()` converts a string to an integer — Python raises a `ValueError` automatically if the conversion fails (e.g. `"abc"`). `test_temperature()` catches it and keeps the program running.

The key insight here: you don't need to manually check if a string is a valid integer. Python already does it when you call `int()`, and raises a `ValueError` with a clear message you can reuse directly.

---

### Ex01 — ft_raise_exception

**File:** `ex1/ft_raise_exception.py`

Building on Ex00, `input_temperature()` now validates the range (0–40°C) and raises its own `ValueError` for out-of-range values. This introduces the idea that **you** decide when something is an error, not just Python.

`test_temperature()` uses a single `for` loop over all test values, with one `try/except` per iteration — so each error is caught independently and the loop continues.

```python
for temp in ["25", "abc", "100", "-50"]:
    try:
        input_temperature(temp)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
```

---

### Ex02 — ft_different_errors

**File:** `ex2/ft_different_errors.py`

Demonstrates that Python has specialized error types for different failure modes. `garden_operations()` triggers four different errors depending on the operation number. All are caught by a single `except Exception as e` block, using `e.__class__.__name__` to display the actual error type dynamically — without using `type()`.

```python
except Exception as e:
    print(f"Caught {e.__class__.__name__}: {e}")
```

---

### Ex03 — ft_custom_errors

**File:** `ex3/ft_custom_errors.py`

Introduces custom exception classes organized through inheritance:

```
Exception
    └── GardenError
            ├── PlantError
            └── WaterError
```

This hierarchy means you can catch errors at the right level of specificity. Catching `PlantError` handles only plant issues. Catching `GardenError` handles all garden-related errors at once.

Each class passes its message up the chain via `super().__init__(message)`, so the standard `str(e)` output works as expected.

---

### Ex04 — ft_finally_block

**File:** `ex4/ft_finally_block.py`

Brings together custom exceptions, `try/except/finally`, and loop logic. The watering system must close whether or not an error occurred — that's the job of `finally`.

When an invalid plant name is found, `except` catches the error, prints the message, and `return` stops the function. But `finally` still runs first, ensuring the system is always properly closed.

Two plant lists are tested in a loop (valid and invalid), keeping the code DRY compared to duplicating `try/except` blocks manually.

---

## Technical Choices

**Why use a `for` loop instead of separate `try/except` blocks?**
Putting each call inside a loop with one `try/except` per iteration means adding a new test case is just adding a value to the list — no structural change needed. Duplicating `try/except` blocks would make the code harder to maintain and read.

**Why `ValueError` for out-of-range temperatures instead of a custom exception?**
A temperature of 100°C is still a wrong _value_ for a plant system — `ValueError` is semantically accurate and keeps error handling uniform in `test_temperature()`. A custom exception would make more sense in a larger system where you need to distinguish plant-specific errors from general input errors.

**Why put `raise` inside `input_temperature()` and not in `test_temperature()`?**
`input_temperature()` owns the validation logic — it knows what a valid temperature is. `test_temperature()` only calls it and handles whatever comes back. This separation of responsibilities makes each function easier to understand and reuse independently.

**Why does `finally` run even after `return`?**
In Python, `finally` is guaranteed to execute before the function actually returns. This is by design — it ensures cleanup always happens, even in early-exit scenarios. This is why it's the right place for resource cleanup like closing files, connections, or hardware interfaces.

**Why inherit custom exceptions from a common `GardenError` base?**
It allows callers to choose their level of specificity. A low-level handler can catch `PlantError` precisely. A top-level handler can catch all `GardenError` at once. This mirrors how Python's own exception hierarchy works — `OSError` catches both `FileNotFoundError` and `PermissionError`, for example.
