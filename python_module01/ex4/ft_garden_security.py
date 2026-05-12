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
    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
    def get_height(self):
        return self.__height
    def get_age(self):
        return self.__age
    def show(self):
        print(f"Created: {self.name}: {self.get_height():.1f}cm, {self.get_age()} days old")

rose = Plant("Rose", 15, 10)

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose.show()
    print(" ")
    rose.set_height(25)
    rose.set_age(30)
    print(" ")
    rose.set_height(-25)
    rose.set_age(-30)
    print(" ")
    print(f"Current state: rose: {rose.get_height():.1f}cm, {rose.get_age()} days old")
