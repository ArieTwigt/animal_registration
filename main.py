from animals.animal import Dog, Cat
from animals.animal_collection import AnimalCollection

# initate a Dog
dog_1 = Dog("Rex", 3, "Dog")

# initiate a Cat
cat_1 = Cat("Tom", 2, "Cat")

# initiate an AnimalCollection
animal_collection = AnimalCollection("Arie Collection")

# add the animals
animal_collection.add_animal(dog_1)
animal_collection.add_animal(cat_1)

# creat the table
animal_collection.create_animal_table()

# save the data
animal_collection.save_animals()

pass