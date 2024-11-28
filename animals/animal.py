class Animal:
    '''
    Parent class for different types of animals
    '''
    def __init__(self, 
                 name: str,
                 age: int,
                 type: str
                 ):
        self.name = name
        self.age = age
        self.type = type
        

class Dog(Animal):
    pass

class Cat(Animal):
    pass