class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = int(age)

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def test_pet():
    print("\n--- Testing Pet Class ---")

    my_pet = Pet()

    name_input = input("Enter your pet's name: ")
    type_input = input("Enter your pet's animal type (e.g., Dog, Cat, Bird): ")
    age_input = input("Enter your pet's age: ")

    my_pet.set_name(name_input)
    my_pet.set_animal_type(type_input)
    my_pet.set_age(age_input)

    print("\n--- Pet Data Retrieved ---")
    print(f"Pet Name:    {my_pet.get_name()}")
    print(f"Animal Type: {my_pet.get_animal_type()}")
    print(f"Pet Age:     {my_pet.get_age()} years old")

if __name__ == "__main__":
    test_pet()