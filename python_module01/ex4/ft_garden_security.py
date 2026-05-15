class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.__height = round(height, 1)
        self.__age = age

    def set_height(self, height: float) -> None:
        if height > 0:
            self.__height = round(height, 1)
            print(f"Height updated: {round(self.get_height())}cm")
        else:
            print(f"""{self.name}: Error, height can't be negative"
Height update rejected""")

    def set_age(self, age: int) -> None:
        if age > 0:
            self.__age = age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"""{self.name}: Error, age can't be negative
Age update rejected""")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def show(self) -> None:
        return(f"{self.name}: {(self.get_height())}cm, {self.get_age()} days old")

def ft_garden_security() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 15.0, 10)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(25.0)
    rose.set_age(30)
    print(" ")
    rose.set_height(-25.0)
    rose.set_age(-30)
    print(" ")
    print(f"Current state: {rose.show()}\n")

if __name__ == "__main__":
    ft_garden_security()