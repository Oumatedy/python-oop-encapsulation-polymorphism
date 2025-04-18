# ========================
# Activity 2: Animal Polymorphism
# ========================

class Animal:
    def move(self):
        print("The animal moves.")

class Dog(Animal):
    def move(self):
        print("🐕 The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("🕊️ The bird flies in the sky.")

class Snake(Animal):
    def move(self):
        print("🐍 The snake slithers silently.")


if __name__ == "__main__":
    animals = [Dog(), Bird(), Snake()]
    for animal in animals:
        animal.move()
