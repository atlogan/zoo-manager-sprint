# animals.py

"""Defines the Animal base class and subclasses for the Zoo Manager"""

class Animal:
    """Base class for all animals in the zoo"""
    
    def __init__ (self, name:str, species:str):
        """Initialize an animal with a name and species"""
        self.name = name
        self.species = species

    def make_sound(self):
        """Generic method to be overwritten by subclasses"""
        pass

class Cat(Animal):
    """Cat class that inherits from the Animal class"""

    def make_sound(self):
        """Overrides the generic method and returns a cat sound"""
        return "Meow!"
    
class Dog(Animal):
    """Dog class that inherits from the Animal class"""

    def make_sound(self):
        """Overrides the generic method and returns a dog sound"""
        return "Woof!"
    
class Bird(Animal):
    """Bird class that inherits from the Animal class"""

    def make_sound(self):
        """Overrides the generic method and returns a bird sound"""
        return "Chirp!"