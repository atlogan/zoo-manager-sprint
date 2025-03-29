#main.py
import animals
import zoo
import file_io

#Creates a Zoo instance
class Zoo:
    def __init__(self, species):
        self.species = species

#Uses a 'try-except statement to either 
#Add animals manually or Load from file

#Provides interface to list, add, save,
#load, or remove