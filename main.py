#main.py
import animals
import zoo
import file_io

#Creates a Zoo object
from animals import Dog, Cat
from zoo import Zoo

def main():
    # Create a new zoo
    my_zoo = Zoo()

    # Create some animals
    dog = Dog("Rex", "Canine")
    cat = Cat("Mittens", "Feline")

    # Add animals to the zoo
    my_zoo.add_animal(dog)
    my_zoo.add_animal(cat)

    # Demonstrate the animals making sounds
    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")

    # Show all animals in the zoo
    print("\nAll animals in the zoo:")
    my_zoo.list_animals()

if __name__ == "__main__":
    main() 

'''
Uses a 'try-except statement to either 
Add animals manually or Load from file
'''


'''
Provides interface to list, add, save,
load, or remove
'''
