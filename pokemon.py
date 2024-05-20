#!/usr/bin/python3
"""Python class personal project"""

class Pokemon:
    """Start of the pokemon class that defines a pokemon"""
    count = 0
    types = ("Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug",
            "Ghost", "Fire", "Water", "Grass", "Electric", "Ice", "Dark",
            "Fairy", "Steel", "Dragon")
    
    def __init__(self, name, pokemon_type, trainer):
        """Initial validation for name, pokemon type and trainer"""

        if type(name) is not str:
            raise TypeError("Please enter name of pokemon")
        if name is None or len(name.strip()) == 0:
            raise ValueError("Please enter pokemon name")
        self.__name = name.strip()

        if type(pokemon_type) is not str:
            raise TypeError("Please enter pokemon type")
        if pokemon_type.capitalize() not in Pokemon.types:
            raise ValueError("Must be a valid pokemon type")
        self.__pokemon_type = pokemon_type.capitalize()

        if type(trainer) is not str:
            raise TypeError("Please enter name of pokemon")
        if trainer is None or len(trainer.strip()) == 0:
            raise ValueError("Please enter pokemon name")
        self.__trainer = trainer.strip()

    @property
    def name(self):
        """Getter for pokemon name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Validation for pokemon name"""
        if type(value) is not str:
            raise TypeError("Please enter name of pokemon")
        if value is None or len(value.strip()) == 0:
            raise ValueError("Please enter pokemon name")
        self.__name = value.strip()

    @property
    def pokemon_type(self):
        """Getter for pokemon type"""
        return self.pokemon_type

    @pokemon_type.setter
    def pokemon_type(self, value):
        """Validation for pokemon type"""
        if type(value) is not str:
            raise TypeError("Please enter pokemon type")
        if value.capitalize() not in Pokemon.types:
            raise ValueError("Must be a valid pokemon type")
        self.__pokemon_type = value.capitalize()

    @property
    def trainer(self):
        """Getter for pokemon trainer"""
        return self.__trainer

    @trainer.setter
    def trainer(self, value):
        """Validation for pokemon trainer"""
        if type(value) is not str:
            raise TypeError("Please enter name of pokemon")
        if value is None or len(value.strip()) == 0:
            raise ValueError("Please enter pokemon name")
        self.__trainer = value.strip()