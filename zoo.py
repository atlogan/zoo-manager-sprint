# zoo.py

from animals import Animal

class Zoo:
    def __init__(self):
        # Initialize an empty list to store Animal objects
        self.animals = []

    def add_animal(self, animal: Animal):
        """Adds an Animal object to the zoo's collection."""
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} added to the zoo.")

    def remove_animal(self, name: str):
        """Removes an animal from the zoo by name."""
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"{name} removed from the zoo.")
                return
        print(f"No animal named {name} found.")

    def list_animals(self):
        """Lists all animals currently in the zoo."""
        if not self.animals:
            print("No animals in the zoo.")
        else:
            for animal in self.animals:
                print(animal)

    def search_animal(self, name: str):
        """Searches for an animal by name (case-insensitive)."""
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                print(f"Found: {animal}")
                return animal
        print(f"No animal named {name} found.")
        return None

    def update_animal(self, name: str, new_name: str = None, new_species: str = None):
        """
        Updates an animal's name and/or species by searching for its current name.
        Only changes values that are explicitly provided.
        """
        animal = self.search_animal(name)
        if animal:
            if new_name:
                print(f"Changing name from {animal.name} to {new_name}")
                animal.name = new_name
            if new_species:
                print(f"Changing species from {animal.species} to {new_species}")
                animal.species = new_species
            print("Animal updated successfully.")
