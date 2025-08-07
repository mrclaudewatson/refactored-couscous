# parent classes

class Animal:
    def __init__(self, name):
        print(f"{name} is an animal.")
        super().__init__(name)  # used to call any class

class CannotFly:
    def __init__(self, name):
        print(f"{name} cannot fly.")



# child class
class Dog(Animal, CannotFly):
    def __init__(self, name):
        print(f"I am a dog named {name}")
        super().__init__(name)


# ---driver portion----
pup = Dog("Pico")
