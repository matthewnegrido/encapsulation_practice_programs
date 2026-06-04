class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = color
        self.__on = bool(on)

    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed

    def set_on(self, on):
        self.__on = bool(on)

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = color

    def test_fan():
        print("--- Testing Fan Class ---")

        fan1 = Fan(speed=Fan.FAST, radius=10.0, color="yellow", on=True)

        fan2 = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", on=False)

        print("Fan 1 Properties:")
        print(f"  Speed:  {fan1.get_speed()}")
        print(f"  Radius: {fan1.get_radius()}")
        print(f"  Color:  {fan1.get_color()}")
        print(f"  On:     {fan1.is_on()}")
        print()

        print("Fan 2 Properties:")
        print(f"  Speed:  {fan2.get_speed()}")
        print(f"  Radius: {fan2.get_radius()}")
        print(f"  Color:  {fan2.get_color()}")
        print(f"  On:     {fan2.is_on()}")

    if __name__ == "__main__":
        test_fan()
