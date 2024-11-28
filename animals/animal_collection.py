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


    def save_animals(self, input_table=None):
        con = sqlite3.connect("data.db")

        if input_table is not None:
            df = pd.read_csv(f"data/{input_table}", sep=";")
            
            df.to_sql("Animals", 
                                  con, 
                                  if_exists="append",
                                  index=False)
        else:
            self.animals_table.to_sql("Animals", 
                                  con, 
                                  if_exists="append",
                                  index=False)
        

class CollectionImport:
    #
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.con = sqlite3.connect("data.db")        


    # method to get an animal
    def get_animal_collection(self):
        
        # get the animal collection
        qry = '''
              SELECT name, age, type, collection_name
              FROM Animals
              WHERE collection_name = ?
              ORDER BY age
              '''
        
        # get the data from the table
        df_animals = pd.read_sql_query(qry, 
                                       self.con,
                                       params=(self.collection_name,)
                                       )
        
        print(df_animals)


def get_available_collections():
    con = sqlite3.connect("data.db")  

    # query for showing collections
    qry = '''
            SELECT DISTINCT(collection_name) as cname
            FROM Animals
            ORDER BY cname
        '''
    
    # get the table with collections
    df_collection_names = pd.read_sql_query(qry,
                                            con)
    
    collections_list = df_collection_names['cname'].unique().tolist()

    return collections_list