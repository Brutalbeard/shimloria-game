class Animal():
    def __init__(self, number_of_legs: int = 12) -> None:
        self.number_of_legs: int = number_of_legs

my_animal = Animal(number_of_legs=2)
print(my_animal.number_of_legs == 2) # -> True

class Cat(Animal):
    def __init__(self, number_of_legs: int = 4, sound: str = "Grr") -> None:
        super().__init__(number_of_legs=number_of_legs)
        self.sound: str = sound

    def make_sound(self) -> None:
        print(f"I make the sound: {self.sound}!")

my_cat = Cat(number_of_legs=4, sound="Meow")
print(my_cat.sound) # -> "Meow"
print(my_cat.number_of_legs) # -> 4
my_cat.make_sound() # -> "I make the sound: Meow!"