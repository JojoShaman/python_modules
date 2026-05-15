class Plants:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = round(height, 1)
        self.age = age
        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0
        self.shade_count = 0

    def bloom(self) -> None:
        self.bloom_count += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
        self.show_count += 1

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and {round(self.trunk, 1)}cm wide.")
        self.shade_count += 1

    def grow(self, height_plus: float) -> None:
        i = 0
        for i in range(i, round(self.days)):
            self.height += height_plus
        self.grow_count += 1

    def value_plus(self, value_plus: int) -> None:
        i = 0
        for i in range(i, round(self.days)):
            self.value += value_plus

    def age_plus(self, age_plus: int) -> None:
        i = 0
        for i in range(i, round(self.days)):
            self.age += age_plus
        self.age_count += 1

    def stats(self) -> None:
        print(f"Stats: {self.grow_count} grow, "
              f"{self.age_count} age, {self.show_count} show")

    @staticmethod
    def is_year_old(age: int) -> None:
        if (age < 365):
            check = "True"
        else:
            check = "False"
        print(f"is {age} days more than a year? -> {check}")

    @classmethod
    def anonymous(cls, name="Unknown plant", height=0, age=0) # type: ignore
        return cls(name, height, age)


class Flower(Plants):
    def __init__(self, name: str, height: int, age: int,
                 color: str, days: int, value: int) -> None:
        super().__init__(name, height, age)
        self.bloom_count = 0
        self.color = color
        self.days = days
        self.value = value

    def show(self) -> None:
        super().show()
        print(f" color: {self.color}")
        if self.bloom_count == 0:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str, days: int,
                 value: int) -> None:
        super().__init__(name, height, age, color, days, value)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {round(self.value)}")


class Tree(Plants):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk, 1)}cm")

    def stats(self) -> None:
        super().stats()
        print(f"{self.shade_count} shade")


def ft_garden_analytics():
    print("=== Garden statistics ===")
    Plants.is_year_old(30)
    Plants.is_year_old(400)
    print(" ")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red", 1, 0)
    rose.show()
    print("[Statistics for r]")
    rose.stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print("[Statistics for Rose]")
    rose.stats()
    print(" ")

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[Statistics for Oak]")
    oak.stats()
    print("[asking the Oak to produce shade]")
    oak.produce_shade()
    print("[Statistics for Oak]")
    oak.stats()
    print(" ")

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 20, 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(1.5)
    sunflower.value_plus(2.1)
    sunflower.age_plus(1)
    sunflower.bloom()
    sunflower.show()
    print("[Statistics for Sunflower]")
    sunflower.stats()
    print(" ")

    print("=== Anonymous")
    anonymous = Plants.anonymous()
    anonymous.show()
    print("[Statistics for Unknown plant]")
    anonymous.stats()


if __name__ == "__main__":
    ft_garden_analytics()