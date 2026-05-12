class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    print("=== Garden Plant Registry ===")
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    rose.show()
    sunflower.show()
    cactus.show()