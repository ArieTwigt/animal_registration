from animals.animal import Dog, Cat
from animals.animal_collection import AnimalCollection, CollectionImport, get_available_collections
import os
import sys

# ask question what to do
action = input("Add or get animals?(add/get)\n") or "add"



# if add
if action == "add":

    # provide name for collection
    collection_name = input("Name of the collection\n") or ""

    # initiate an AnimalCollection
    animal_collection = AnimalCollection(collection_name)
    
    # bulk  import
    bulk_import = input("Bulk import? (yes/no)\n") or "no"
    
    # check if is import or not
    if bulk_import == "yes":
        print(os.listdir("data"))
        file_name = input("Name of the file:\n")


        animal_collection.save_animals(file_name)

        # stop the program
        sys.exit(0)


    # instructions to add an animal
    name = input("Name of the animal?\n") or ""
    age = int(input("Age of the animal?\n")) or 0
    animal_type = input("Type of the animal (cat/dog)\n") or "dog"
    

    # compose the animal
    if animal_type == "dog":
        # initate a Dog
        dog = Dog(name=name,
                age=age,
                type=animal_type)
        
        # add to the collection
        animal_collection.add_animal(dog)

    elif animal_type == "cat":
        cat = Cat(name=name,
                age=age,
                type=animal_type)
        
        # add to the collection
        animal_collection.add_animal(cat)



    # creat the table
    animal_collection.create_animal_table()

    # save the data
    animal_collection.save_animals()
else:
    collections_list =get_available_collections()
    collections_list_numbered = [f"{id} - {collection}" 
                                 for id, collection 
                                 in enumerate(collections_list)]
    
    print("\n".join(collections_list_numbered))


    selected_collection = int(input("Which collection?\n"))
    

    collection_import = CollectionImport(collections_list[selected_collection])
    
    

    collection_import.get_animal_collection()
    print("Done")   
