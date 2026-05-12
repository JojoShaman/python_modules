class Plants:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

class Flower(Plants):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
    def set_color(self, color):
        self.color = color
    def show(self):
        super().show()
        print(f" color: {self.color}")
    def bloom(self):
        print(f" {self.name} has not bloomed yet")
        print(f"[asking {self.name} to bloom]")
        self.show()
        print(f" {self.name} is blooming beautifully!")

class Tree(Plants):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
    def set_trunk_dia(self, trunk):
        self.trunk = trunk
    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk}")
    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm long and {self.trunk:.1f}cm wide.")

class Vegetable(Plants):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
    def set_growth(self, growth):
        self.growth = growth
    def set_h_season(self, month):
        self.h_season = month
    def set_n_value(self, value):
        self.n_value = value
    def show(self):
        super().show()
        print(f" Harvest season: {self.h_season}")
        print(f" Nutrinional value: {self.n_value}")
    def grow(self):
        print(f"[make tomato grow and age for {self.growth} days]")
        i = 1
        days = range(i, round(self.growth) + 1)
        for i in days:
            self.height += 2.1
            self.age += 1
            self.n_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10)
    rose.set_color("red")
    rose.show()
    rose.bloom()
    print(" ")

    print("=== Tree")
    oak = Tree("Oak", 200, 365)
    oak.set_trunk_dia(5)
    oak.show()
    oak.produce_shade()
    print(" ")

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10)
    tomato.set_h_season("April")
    tomato.set_n_value(0)
    tomato.set_growth(20)
    tomato.show()
    tomato.grow()
    tomato.show()
