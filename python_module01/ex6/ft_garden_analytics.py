class Plants:
    def __init__(self, name="Unknown plant", height=0, age=0):
        self.name = name
        self.height = height
        self.age = age
        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0
        self.shade_count = 0
    def bloom(self):
        self.bloom_count += 1
    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self.show_count += 1
    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm long and {self.trunk:.1f}cm wide.")
        self.shade_count += 1
    def grow(self, height_plus, age_plus, value_plus):
        i = 1
        self.range = range(i, round(self.days) + 1)
        for i in self.range:
            self.height += height_plus
            self.age += age_plus
            self.value += value_plus
        if age_plus > 0:
            self.age_count += 1
        self.grow_count += 1
    def stats(self):
        print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")
    @staticmethod
    def is_year_old(age):
        if (age < 365):
            check = "True"
        else:
            check = "False"
        print(f"is {age} days more than a year? -> {check}")
    
class Flower(Plants):
    def __init__(self, name, height, age, color, days, value):
        super().__init__(name, height, age)
        self.bloom_count = 0
        self.color = color
        self.days = days
        self.value = value
    def show(self):
        super().show()
        print(f" color: {self.color}")
        if self.bloom_count == 0:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

class Seed(Flower):
    def __init__(self, name, height, age, color, days, value, value_plus, height_plus, age_plus):
        super().__init__(name, height, age, color, days, value)
        self.value_plus = value_plus
        self.height_plus = height_plus
        self.age_plus = age_plus
    def show(self):
        super().show()
        print(f" Seeds: {round(self.value)}")
    def grow_age_bloom(self):
        super().grow(self.height_plus, self.age_plus, self.value_plus)
        super().bloom()


class Tree(Plants):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk = trunk
    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk:.1f}cm")
    def stats(self):
        super().stats()
        print(f"{self.shade_count} shade")

class Vegetable(Plants):
    def __init__(self, name, height, age, month, value, value_plus, height_plus, age_plus, days):
        super().__init__(name, height, age)
        self.h_season = month
        self.value = value
        self.value_plus = value_plus
        self.height_plus = height_plus
        self.age_plus = age_plus
        self.days = days
    def show(self):
        super().show()
        print(f" Harvest season: {self.h_season}")
        print(f" Nutrinional value: {self.value}")
    def grow(self):
        print(f"[make {self.name} grow and age for {self.days} days]")
        super().grow(self.height_plus, self.age_plus, self.value_plus)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    Plants.is_year_old(30)
    Plants.is_year_old(400)
    print(" ")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red", 1, 0)
    rose.show()
    print("[Statistics for Rose]")
    rose.stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8, 0, 0)
    rose.bloom()
    rose.show()
    print("[Statistics for Rose]")
    rose.stats()
    print(" ")

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[Statistics for Oak]")
    oak.stats()
    print(f"[asking the Oak to produce shade]")
    oak.produce_shade()
    print("[Statistics for Oak]")
    oak.stats()
    print(" ")

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0, 1, 2.1, 1, 20)
    tomato.show()
    tomato.grow()
    tomato.show()
    print(" ")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", 20, 0, 2.1, 1.5, 1)
    sunflower.show()
    print(f"[make sunflower grow, age and bloom]")
    sunflower.grow_age_bloom()
    sunflower.show()
    print("[Statistics for Sunflower]")
    sunflower.stats()    
    print(" ")

    print("=== Anonymous")
    anonymous = Plants()
    anonymous.show()
    print("[Statistics for Unknown plant]")
    anonymous.stats()