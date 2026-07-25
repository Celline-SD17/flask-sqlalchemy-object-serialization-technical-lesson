# lib/serialize.py

from pprint import pprint
from marshmallow import Schema, fields

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging
    def give_treat(self):
        self.tail_wagging = True
    def scold(self):
        self.tail_wagging = False


#schema
class DogSchema(Schema):
    name = fields.String()
    breed = fields.String()
    tail_wagging = fields.Boolean()


# create model instance
dog_schema = DogSchema()
dog = Dog(name="Snuggles", breed="Beagle", tail_wagging=True)

dog_dict = dog_schema.dump(dog)
pprint(dog_dict)

dog_json = dog_schema.dumps(dog)
pprint(dog_json)

dog_summary = DogSchema(only=("name", "breed")).dumps(dog)
pprint(dog_summary)

dog_summary = DogSchema(exclude=("tail_wagging", )).dumps(dog)
pprint(dog_summary)

dogs = [Dog(name="Snuggles", breed="Beagle", tail_wagging=True),
        Dog(name="Wags", breed="Collie", tail_wagging=False)]

dictionary_list = DogSchema(many=True).dump(dogs)
pprint(dictionary_list)


json_array = DogSchema(many=True).dumps(dogs)       # dumps returns JSON-encoded list
pprint(json_array) 