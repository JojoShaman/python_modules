class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} days old")

rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 265)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)

my_plants = [rose, oak, cactus, sunflower, fern]

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    for plants in my_plants:
        plants.show()