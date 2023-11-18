import json


class Fruit:
    def __init__(self, fruitId, name, season):
        self.id = fruitId
        self.name = name
        self.season = season


class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.fruits = []

    def add_fruit(self, name, season, fruitId):
        fruit = Fruit(fruitId, name, season)
        self.fruits.append(fruit)


# Custom encoder for Fruit objects
class FruitEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Fruit):
            return obj.__dict__
        return super().default(obj)
