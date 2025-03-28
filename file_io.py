import json
import logging
from animals import Animal, Dog, Cat

logging.basicConfig(filename="zoo.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def save_animals(zoo, filename="zoo_data.json"):
    """Save the list of zoo animals"""
    try:
        data = []
        for animal in zoo.animals:
            data.append({
                "name": animal.name,
                "species": animal.species
            })
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Animals saved successfully to {filename}.")
    except Exception as e:
        logging.error(f"Error saving animals to file: {e}")