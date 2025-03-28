# zoo.py

from animals import Animal

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} added to the zoo.")

    def remove_animal(self, name: str):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"{name} removed from the zoo.")
                return
        print(f"No animal named {name} found.")

    def list_animals(self):
        if not self.animals:
            print("No animals in the zoo.")
        else:
            for animal in self.animals:
                print(animal)