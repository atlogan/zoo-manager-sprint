#main.py

from animals import Dog, Cat, Bird
from zoo import Zoo
from file_io import save_animals, load_animals

def main():
    # Create a new zoo
    my_zoo = Zoo()

    # Load animals from file
    if load_animals(my_zoo):
        print("Animals loaded from file.")
    else:
        print("Starting with an empty zoo.")

    while True:
        print("\nMenu:")
        print("1. List animals")
        print("2. Add a new animal")
        print("3. Save animals to file")
        print("4. Load animals from file")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            my_zoo.list_animals()
        elif choice == "2":
            name = input("Enter animal name: ")
            species = input("Enter animal species: ")
            animal_type = input("Enter animal type (Dog/Cat/Bird): ")
            if animal_type == "Dog":
                animal = Dog(name, species)
            elif animal_type == "Cat":
                animal = Cat(name, species)
            elif animal_type == "Bird":
                animal = Bird(name, species)
            else:
                print("Unknown animal type.")
                continue
            my_zoo.add_animal(animal)
        elif choice == "3":
            if save_animals(my_zoo):
                print("Animals saved successfully.")
            else:
                print("Failed to save animals.")
        elif choice == "4":
            if load_animals(my_zoo):
                print("Animals loaded successfully.")
            else:
                print("Failed to load animals.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

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
