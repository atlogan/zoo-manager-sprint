import json
import logging
from animals import Animal, Dog, Cat, Bird
import os

logging.basicConfig(filename="zoo.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def save_animals(zoo, filename="zoo_data.json"):
    """Save the list of zoo animals"""
    try:
        if not hasattr(zoo, 'animals') or not hasattr(zoo.animals, '__iter__'):
            logging.error("Zoo object doesn't have a valid animals attribute")
            return False
            
        data = []
        for animal in zoo.animals:
            animal_data = {
                "name": animal.name,
                "species": animal.species,
                "type": type(animal).__name__,
            }
            data.append(animal_data)
            
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Animals saved successfully to {filename}.")
        return True
    except Exception as e:
        logging.error(f"Error saving animals to file: {e}")
        return False

def load_animals(zoo, filename="zoo_data.json"):
    """Load animals from a JSON file and add them to the zoo."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        
        for item in data:
            # Validate required fields are present
            if not all(key in item for key in ["name", "species", "type"]):
                logging.warning(f"Skipping invalid animal entry: {item}")
                continue
                
            name = item["name"]
            species = item["species"]
            animal_type = item["type"]
            
            if animal_type == "Dog":
                animal = Dog(name, species)
            elif animal_type == "Cat":
                animal = Cat(name, species)
            elif animal_type == "Bird":
                animal = Bird(name, species)
            else:
                animal = Animal(name, species)  # Default to generic Animal
            
            zoo.add_animal(animal)
        logging.info(f"Animals loaded successfully from {filename}.")
        return True
    except FileNotFoundError:
        logging.warning(f"Error: {filename} not found. Starting with an empty zoo.")
        return False
    except json.JSONDecodeError:
        logging.error(f"Error: Failed to decode {filename}. File may be corrupted.")
        return False
    except Exception as e:
        logging.error(f"Unexpected error loading animals: {e}")
        return False

def check_save_file_exists(filename="zoo_data.json"):
    """Check if the save file exists.
    
    Returns:
        bool: True if file exists, False otherwise
    """
    exists = os.path.isfile(filename)
    if not exists:
        logging.info(f"Save file {filename} does not exist")
    return exists