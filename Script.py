traffic_light = "Green"
speed_limit = 60

class Vehicle:
    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):
    def __init__(self, a):
        self.a = a
    def start_engine(self):
        message = "Car engine is started."
        print(message)

class Bike(Vehicle):
    def __init__(self, bike_type):
        self.type = bike_type

    def start_engine(self):
        message = "Bike engine started."
        print(message)

if __name__ == "__main__":
    print(f"traffic_light:- {traffic_light}")
    print(f"speed_limit:- {speed_limit}")

    car = Car("Toyota")
    bike = Bike("Mountain")

    print(f"Car made: {car.a}")
    car.start_engine()

    print(f"Bike type: {bike.type}")
    bike.start_engine()
