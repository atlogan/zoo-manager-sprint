from animals import Animal, Dog, Cat, Bird
import json
import os

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} the {animal.species} added to the zoo.")
        else:
            print("Only Animal objects can be added.")

    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"{name} removed from the zoo.")
                return
        print(f"No animal named {name} found.")