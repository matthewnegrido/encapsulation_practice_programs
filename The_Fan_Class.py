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

    def get_speed(self):
        return self.__speed

    def is_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color