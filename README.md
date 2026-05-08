# python_modules

## Python Fundamentals Through Garden Data

For this first Python module of the 42 curriculum, we are asked to write multiple functions to familiarize ourselves with the fundamentals of the language. There are 7 exercises in total.

---

## Table of Contents

- [ex00 - ft_hello_garden](#ex00---ft_hello_garden)
- [ex01 - ft_garden_name](#ex01---ft_garden_name)
- [ex02 - ft_plot_area](#ex02---ft_plot_area)
- [ex03 - ft_harvest_total](#ex03---ft_harvest_total)
- [ex04 - ft_plant_age](#ex04---ft_plant_age)
- [ex05 - ft_water_reminder](#ex05---ft_water_reminder)
- [ex06 - ft_count_harvest](#ex06---ft_count_harvest-iterative--recursive)
- [ex07 - ft_seed_inventory](#ex07---ft_seed_inventory)

---

### ex00 - ft_hello_garden

The first exercise introduces the most basic building blocks: defining a function and printing output with `print()`.

```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```

**Functions used:**

`print(*objects, sep=' ', end='\n')` — outputs the given objects to the console. Multiple values can be passed and will be separated by `sep` (a space by default). Each call ends with a newline by default.

---

### ex01 - ft_garden_name

Here we discover `input()`, which reads a line from standard input and returns it as a string. We also practice string concatenation with `+`.

```python
def ft_garden_name():
    garden_name = input("Enter garden name: ")
    print("Garden: " + garden_name)
    print("Status: Growing well!")
```

**Functions used:**

`input(prompt)` — displays `prompt` in the console, waits for the user to type something and press Enter, then returns what was typed as a `str`.

---

### ex02 - ft_plot_area

This exercise introduces `int()`, which casts a value to an integer. Its full syntax is `int(value, base)` where `base` defaults to 10. For example, `int("FF", 16)` returns `255`. We also use the multiplication operator `*` for the first time.

```python
def ft_plot_area():
    length = input("Enter length: ")
    width = input("Enter width: ")
    print("Plot area: ", int(length) * int(width))
```

**Functions used:**

`int(value, base=10)` — converts `value` to an integer. Since `input()` always returns a string, wrapping it with `int()` is necessary before doing any arithmetic. The optional `base` parameter lets you parse values in other number systems (binary, hex, etc.).

---

### ex03 - ft_harvest_total

Similar to the previous exercise but using the addition operator `+` to sum values across multiple inputs.

```python
def ft_harvest_total():
    day_one = input("Day 1 harvest: ")
    day_two = input("Day 2 harvest: ")
    day_three = input("Day 3 harvest: ")
    print("Total harvest: ", int(day_one) + int(day_two) + int(day_three))
```

**Functions used:**

Same as ex02: `input()` to read each value and `int()` to convert them before adding.

---

### ex04 - ft_plant_age

This exercise introduces `if/else` conditionals. The syntax is clean and indentation-based — no braces needed.

```python
def ft_plant_age():
    age = input("Enter plant age in days: ")
    if int(age) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
```

**Syntax used:**

```python
if condition:
    # executed if condition is True
else:
    # executed if condition is False
```

The condition is any expression that evaluates to a boolean. Here `int(age) > 60` returns `True` or `False` depending on the value entered.

---

### ex05 - ft_water_reminder

We combine `input()` with a conditional check to build a simple decision tool. If the plant hasn't been watered in over 2 days, it prompts the user to act.

```python
def ft_water_reminder():
    days = input("Days since last watering: ")
    if int(days) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
```

**Syntax used:**

Same `if/else` structure as ex04, applied to a different real-world condition.

---

### ex06 - ft_count_harvest (iterative & recursive)

This exercise has two versions implementing the same logic — printing each day from 1 to N — to illustrate the difference between **iterative** and **recursive** approaches.

#### Iterative

Uses a `for` loop over a `range()` to go through each day sequentially.

```python
def ft_count_harvest_iterative():
    days = input("Days until harvest: ")
    for i in range(1, int(days) + 1):
        print("Day: ", i)
```

**Syntax used:**

```python
for variable in iterable:
    # executed for each element
```

`range(start, stop)` — generates a sequence of integers from `start` (inclusive) to `stop` (exclusive). So `range(1, int(days) + 1)` produces `1, 2, ..., days`.

#### Recursive

Uses a helper function that calls itself with an incremented counter until it exceeds the target.

```python
def ft_count_helper(days, current):
    if current > days:
        return
    print("Day: ", current)
    ft_count_helper(days, current + 1)

def ft_count_harvest_recursive():
    days = input("Days until harvest: ")
    ft_count_helper(int(days), 1)
```

**Syntax used:**

A recursive function calls itself. It requires a **base case** (`if current > days: return`) to stop the recursion, otherwise it would run forever. Each call works on a smaller sub-problem (incrementing `current`) until the base case is reached.

The two implementations produce identical output. The iterative version is more efficient in Python since the language does not optimize tail recursion, but the recursive version is a useful exercise in thinking about base cases and call stacks.

---

### ex07 - ft_seed_inventory

This exercise introduces typed function parameters and return type hints. The function takes a seed type, quantity, and unit, then formats the output using `elif` chains and the `capitalize()` string method.

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print(seed, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(seed, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(seed, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
```

**Syntax used:**

`def function(param: type, ...) -> return_type` — type hints are optional in Python but improve readability and help tools like linters catch type errors. `-> None` means the function returns nothing.

```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```

`elif` (short for "else if") chains multiple conditions together. Python evaluates them top to bottom and executes the first matching branch.

`str.capitalize()` — returns a copy of the string with the first character uppercased and the rest lowercased. `"tomato".capitalize()` → `"Tomato"`.
