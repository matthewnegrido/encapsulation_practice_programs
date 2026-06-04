class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed = max(0, self.__speed - 5)

    def get_speed(self):
        return self.__speed


def test_car():
    print("\n--- Testing Car Class ---")

    # Creating a Car object
    my_car = Car("2026", "CyberTruck")

    # Accelerating 5 times
    print("Accelerating:")
    for _ in range(5):
        my_car.accelerate()
        print(f"  Current speed: {my_car.get_speed()} mph")

    print()

    # Braking 5 times
    print("Braking:")
    for _ in range(5):
        my_car.brake()
        print(f"  Current speed: {my_car.get_speed()} mph")

if __name__ == "__main__":
    test_car()