# zoo.py

from animals import Animal

class Zoo:
    def __init__(self):
        # Initialize an empty list to store Animal objects
        self.animals = []

    def add_animal(self, animal: Animal):
        """Adds an Animal object to the zoo."""
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} added to the zoo.")

    def remove_animal(self, name: str):
        """Removes an animal by name using efficient lookup."""
        animal = next((a for a in self.animals if a.name == name), None)
        if animal:
            self.animals.remove(animal)
            print(f"{name} removed from the zoo.")
        else:
            print(f"No animal named {name} found.")

    def list_animals(self):
        """Prints all animals in the zoo with name and species."""
        if not self.animals:
            print("No animals in the zoo.")
        else:
            for animal in self.animals:
                print(f"{animal.name} ({animal.species})")

    def search_animal(self, name: str):
        """Searches for an animal by name (case-insensitive) and prints details."""
        animal = next((a for a in self.animals if a.name.lower() == name.lower()), None)
        if animal:
            print(f"Found: {animal.name} ({animal.species})")
            return animal
        print(f"No animal named {name} found.")
        return None

    def update_animal(self, name: str, new_name: str = None, new_species: str = None):
        """
        Updates an animal's name and/or species if found.
        Only applies changes if new values are provided.
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
        else:
            print("No updates performed.")