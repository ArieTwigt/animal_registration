from animals.animal import Cat, Dog
from typing import Union
import pandas as pd
import sqlite3


class AnimalCollection:


    def __init__(self, name: str):
        self.name = name
        self.animals = [] # 🆕 aangemaakt 

    
    def add_animal(self, animal: Union[Cat, Dog]):
        self.animals.append(animal) # 💾 opgeslagen

    
    def create_animal_table(self):
        # creata a list of dicts from the animals list
        animals_dicts_list = []

        for animal in self.animals:
            animals_dicts_list.append(animal.__dict__)

        # create the data frame
        animals_table = pd.DataFrame(animals_dicts_list)
        animals_table['collection_name'] = self.name

        # add name of collection
        self.animals_table = animals_table



    def save_animals(self):
        con = sqlite3.connect("data.db")

        self.animals_table.to_sql("Animals", con, if_exists="append")