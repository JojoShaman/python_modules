class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.growth = 0
        self.age = age
    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
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

my_plants = Plant("Rose", 25, 30)
# def plant_grow(my_plants):
#     my_plants.show()
#     for i in range(1, 8):
#         print(f"=== Day {i} ===")
#         if my_plants.name == "Rose":
#             my_plants.height += 0.8
#             my_plants.growth += 0.8
#         elif my_plants.name == "Sunflower":
#             my_plants.height += 0.5
#             my_plants.growth += 0.5
#         elif my_plants.name == "Cactus":
#             my_plants.height += 0.3
#             my_plants.growth += 0.3
#         my_plants.age += 1
#         my_plants.show()

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    my_plants.show()
    # plant_grow(my_plants)
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        my_plants.grow()
        my_plants.show()
    print(f"Growth this week: {my_plants.growth}cm")