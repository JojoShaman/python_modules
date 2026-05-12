**keywords:** `Imperative programming` `OOP` `Python` `Basics` **skills:** `Object-oriented programming` `Rigor` `Imperative programming`

# Python Module 01

## Object-Oriented Programming Through Garden Data

For this second Python module of the 42 curriculum, we explore the fundamentals of object-oriented programming in Python. There are 7 exercises in total.

---

## Table of Contents

- [ex00 - ft_garden_intro](#ex00---ft_garden_intro)
- [ex01 - ft_garden_data](#ex01---ft_garden_data)
- [ex02 - ft_plant_growth](#ex02---ft_plant_growth)
- [ex03 - ft_plant_factory](#ex03---ft_plant_factory)
- [ex04 - ft_garden_security](#ex04---ft_garden_security)
- [ex05 - ft_plant_types](#ex05---ft_plant_types)
- [ex06 - ft_garden_analytics](#ex06---ft_garden_analytics)

---

### ex00 - ft_garden_intro

This exercise introduces the most basic building block of a Python program: the entry point. Before writing classes or complex logic, we need to understand how Python decides where to start execution.

```python
def ft_garden_intro():
    print("=== Welcome to My Garden ===")
    print("Plant: Rose")
    print("Height: 25cm")
    print("Age: 30 days")
    print(" ")
    print("=== End of Program ===")

if __name__ == "__main__":
    ft_garden_intro()
```

**Syntax used:**

`def function_name():` — defines a reusable block of code. Calling it executes all the indented lines inside.

`if __name__ == "__main__":` — a special Python pattern that checks whether the file is being run directly or imported as a module. Code inside this block only runs when the file is executed directly with `python3`. This is a fundamental good practice in Python that prepares for the concept of imports in future projects.

---

### ex01 - ft_garden_data

This exercise introduces the concept of a **class** in Python. A class is a blueprint for creating objects. We define a `Plant` class with an `__init__` method to initialize its attributes and a `show()` method to display them.

```python
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
```

**Syntax used:**

`class ClassName:` — defines a new class. By convention, class names use PascalCase.

`def __init__(self, ...)` — the constructor method, called automatically when an instance is created. `self` refers to the instance being created and is always the first parameter.

`self.attribute = value` — assigns a value to an instance attribute. Each instance keeps its own copy of these values.

`f"{variable}"` — an f-string, which allows embedding expressions directly inside string literals for clean and readable formatting.

---

### ex02 - ft_plant_growth

This exercise focuses on simulating plant growth over time. The `grow()` method updates the plant's height and age differently depending on the plant's name, and a `growth` attribute tracks the total increase over time.

```python
def grow(self):
    if self.name == "Rose":
        self.height += 0.8
        self.growth += 0.8
    elif self.name == "Sunflower":
        self.height += 0.5
        self.growth += 0.5
    elif self.name == "Cactus":
        self.height += 0.3
        self.growth += 0.3
    self.age += 1
```

**Syntax used:**

`self.attribute += value` — increments an attribute in place. Equivalent to `self.attribute = self.attribute + value`.

`elif` — short for "else if", chains multiple conditions together. Python evaluates them top to bottom and executes the first matching branch.

The `__main__` block calls `grow()` repeatedly inside a `for` loop to simulate a week of growth, then reads `self.growth` to display the total weekly increase.

---

### ex03 - ft_plant_factory

Here we create multiple instances of the `Plant` class and store them in a **list**. We then iterate over the list with a `for` loop to call `show()` on each plant.

```python
my_plants = [rose, oak, cactus, sunflower, fern]

if __name__ == "__main__":
    for plants in my_plants:
        plants.show()
```

**Syntax used:**

`[item1, item2, ...]` — a list literal. Lists are ordered, mutable sequences that can hold any type of object, including class instances.

```python
for variable in iterable:
    # executed for each element
```

Iterating over a list of objects allows us to call methods on each one without repeating code. Each plant is created by passing its values directly to `__init__`, making each instance immediately ready to use.

---

### ex04 - ft_garden_security

This exercise introduces **encapsulation** through private attributes and getter/setter methods with validation logic. Invalid values are rejected with an error message, leaving the data unchanged.

```python
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self):
        return self.__height
```

**Syntax used:**

`self.__attribute` — the double underscore prefix triggers **name mangling** in Python, making the attribute private. It cannot be accessed directly from outside the class.

`get_*` and `set_*` methods — also called **getters** and **setters**, these are the controlled interface to read and write private attributes. The setter enforces validation rules before applying any change, protecting data integrity.

---

### ex05 - ft_plant_types

This exercise introduces **inheritance**. A parent class `Plants` holds the common features, and three subclasses — `Flower`, `Tree`, and `Vegetable` — extend it with their own attributes and methods.

```python
class Flower(Plants):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)

    def show(self):
        super().show()
        print(f" color: {self.color}")

    def bloom(self):
        print(f" {self.name} has not bloomed yet")
        print(f"[asking {self.name} to bloom]")
        self.show()
        print(f" {self.name} is blooming beautifully!")
```

**Syntax used:**

`class Child(Parent):` — declares a subclass that inherits all attributes and methods from the parent.

`super().__init__(...)` — calls the parent class constructor to initialize the shared attributes, avoiding code duplication.

`super().show()` — calls the parent's version of `show()`, then adds the subclass-specific output on top. This is **method overriding**: redefining a method in the subclass while still reusing the parent's logic.

---

### ex06 - ft_garden_analytics

This exercise brings everything together. It extends the previous classes with usage counters, a `@staticmethod` to check plant age, a `@classmethod` to create anonymous plants, and a `Seed` class that inherits from `Flower` and tracks the number of seeds after blooming.

```python
@staticmethod
def is_year_old(age):
    if (age < 365):
        check = "True"
    else:
        check = "False"
    print(f"is {age} days more than a year? -> {check}")

@classmethod
def anonymous(cls, name="Unknown plant", height=0, age=0):
    return cls(name, height, age)
```

**Syntax used:**

`@staticmethod` — marks a method that belongs to the class but receives neither `self` nor `cls`. Called directly on the class: `Plants.is_year_old(30)`. Used here for a utility check that doesn't need any instance data.

`@classmethod` — marks a method that receives the class itself as `cls`. Used here as an alternative constructor to create a plant when not all information is available. Since `cls` refers to the class it's called on, `Plants.anonymous()` creates a `Plants` instance with default values.

**Counters** — `grow_count`, `age_count`, `show_count`, and `shade_count` are initialized in `__init__` and incremented inside their respective methods, then displayed via `stats()`. This tracks how many times each operation has been performed on a given plant.

**Inheritance chain** — `Seed` inherits from `Flower`, which inherits from `Plants`, forming a three-level hierarchy. `super()` is used at each level to delegate initialization and method calls to the parent.
