# ==============================
# Assignment 1: Custom Class (Smartphone)
# ==============================

class Device:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    def specs(self):
        print(f"Device: {self._brand} {self._model}")

class Smartphone(Device):
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model)
        self.__storage = storage
        self.__camera = camera

    def specs(self):
        print(f"Smartphone: {self._brand} {self._model}")
        print(f"Storage: {self.__storage}GB")
        print(f"Camera: {self.__camera}MP")

    def take_photo(self):
        print(f"📸 {self._brand} takes a {self.__camera}MP photo!")


# ==============================
# Activity 2: Polymorphism Challenge (Vehicle)
# ==============================

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚢 Sailing on water.")

# ==============================
# Demo / Test Run
# ==============================

def test_assignment():
    print("=== Smartphone Demo ===")
    phone1 = Smartphone("Samsung", "Galaxy S24", 256, 108)
    phone1.specs()
    phone1.take_photo()

def test_polymorphism():
    print("\n=== Polymorphism Demo ===")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()

# ==============================
# Main
# ==============================

if __name__ == "__main__":
    test_assignment()
    test_polymorphism()
