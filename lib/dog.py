#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self._name = None
        self._breed = None
        self.name = name  # Use the property setter
        self.breed = breed  # Use the property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

if __name__ == "__main__":
    fido = Dog("Fido", "Beagle")
    print(fido.name)  
    print(fido.breed) 

    rocky = Dog("Rocky", "German Shepherd")  
    rocky.name = "Rocky the Great Dane with a Very Long Name"  
