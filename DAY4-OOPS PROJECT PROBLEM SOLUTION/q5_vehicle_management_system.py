class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display(self):
        super().display()
        print(f"Fuel Type: {self.fuel_type}")


class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def display(self):
        super().display()
        print(f"Engine Capacity: {self.engine_capacity}")


if __name__ == "__main__":
    car = Car("Toyota", "Corolla", "Petrol")
    bike = Bike("Honda", "CBR", "150cc")

    print("Car Details")
    car.display()

    print("\nBike Details")
    bike.display()
