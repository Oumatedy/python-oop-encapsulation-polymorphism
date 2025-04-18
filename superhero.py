# ========================
# Assignment 1: Superhero Class
# ========================

class Character:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def intro(self):
        print(f"I am {self.name} from {self.origin}!")


class Superhero(Character):
    def __init__(self, name, origin, power, weakness):
        super().__init__(name, origin)
        self.__power = power
        self.__weakness = weakness

    def intro(self):
        print(f"🦸‍♂️ Superhero: {self.name} from {self.origin}!")
        print(f"   Power: {self.__power}")
        print(f"   Weakness: {self.__weakness}")

    def use_power(self):
        print(f"{self.name} uses {self.__power}! 💥")


if __name__ == "__main__":
    hero = Superhero("Voltman", "Electric City", "Lightning Strike", "Water")
    hero.intro()
    hero.use_power()
